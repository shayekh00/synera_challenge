from langchain_community.vectorstores import FAISS

from langchain.text_splitter import RecursiveCharacterTextSplitter
from agent_state import AgentState
from langchain_huggingface import HuggingFaceEmbeddings




def retrieve_relevant_chunks(state: AgentState) -> AgentState:
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(state["documents"])
    
    embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    db = FAISS.from_documents(chunks, embedding_model)
    retriever = db.as_retriever()
    
    top_chunks = retriever.invoke(state["user_query"])
    retrieved_text = "\n\n".join([chunk.page_content for chunk in top_chunks])

    return {**state, "retrieved_chunks": retrieved_text}
