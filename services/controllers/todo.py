from pydantic import BaseModel
from providers import todo_database


def get_all_todo():
    return list(todo_database.get_all())


def get_todo_by_id(todo_id: int):
    return todo_database.get_by_id(todo_id)


def create_todo(data: BaseModel):
    return todo_database.create(data.model_dump())


def update_todo(todo_id: int, data: BaseModel):
    return todo_database.update(todo_id, data.model_dump(exclude_defaults=True))


def delete_todo(todo_id: int):
    return todo_database.delete(todo_id)
