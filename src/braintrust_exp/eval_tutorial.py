from autoevals import LevenshteinScorer
from braintrust import Eval

Eval(
    "Say Hi Bot",
    data=lambda: [
        {
            "input": "Foo",
            "expected": "Hi Foo",
        },
        {
            "input": "Bar",
            "expected": "Hello Bar",
        },
    ],  # Replace with your eval dataset
    task=lambda input: "Hi " + input,  # Replace with your LLM call
    scores=[LevenshteinScorer],
)
