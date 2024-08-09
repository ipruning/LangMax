import json

from pydantic import BaseModel, Field


class User(BaseModel):
    id: int
    name: str = Field(..., min_length=1, max_length=100, description="User's full name")
    email: str = Field(..., description="User's email address")


schema = User.model_json_schema()
print(json.dumps(schema, indent=2))
