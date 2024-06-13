"""
Extract full next-token probabilities via language model APIs
"""

import openlogprobs

extracted_logprobs, num_calls = openlogprobs.extract_logprobs("gpt-3.5-turbo-instruct", "i like pie", method="topk")

print(extracted_logprobs)
