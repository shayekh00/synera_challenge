# from langchain_community.vectorstores import FAISS

# from langchain.text_splitter import RecursiveCharacterTextSplitter
# from agent_state import AgentState
# from langchain_huggingface import HuggingFaceEmbeddings

from agent_state import AgentState
def retrieve_relevant_tools(state: AgentState) -> AgentState:
    query = state["user_query"]
    results = state["tool_vector_store"].similarity_search(query, k=15)
    tools = [doc.page_content for doc in results]
    return {**state, "retrieved_tools": tools}
