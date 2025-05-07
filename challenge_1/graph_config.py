# graph_config.py
from dotenv import load_dotenv
load_dotenv()

from langgraph.graph import StateGraph
from agents.context_loader import load_documents
from agents.retriever import retrieve_relevant_chunks
from agents.reasoning import reason_over_context
from agent_state import AgentState




workflow = StateGraph(AgentState)

workflow.add_node("load", load_documents)
workflow.add_node("retrieve", retrieve_relevant_chunks)
workflow.add_node("reason", reason_over_context)
workflow.set_entry_point("load")

workflow.add_edge("load", "retrieve")
workflow.add_edge("retrieve", "reason")


graph = workflow.compile()
