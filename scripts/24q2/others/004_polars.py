from typing import Dict

import numpy as np
import polars as pl

num_rows: int = 5000
rng: np.random.Generator = np.random.default_rng(seed=7)

building_data: Dict[str, pl.Series] = {
    "id": pl.Series("building_id", list(range(num_rows))),
    "building_name": pl.Series("building_name", [f"building_{i}" for i in range(num_rows)]),
    "building_height": pl.Series("building_height", rng.integers(1, 100, num_rows)),
    "building_age": pl.Series("building_age", rng.integers(1, 100, num_rows)),
}
buildings: pl.DataFrame = pl.DataFrame(building_data)

print(buildings.head())
print(buildings.schema)
