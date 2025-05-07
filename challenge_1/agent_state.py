# types/agent_state.py

from typing import TypedDict, Optional, List

class AgentState(TypedDict):
    user_query: str
    documents: Optional[List[str]]  # paths or raw text
    retrieved_chunks: Optional[str]
    reasoning: Optional[str]
    tool_plan: Optional[str]
    tool_result: Optional[str]
