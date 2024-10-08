from enum import Enum
from typing import List, Union

import openai
from pydantic import BaseModel
from rich import print


class Query(BaseModel):
    """
    A class to represent a database query.

    Attributes:
    ----------
    table_name : Table
        The name of the table to query.
    columns : List[Column]
        The columns to select in the query.
    conditions : List[Condition]
        The conditions to apply to the query.
    order_by : OrderBy
        The order in which to sort the results.
    """

    class Table(str, Enum):
        """Enum to represent the table names."""

        orders = "orders"
        customers = "customers"
        products = "products"

    table_name: Table

    class Column(str, Enum):
        """Enum to represent the column names."""

        id = "id"
        status = "status"
        expected_delivery_date = "expected_delivery_date"
        delivered_at = "delivered_at"
        shipped_at = "shipped_at"
        ordered_at = "ordered_at"
        canceled_at = "canceled_at"

    columns: List[Column]

    class Condition(BaseModel):
        """
        A class to represent a condition in the query.

        Attributes:
        ----------
        column : str
            The column to apply the condition to.
        operator : Operator
            The operator to use in the condition.
        value : Union[str, int, DynamicValue]
            The value to compare the column to.
        """

        column: str

        class Operator(str, Enum):
            """Enum to represent the operators for conditions."""

            eq = "="
            gt = ">"
            lt = "<"
            le = "<="
            ge = ">="
            ne = "!="

        operator: Operator

        class DynamicValue(BaseModel):
            """
            A class to represent a dynamic value in the condition.

            Attributes:
            ----------
            column_name : str
                The name of the column to use as the value.
            """

            column_name: str

        value: Union[str, int, DynamicValue]

    conditions: List[Condition]

    class OrderBy(str, Enum):
        """Enum to represent the order by options."""

        asc = "asc"
        desc = "desc"

    order_by: OrderBy


client = openai.OpenAI()
completion = client.beta.chat.completions.parse(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant. The current date is August 6, 2024. You help users query for the data they are looking for by calling the query function.",
        },
        {
            "role": "user",
            "content": "look up all my orders in may of last year that were fulfilled but not delivered on time",
        },
    ],
    tools=[
        openai.pydantic_function_tool(Query),
    ],
)

tool_call = (completion.choices[0].message.tool_calls or [])[0]
print(tool_call.function.parsed_arguments)
