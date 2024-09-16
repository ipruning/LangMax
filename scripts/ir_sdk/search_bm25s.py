from pathlib import Path
from typing import List, Tuple

import bm25s
import Stemmer


class BM25Searcher:
    def __init__(self):
        self.index_path: Path | None = None
        self.corpus: List[str] | None = None
        self.stemmer: Stemmer.Stemmer | None = None
        self.bm25_searcher: bm25s.BM25 | None = None

    def search(self, query: str, top_k: int = 3) -> List[Tuple[str, float]]:
        if not self.index_path or not self.bm25_searcher or not self.corpus or not self.stemmer:
            raise RuntimeError("Search index not properly initialized.")

        tokenized_query = bm25s.tokenize(query, stemmer=self.stemmer)
        search_results, relevance_scores = self.bm25_searcher.retrieve(tokenized_query, corpus=self.corpus, k=top_k)

        return [(search_results[0, i], relevance_scores[0, i]) for i in range(search_results.shape[1])]

    def _create_example_index(self):
        self.index_path = Path("data/test_index_bm25s")
        self.corpus = [
            "a cat is a feline and likes to purr",
            "a dog is the human's best friend and loves to play",
            "a bird is a beautiful animal that can fly",
            "a fish is a creature that lives in water and swims",
        ]

        self.bm25_searcher = bm25s.BM25()
        self.stemmer = Stemmer.Stemmer("english")

        if not self.index_path or not self.bm25_searcher or not self.corpus or not self.stemmer:
            raise RuntimeError("Search index not properly initialized.")

        self.bm25_searcher.index(bm25s.tokenize(self.corpus, stopwords="en", stemmer=self.stemmer))
        self.bm25_searcher.save(self.index_path, corpus=self.corpus)

    def _create_example_search(self):
        if not all([self.index_path, self.corpus, self.stemmer]):
            self._create_example_index()

        print(self.search("lives in water"))
