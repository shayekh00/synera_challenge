# agent_state.py
from langchain_core.documents import Document
from typing import TypedDict, List, Union

from typing import TypedDict, Optional, List

# class AgentState(TypedDict):
#     user_query: str
#     documents: Optional[List[str]]  # paths or raw text
#     retrieved_chunks: Optional[str]
#     reasoning: Optional[str]
#     tool_plan: Optional[str]
#     tool_result: Optional[str]

from langchain_community.vectorstores import FAISS

class AgentState(TypedDict):
    user_query: str
    documents: Optional[List[str]]  # initial paths only
    vectorstore: Optional[FAISS]
    retrieved_chunks: Optional[str]
    reasoning: Optional[str]
    tool_plan: Optional[str]
    tool_result: Optional[str]
