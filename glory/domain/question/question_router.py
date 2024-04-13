from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette import status

from database import get_db

from .services import question_service, answer_service
from .schema import Question, AnswerInput

router = APIRouter(prefix="/api/question")


@router.get("", response_model=list[Question])
def get_question_list(db: Session = Depends(get_db)):
    return question_service.get_question_list(db)


@router.get("/{question_id}", response_model=Question)
def get_question(question_id: int, db: Session = Depends(get_db)):
    return question_service.get_question(db, question_id)


@router.post(
    path="/{question_id}/answer/create", status_code=status.HTTP_204_NO_CONTENT
)
def create_answer(
    question_id: int, answer_input: AnswerInput, db: Session = Depends(get_db)
):
    question = question_service.get_question(db, question_id)
    return answer_service.create_answer(db, question, answer_input)
