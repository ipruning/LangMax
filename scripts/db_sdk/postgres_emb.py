import os

import psycopg
from openai import OpenAI
from pgvector.psycopg import register_vector


def setup_db():
    conn = psycopg.connect(
        dbname=os.getenv("NEON_DB_NAME"),
        user=os.getenv("NEON_DB_USER"),
        password=os.getenv("NEON_DB_PASSWORD"),
        host=os.getenv("NEON_DB_HOST"),
        port=os.getenv("NEON_DB_PORT"),
        sslmode=os.getenv("NEON_DB_SSLMODE"),
        autocommit=True,
    )
    conn.execute("CREATE EXTENSION IF NOT EXISTS vector")
    register_vector(conn)
    conn.execute("DROP TABLE IF EXISTS docs")
    conn.execute("CREATE TABLE docs (id bigserial PRIMARY KEY, content text UNIQUE, embedding vector(1536))")
    return conn


def add_docs(conn, texts):
    client = OpenAI()
    embed_response = client.embeddings.create(input=texts, model="text-embedding-3-small")
    embeddings = [v.embedding for v in embed_response.data]

    for content, embedding in zip(texts, embeddings):
        conn.execute(
            """
            INSERT INTO docs (content, embedding) 
            VALUES (%s, %s) 
            ON CONFLICT (content) DO NOTHING
            """,
            (content, embedding),
        )


def get_top_3_similar(conn, query):
    client = OpenAI()
    query_embed_response = client.embeddings.create(input=[query], model="text-embedding-3-small")
    query_embedding = query_embed_response.data[0].embedding

    similar_docs = conn.execute(
        """
        SELECT content 
        FROM docs 
        ORDER BY embedding <=> %s::vector 
        LIMIT 3
        """,
        (query_embedding,),
    ).fetchall()

    return [doc[0] for doc in similar_docs]


conn = setup_db()
sample_texts = [
    "The elusive purple unicorn danced gracefully under the shimmering aurora borealis, its horn glowing with an otherworldly iridescence that captivated all who witnessed the spectacle.",
    "In a parallel universe, sentient vegetables ruled the planet, holding annual carrot conventions to discuss the latest advancements in photosynthesis technology and root system optimization.",
    "The time-traveling toaster, accidentally set to 'Medieval Europe,' found itself in the court of King Arthur, where it proceeded to revolutionize breakfast with its ability to create perfectly crisp toast.",
    "Deep in the quantum realm, subatomic particles engaged in elaborate soap operas, with electrons dramatically orbiting protons while neutrons watched from the sidelines, occasionally intervening in their cosmic drama.",
    "The last remaining library on Mars housed a collection of Earth's most perplexing conspiracy theories, which Martian scholars studied with great interest, trying to decipher the peculiarities of human imagination.",
    "The dog is barking",
    "The cat is purring",
    "The bear is growling",
]
add_docs(conn, sample_texts)

query = "中世纪面包机和猫猫"
top_3_results = get_top_3_similar(conn, query)
print(f"Top 3 similar documents for '{query}':")
for result in top_3_results:
    print(result)
