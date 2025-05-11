from agent_state import AgentState

def retrieve_example_workflows(state: AgentState) -> AgentState:
    query = state["user_query"]
    results = state["workflow_vector_store"].similarity_search(query, k=1)
    examples = [doc.page_content for doc in results]
    return {**state, "retrieved_workflows": examples}
