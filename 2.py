from typing import List

import polars as pl
from pydantic import BaseModel
from rich import print


class Item(BaseModel):
    id: int
    name: str
    value: float


df = pl.DataFrame({"id": [1, 2, 3], "name": ["item1", "item2", "item3"], "value": [10.5, 20.75, 30.0]})

data_dicts = df.to_dicts()

items: List[Item] = [Item(**item) for item in data_dicts]

for item in items:
    print(item)
