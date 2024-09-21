from fastapi import APIRouter
from fastapi.responses import ORJSONResponse
from controllers.todo import (
    get_all_todo,
    get_todo_by_id,
    create_todo,
    update_todo,
    delete_todo,
)
from models.todo import TodoModel
import os

router = APIRouter(prefix="/todo")


@router.get("/")
def get_all_todo_api():
    todo_items = get_all_todo()
    return ORJSONResponse(content={
        "msg": "Get all todo items",
        "data": todo_items
    })


@router.post("/")
def create_todo_api(data: TodoModel):
    todo_id = create_todo(data)
    return ORJSONResponse(content={
        "msg": "Create new todo item",
        "data": todo_id
    })


@router.get("/{todo_id}")
def get_todo_by_id_api(todo_id: str):
    todo_item = get_todo_by_id(todo_id)

    # Check if todo_item is None
    if not todo_item:
        return ORJSONResponse(content={
            "msg": f"Todo item with id: {todo_id} not found"
        }, status_code=404)

    return ORJSONResponse(content={
        "msg": f"Get todo item by id: {todo_id}",
        "data": todo_item
    })


@router.put("/{todo_id}")
def update_todo_api(todo_id: str, data: TodoModel):
    update_count = update_todo(todo_id, data)
    return ORJSONResponse(content={
        "msg": f"Update todo item by id: {todo_id}",
        "data": update_count
    })


@router.delete("/{todo_id}")
def delete_todo_api(todo_id: str):
    delete_count = delete_todo(todo_id)
    return ORJSONResponse(content={
        "msg": f"Delete todo item by id: {todo_id}",
        "data": delete_count
    })
