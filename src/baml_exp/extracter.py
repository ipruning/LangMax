from src.baml_client import b
from src.baml_client.types import Resume

p = """Jason Doe
Python, Rust
University of California, Berkeley, B.S.
in Computer Science, 2020
Also an expert in Tableau, SQL, and C++
"""
r = b.ExtractResume(p)

assert isinstance(r, Resume)

print(r.name)
print(r.email)
print(r.experience)
print(r.skills)

p = """I want to cancel my order"""

r = b.ClassifyMessage(p)
print(r)
