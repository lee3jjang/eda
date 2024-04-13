import datetime

from sqlalchemy.orm import Session

from models import Question, Answer

from ..schema import AnswerInput


def get_answer(): ...
def get_answer_list(): ...
def create_answer(db: Session, question: Question, answer_input: AnswerInput):
    answer = Answer(
        question=question,
        create_date=datetime.datetime.now(),
        **answer_input.__dict__,
    )
    db.add(answer)
    db.commit()


def update_answer(): ...
def delete_answer(): ...
