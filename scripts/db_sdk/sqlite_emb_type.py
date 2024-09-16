import sqlite3
import struct
from typing import List

import sqlite_vec
from openai import OpenAI


class VectorDB:
    def __init__(self, db_path: str):
        self.db_path = db_path
        self.client = OpenAI()
        self.conn = self._initialize_db()

    def _initialize_db(self) -> sqlite3.Connection:
        conn = sqlite3.connect(self.db_path)
        conn.enable_load_extension(True)
        sqlite_vec.load(conn)
        conn.enable_load_extension(False)

        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='embeddings'")
        if not cursor.fetchone():
            conn.execute("CREATE VIRTUAL TABLE embeddings USING vec0(vector FLOAT[1536])")

        return conn

    def get_embedding(self, text: str) -> List[float]:
        """Get embedding for a given text using OpenAI API"""
        response = self.client.embeddings.create(model="text-embedding-3-small", input=text)
        return response.data[0].embedding

    @staticmethod
    def serialize_vector(vector: List[float]) -> bytes:
        """Serializes a list of floats into a compact "raw bytes" format"""
        return struct.pack("%sf" % len(vector), *vector)

    def insert_entries(self, texts: List[str]):
        with self.conn:
            for text in texts:
                embedding = self.get_embedding(text)
                self.conn.execute(
                    "INSERT INTO embeddings(rowid, vector) VALUES (NULL, ?)", [self.serialize_vector(embedding)]
                )

    def search_similar(self, query_text: str, limit: int = 3) -> List[tuple]:
        query_embedding = self.get_embedding(query_text)
        return self.conn.execute(
            """
            SELECT
              rowid,
              distance
            FROM embeddings
            WHERE vector MATCH ?
            ORDER BY distance
            LIMIT ?
            """,
            [self.serialize_vector(query_embedding), limit],
        ).fetchall()

    def close(self):
        self.conn.close()


def main():
    # Example 1: Import data into the database
    db_path = "vector_db.db"
    vdb = VectorDB(db_path)

    entries = [
        "The quick brown fox jumps over the lazy dog",
        "A journey of a thousand miles begins with a single step",
        "To be or not to be, that is the question",
        "All that glitters is not gold",
        "Where there's a will, there's a way",
    ]

    vdb.insert_entries(entries)
    print(f"Imported {len(entries)} entries into the database")
    vdb.close()

    # Example 2: Query for similar entries
    vdb = VectorDB(db_path)
    query_text = "What is the meaning of life?"
    results = vdb.search_similar(query_text, limit=3)

    print(f"\nQuery text: '{query_text}'")
    print("Top 3 similar results:")
    for i, (rowid, distance) in enumerate(results, 1):
        print(f"{i}. ID: {rowid}, Distance: {distance:.4f}")
        if 0 <= rowid - 1 < len(entries):
            print(f"   Text: {entries[rowid - 1]}")
        else:
            print(f"   Text: ID {rowid} not in the entries list")

    vdb.close()


if __name__ == "__main__":
    main()
