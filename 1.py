import matplotlib.pyplot as plt
import nltk
import numpy as np
import requests
from nltk.tokenize import sent_tokenize
from umap import UMAP

# Download nltk data for sentence tokenization
nltk.download("punkt")


def fetch_hn_content():
    """Fetch content from Hacker News using Jina's s.reader API"""
    endpoint = "https://s.jina.ai/hacker%20news"
    headers = {
        "Accept": "application/json",
        "Authorization": "Bearer $JINA_API_KEY",  # Replace with your API key
    }

    response = requests.get(endpoint, headers=headers)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch HN content: {response.text}")

    return response.json()["data"]


def extract_sentences(articles):
    """Extract sentences from articles"""
    sentences = []
    for article in articles:
        if article.get("content"):
            # Split content into sentences
            article_sentences = sent_tokenize(article["content"])
            sentences.extend(article_sentences)
    return sentences


def get_embeddings(sentences):
    """Generate embeddings using Jina's embeddings API"""
    endpoint = "https://api.jina.ai/v1/embeddings"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer $JINA_API_KEY",  # Replace with your API key
        "Accept": "application/json",
    }

    # Prepare data for embedding
    data = {"model": "jina-embeddings-v2", "input": [{"text": s} for s in sentences]}

    response = requests.post(endpoint, json=data, headers=headers)
    if response.status_code != 200:
        raise Exception(f"Failed to generate embeddings: {response.text}")

    embeddings = [result["embedding"] for result in response.json()["data"]]
    return np.array(embeddings)


def visualize_embeddings(embeddings, sentences):
    """Create UMAP visualization of embeddings"""
    # Reduce dimensionality with UMAP
    umap_model = UMAP(n_components=2, random_state=42)
    reduced_embeddings = umap_model.fit_transform(embeddings)

    # Create scatter plot
    plt.figure(figsize=(12, 8))
    scatter = plt.scatter(reduced_embeddings[:, 0], reduced_embeddings[:, 1], alpha=0.5, s=50)

    # Add hover annotations
    for idx, (x, y) in enumerate(reduced_embeddings):
        plt.annotate(
            sentences[idx][:50] + "...",  # Show first 50 chars
            (x, y),
            xytext=(5, 5),
            textcoords="offset points",
            bbox=dict(facecolor="white", alpha=0.7),
            fontsize=8,
            alpha=0,
        )

    plt.title("UMAP Visualization of Hacker News Sentences")
    plt.xlabel("UMAP Dimension 1")
    plt.ylabel("UMAP Dimension 2")

    return plt


def main():
    print("Fetching Hacker News content...")
    articles = fetch_hn_content()

    print("Extracting sentences...")
    sentences = extract_sentences(articles)
    print(f"Found {len(sentences)} sentences")

    print("Generating embeddings...")
    embeddings = get_embeddings(sentences)

    print("Creating visualization...")
    plt = visualize_embeddings(embeddings, sentences)
    plt.savefig("hn_embeddings.png", dpi=300, bbox_inches="tight")
    print("Visualization saved as 'hn_embeddings.png'")


if __name__ == "__main__":
    main()
