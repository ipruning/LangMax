from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

ARTICLE = """
"""

print(summarizer(ARTICLE, max_length=130, min_length=30, do_sample=False))
