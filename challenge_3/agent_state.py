from typing import TypedDict, List, Optional
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document

class AgentState(TypedDict):
    user_query: str
    retrieved_tools: List[str]
    retrieved_workflows: List[str]
    structured_plan: Optional[str]
    validation_errors: List[str]
    final_output: Optional[dict]
    tool_vector_store: FAISS
    workflow_vector_store: FAISS
