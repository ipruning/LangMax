import os
from datetime import datetime
from typing import List, Optional

from openai import OpenAI
from pydantic import BaseModel
from rich.console import Console


class Date(BaseModel):
    yyyy: int
    mm: int
    dd: int
    hh: int
    mm: int
    ss: int


class Event(BaseModel):
    title: str
    start_dt: Optional[Date]
    end_dt: Optional[Date]


class DataExtracterResult(BaseModel):
    through: Optional[List[str]]
    events: Optional[List[Event]]


ENTITY_EXTRACTER_SYSTEM_TEMPLATE = """你是一个高度专业、精确且高效的日程记录员，能够细致入微且毫无差错地对用户以文字输入形式传达的日程信息进行全面而深入的提取，并生成清晰明了、详尽准确的日程记录。请使用 yyyy-mm-dd hh:mm:ss 的格式来表示日期和时间。

class Date(BaseModel):
    yyyy: int
    mm: int
    dd: int
    hh: int
    mm: int
    ss: int


class Event(BaseModel):
    title: str
    start_dt: Optional[Date]
    end_dt: Optional[Date]


class DataExtracterResult(BaseModel):
    through: Optional[List[str]]
    events: Optional[List[Event]]
"""


class DataExtracter:
    @staticmethod
    def execute(prompt: str) -> DataExtracterResult:
        client = OpenAI(
            api_key=os.environ.get("OPENAI_API_KEY"),
        )

        completion = client.beta.chat.completions.parse(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": ENTITY_EXTRACTER_SYSTEM_TEMPLATE,
                },
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
            response_format=DataExtracterResult,
        )

        if completion.choices[0].message.parsed is None:
            raise ValueError("OpenAI SDK returned an invalid structured outputs")

        return completion.choices[0].message.parsed


test_prompt = """这周六上午10点，我要在会议室1举行项目启动会议，讨论项目需求和目标，接着下午2点30分，在会议室2我有一个代码审查会议。然后在下周五上午11点要去上海参加一个技术论坛。
"""

date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
formatted_prompt = test_prompt + f"当前日期是 {date}" + f"是星期{datetime.now().weekday()}"

result = DataExtracter.execute(formatted_prompt)

console = Console()

console.rule("[bold]Prompt[/bold]")
console.print(test_prompt)
console.rule("[bold]Result[/bold]")
console.print(result)
