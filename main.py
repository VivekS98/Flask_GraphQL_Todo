from api import app
from ariadne import load_schema_from_path, make_executable_schema, graphql_sync, snake_case_fallback_resolvers, ObjectType
from ariadne.constants import PLAYGROUND_HTML
from flask import request, jsonify
from api.query import resolve_todo, resolve_todos
from api.mutation import resolve_create_todo, resolve_mark_done, resolve_delete_todo

query = ObjectType("Query")

# Configure Queries in  Ariadne
query.set_field("todos", resolve_todos)
query.set_field("todo", resolve_todo)

# Configure Mutations in  Ariadne
mutation = ObjectType("Mutation")
mutation.set_field("createTodo", resolve_create_todo)
mutation.set_field("markDone", resolve_mark_done)
mutation.set_field("deleteTodo", resolve_delete_todo)

# Configure the schema file in Ariadne
type_defs = load_schema_from_path("schema.graphql")
schema = make_executable_schema(
    type_defs, query, mutation, snake_case_fallback_resolvers
)


# GraphQL Playground Query route
@app.route("/graphql", methods=["GET"])
def graphql_playground():
    return PLAYGROUND_HTML, 200


# GraphQL Playground Mutation route
@app.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()

    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
        debug=app.debug
    )

    status_code = 200 if success else 400
    return jsonify(result), status_code
