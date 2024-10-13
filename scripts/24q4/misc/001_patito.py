from typing import Literal

import patito as pt
import polars as pl


class Product(pt.Model):
    product_id: int = pt.Field(unique=True)
    name: str
    temperature_zone: Literal["dry", "cold", "frozen"]
    demand_percentage: float = pt.Field(constraints=pt.field.sum() == 100.0)


invalid_product_df = pl.DataFrame(
    {
        "product_id": [64, 64],
        "name": ["Pizza", "Cereal"],
        "temperature_zone": ["oven", "dry"],
        "demand_percentage": [0.07, 0.16],
    }
)

Product.validate(invalid_product_df)
