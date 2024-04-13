import datetime

from pydantic import BaseModel, field_validator

__all__ = [
    "Answer",
    "AnswerInput",
]


class Answer(BaseModel):
    id: int
    content: str
    create_date: datetime.datetime


class AnswerInput(BaseModel):
    content: str

    @field_validator("content")
    def not_empty(cls, v: str):
        if not v:
            raise ValueError("빈 값은 허용되지 않습니다.")
        return v
