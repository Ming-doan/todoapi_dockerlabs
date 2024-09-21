import dspy
from datetime import datetime
from models.llm import LLMCreateTodoModel
from models.todo import TodoModel
from configs.gemini import llm
from providers import todo_database


class GenerateTodoItems(dspy.Signature):
    '''
    Generate todo items based on user requirement.
    '''
    prompt = dspy.InputField(description="Request to generate todo items")
    current_date = dspy.InputField(
        description="Current date. Format: YYYY-MM-DD")
    output: LLMCreateTodoModel = dspy.OutputField()


generator = dspy.TypedPredictor(GenerateTodoItems)


def create_todo_by_llm(prompt: str):
    # Generate todo items based on user requirement
    with dspy.context(lm=llm):
        response = generator(
            prompt=prompt, current_date=datetime.now().strftime("%Y-%m-%d"))

    # Create todo items
    create_ids = []
    for _ in range(response.output.replicas):
        id = todo_database.create(TodoModel(
            title=response.output.title,
            finish_date=response.output.finish_date
        ).model_dump())
        create_ids.append(id)

    return create_ids
