from ariadne import convert_kwargs_to_snake_case
from .csv_helper import csv_to_dict, dict_to_csv


# Create new todo
@convert_kwargs_to_snake_case
def resolve_create_todo(obj, info, description, due_date):
    try:
        todoList = csv_to_dict()
        todo = {
            "id": len(todoList),
            "description": description,
            "completed": "False",
            "dueDate": due_date
        }
        todoList.append(todo)
        dict_to_csv(todoList)
        payload = {
            "success": True,
            "todo": todo
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload


# Alter an existing todo
def alter_list(elem, todo_id):
    if elem["id"] == todo_id:
        todo = {
            "id": elem["id"],
            "description": elem["description"],
            "completed": "True",
            "dueDate": elem["dueDate"]
        }
        return todo
    else:
        return elem


# Mark an existing todo as done
@convert_kwargs_to_snake_case
def resolve_mark_done(obj, info, todo_id):
    try:
        todoList = csv_to_dict()
        todo = list(map(lambda elem: alter_list(elem, todo_id), todoList))
        dict_to_csv(todo)
        payload = {
            "success": True,
            "todo": list(filter(lambda elem: elem['id'] == todo_id, csv_to_dict()))[0]
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload


# Delete an existing todo
@convert_kwargs_to_snake_case
def resolve_delete_todo(obj, info, todo_id):
    try:
        todoNewList = list(
            filter(lambda elem: elem['id'] != todo_id, csv_to_dict()))
        dict_to_csv(todoNewList)
        payload = {
            "success": True,
            "todo": todoNewList
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload
