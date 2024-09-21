from pydantic import BaseModel, Field


class LLMCreateTodoModel(BaseModel):
    title: str = Field(..., min_length=1, max_length=100,
                       description="Title of the todo")
    replicas: int = Field(
        1, ge=1, le=10, description="Number of duplicate for todo items.")
    finish_date: str = Field(
        None, description="Finish date of the todo item, Format: YYYY-MM-DD")
