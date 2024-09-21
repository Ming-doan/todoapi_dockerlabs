from typing import Annotated
from pydantic import BaseModel, Field
from fastapi import APIRouter
from fastapi.responses import ORJSONResponse
from controllers.llm import (
    create_todo_by_llm
)


router = APIRouter(prefix="/llm")


class PromptInput(BaseModel):
    prompt: str = Field(..., min_length=1, max_length=100)


@router.post("/create")
def create_todo_by_llm_api(data: PromptInput):
    create_ids = create_todo_by_llm(data.prompt)
    return ORJSONResponse(content={
        "msg": "Create new todo items by llm",
        "data": create_ids
    })
