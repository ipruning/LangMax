from dotenv import load_dotenv
from sglang import OpenAI, function, gen, set_default_backend

load_dotenv()

set_default_backend(OpenAI("gpt-4o"))


@function
def text_qa(s, question):
    s += "Q: " + question + "\n"
    s += "A:" + gen("answer", stop="\n")


state = text_qa.run(question="What is the capital of France?", temperature=0.1, stream=True)  # type: ignore

for out in state.text_iter():
    print(out, end="", flush=True)
