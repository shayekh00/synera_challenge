from langchain_community.vectorstores import FAISS

from langchain.text_splitter import RecursiveCharacterTextSplitter
from agent_state import AgentState
from langchain_huggingface import HuggingFaceEmbeddings
from memory.memory_manager import retrieve_relevant_memory

def retrieve_relevant_chunks(state: AgentState) -> AgentState:
    if not state.get("memory_active", False):
        # First run: use only documents
        splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        chunks = splitter.split_documents(state["documents"])
        embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
        db = FAISS.from_documents(chunks, embedding_model)
        retriever = db.as_retriever()
        top_chunks = retriever.invoke(state["user_query"])
        retrieved_text = "\n\n".join([chunk.page_content for chunk in top_chunks])
        return {**state, "retrieved_chunks": retrieved_text}
    
    else:
        # Subsequent calls: use hybrid memory
        top_chunks = retrieve_relevant_memory(
            query=state["user_query"],
            state=state,
            vector_store=state["vector_store"]
        )
        return {**state, "retrieved_chunks": "\n\n".join(top_chunks)}
