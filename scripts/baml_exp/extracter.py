import asyncio

from baml_client import b
from baml_client.types import Resume


async def main():
    resume_text = """Jason Doe\nPython, Rust\nUniversity of California, Berkeley, B.S.\nin Computer Science, 2020\nAlso an expert in Tableau, SQL, and C++\n"""

    resume: Resume = await b.ExtractResume(resume_text)

    assert isinstance(resume, Resume)

    print(resume)


if __name__ == "__main__":
    asyncio.run(main())
