
from agent_state import AgentState




def retrieve_relevant_chunks(state: AgentState) -> AgentState:
    retriever = state["vectorstore"].as_retriever()
    top_chunks = retriever.invoke(state["user_query"])
    retrieved_text = "\n\n".join([chunk.page_content for chunk in top_chunks])
    return {**state, "retrieved_chunks": retrieved_text}
