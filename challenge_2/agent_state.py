from typing import TypedDict, List, Optional, Dict
from langchain_core.documents import Document
from langchain_community.vectorstores import FAISS

class Message(TypedDict):
    sender: str
    recipient: str
    content: str
    timestamp: str

# class AgentState(TypedDict):
#     user_query: str
#     documents: Optional[List[str]]  
#     short_term_buffer: List[Message]
#     summary_memory: List[Document]
#     vector_store: FAISS
#     latest_message: str

class AgentState(TypedDict):
    user_query: str
    documents: Optional[List[str]]
    retrieved_chunks: Optional[str]
    reasoning: Optional[str]
    tool_plan: Optional[str]
    tool_result: Optional[str]
    short_term_buffer: Optional[List[Dict]]
    summary_memory: Optional[List[Document]]
    vector_store: Optional[FAISS]
    latest_message: Optional[str]
    memory_active: Optional[bool]  # <-- Add this!
