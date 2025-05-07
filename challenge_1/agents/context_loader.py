# context_loader.py

from loaders.pdf_loader import load_pdf_documents
from agent_state import AgentState


def load_documents(state: AgentState) -> AgentState:
    docs = load_pdf_documents(state["documents"])
    return {**state, "documents": docs}
