from sqlalchemy.orm import Session

from models.question.question import Question


def get_question(db: Session, question_id: int) -> Question:
    return db.query(Question).get(question_id)


def get_question_list(db: Session) -> list[Question]:
    return db.query(Question).order_by(Question.create_date.desc()).all()


def create_question(): ...
def update_question(): ...
def delete_question(): ...
