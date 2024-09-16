import os
from datetime import date

import logfire
from pydantic import BaseModel

logfire.configure(token=os.getenv("LOGFIRE_TOKEN"))


class User(BaseModel):
    name: str
    country_code: str
    dob: date


user = User(
    name="Anne",
    country_code="USA",
    dob=date.fromisoformat("2000-01-01"),
)

logfire.info("user processed: {user!r}", user=user)
