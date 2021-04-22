from ariadne import convert_kwargs_to_snake_case
from .csv_helper import csv_to_dict, dict_to_csv


# Get all todos
def resolve_todos(obj, info):
    try:
        payload = {
            "success": True,
            "todos": csv_to_dict()
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    print(payload)
    return payload


# Get a spectfic todo
@convert_kwargs_to_snake_case
def resolve_todo(obj, info, todo_id):
    print(todo_id)
    try:
        payload = {
            "success": True,
            "todo": list(filter(lambda elem: elem['id'] == todo_id, csv_to_dict()))[0]
        }

    except AttributeError:  # todo not found
        payload = {
            "success": False,
            "errors": [f"Todo item matching id {todo_id} not found"]
        }
    print(payload)
    return payload
