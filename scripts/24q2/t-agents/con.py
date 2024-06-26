import controlflow as cf
from pydantic import BaseModel

# create an agent to write a research report
author = cf.Agent(
    name="Deep Thought",
    instructions="Use a formal tone and clear language",
)


class ResearchTopic(BaseModel):
    title: str
    keywords: list[str]


@cf.flow
def research_workflow() -> str:
    # Task 1: the default agent will work with the user to choose a topic
    topic = cf.Task(
        "Work with the user to come up with a research topic",
        result_type=ResearchTopic,
        user_access=True,
    )

    # Task 2: the default agent will create an outline based on the topic
    outline = cf.Task("Create an outline", context=dict(topic=topic))

    # Task 3: the author agent will write a first draft
    draft = cf.Task("Write a first draft", context=dict(outline=outline), agents=[author])

    return draft


# run the workflow
result = research_workflow()
print(result)
