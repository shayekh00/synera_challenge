from typing import TypedDict, List, Optional
from langchain_core.documents import Document
from langchain_community.vectorstores import FAISS

class Message(TypedDict):
    sender: str
    recipient: str
    content: str
    timestamp: str

class AgentState(TypedDict):
    user_query: str
    documents: Optional[List[str]]  
    short_term_buffer: List[Message]
    summary_memory: List[Document]
    vector_store: FAISS
    latest_message: str
    tool_plan: Optional[str]
