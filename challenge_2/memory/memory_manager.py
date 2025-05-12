# memory_manager.py

from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_core.documents import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from typing import List, Dict

from langchain_community.llms import Ollama

llm = Ollama(model="tinyllama")

embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
text_splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=50)

def initialize_vector_store() -> FAISS:
    return FAISS.from_documents([], embedding_model)

def add_messages_to_vector_store(messages: List[str], vector_store: FAISS):
    docs = [Document(page_content=m) for m in messages]
    chunks = text_splitter.split_documents(docs)
    vector_store.add_documents(chunks)

# def retrieve_relevant_memory(query: str, vector_store: FAISS,state: Dict, k=5) -> List[str]:
#     top_docs = vector_store.similarity_search(query, k=k)
#     return [doc.page_content for doc in top_docs]

def retrieve_relevant_memory(query: str, vector_store: FAISS, state: Dict, k=5) -> List[str]:
    vector_store = state["vector_store"]
    summary_memory = state.get("summary_memory", [])
    short_term_buffer = state.get("short_term_buffer", [])

    # Vector store retrieval
    vector_chunks = vector_store.similarity_search(query, k=k)
    vector_texts = [doc.page_content for doc in vector_chunks]

    # Search summaries (simple keyword match, or vector embed + search)
    summary_hits = [
        doc.page_content for doc in summary_memory
        if query.lower() in doc.page_content.lower()
    ]

    # Combine recent short-term memory (fresh context)
    buffer_context = short_term_buffer[-k:]

    # Merge all sources
    return buffer_context + summary_hits + vector_texts


def summarize_messages(messages: List[str]) -> str:
    prompt = """Summarize the following agent interaction history:

{history}

Summary:""".format(history="\n".join(messages))
    return llm.invoke(prompt)

def manage_memory(state: Dict, max_short_term: int = 5) -> Dict:
    # Step 1: Add new message to short-term buffer
    buffer = state.get("short_term_buffer", [])
    new_message = state.get("latest_message")
    if new_message:
        buffer.append(new_message)
        state["short_term_buffer"] = buffer[-max_short_term:]  # truncate

        # Step 2: Add to vector store
        add_messages_to_vector_store([new_message], state["vector_store"])

        # Step 3: Optionally summarize older messages
        if len(buffer) > max_short_term:
            summary = summarize_messages(buffer[:-max_short_term])
            summary_doc = Document(page_content=summary, metadata={"type": "summary"})
            state.setdefault("summary_memory", []).append(summary_doc)

    state["memory_active"] = True

    return state
