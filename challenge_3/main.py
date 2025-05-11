from vectorstores.tool_store import initialize_tool_store
from vectorstores.workflow_store import initialize_workflow_store
from graph_config import compiled_graph

tool_vector_store = initialize_tool_store()
workflow_vector_store = initialize_workflow_store()


initial_state = {
    "user_query": "Build me a workflow to add 3 to all uneven numbers in the list.",
    "tool_vector_store": initialize_tool_store(),
    "workflow_vector_store": initialize_workflow_store(),
}

result = compiled_graph.invoke(initial_state)
print(result["final_output"])
