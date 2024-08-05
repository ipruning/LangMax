from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from llama_index.core import download_loader
from ragas.testset.evolutions import multi_context, reasoning, simple  # type: ignore
from ragas.testset.generator import TestsetGenerator  # type: ignore

SemanticScholarReader = download_loader("SemanticScholarReader")

loader = SemanticScholarReader()
query_space = "large language models"
documents = loader.load_data(query=query_space, limit=100)

# generator with openai models
generator_llm = ChatOpenAI(model="gpt-3.5-turbo-16k")
critic_llm = ChatOpenAI(model="gpt-4")
embeddings = OpenAIEmbeddings()

generator = TestsetGenerator.from_langchain(generator_llm, critic_llm, embeddings)


distributions = {simple: 0.5, multi_context: 0.4, reasoning: 0.1}

# generate testset
testset = generator.generate_with_llamaindex_docs(documents, 10, distributions)
testset.to_pandas()

print(testset)
