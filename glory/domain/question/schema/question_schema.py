import datetime

from pydantic import BaseModel
from .answer_schema import Answer

__all__ = ["Question"]


class Question(BaseModel):
    id: int
    subject: str
    content: str
    create_date: datetime.datetime
    answers: list[Answer] = []
