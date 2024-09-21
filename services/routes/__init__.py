from fastapi import APIRouter
from .todo import router as todo_router
from .llm import router as llm_router


api_router = APIRouter(prefix="/api")

api_router.include_router(todo_router)
api_router.include_router(llm_router)
