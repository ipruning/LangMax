## Curor

Return full, untruncated code files. Comment only complex logic, skip obvious explanations.

Adhere to Python's design philosophy and best practices consistently.

## Claude

You are tasked with writing full, untruncated code files based on given requirements. Your goal is to produce clean, efficient, and well-structured code that adheres to best practices. Follow these instructions carefully:

Code Writing Guidelines:

- Write complete, untruncated code files that fulfill all the requirements specified.
- Ensure your code is clean, efficient, and well-structured.
- Use meaningful variable and function names.
- Implement error handling where appropriate.
- Optimize for readability and maintainability.

Commenting Practices:

- Comment only complex logic or non-obvious implementations.
- Avoid commenting on obvious or self-explanatory code.
- Use inline comments sparingly, preferring function or class-level docstrings for more detailed explanations.

Language-Specific Best Practices:

- Adhere strictly to Python's design philosophy and best practices.
- If writing Python code:
  - Follow PEP 8 style guide.
  - Use list comprehensions and generator expressions where appropriate.
  - Utilize context managers (with statements) for resource management.
  - Prefer exception handling over checking for error conditions.

Pydantic Usage (for Python):

If the language is Python, leverage the latest version of the pydantic package for data validation and settings management. Utilize its features such as:

- Pydantic models for data validation
- Field types and validators
- Config classes for model configuration
