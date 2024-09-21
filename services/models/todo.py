from pydantic import BaseModel, Field


class TodoModel(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    description: str = Field("", min_length=1, max_length=500)
    finish_date: str = Field(None)
    is_done: bool = Field(False)
