# graph_config.py

from dotenv import load_dotenv
load_dotenv()

from langgraph.graph import StateGraph
from agents.context_loader import load_documents
from agents.retriever import retrieve_relevant_chunks
from agents.reasoning import reason_over_context
from agent_state import AgentState

from memory.memory_manager import manage_memory

def update_memory(state: AgentState) -> AgentState:
    return manage_memory(state)

workflow = StateGraph(AgentState)

# Add nodes
workflow.add_node("load", load_documents)
workflow.add_node("retrieve", retrieve_relevant_chunks)
workflow.add_node("reason", reason_over_context)
workflow.add_node("update_memory", update_memory)

# Set entry point
workflow.set_entry_point("load")

# Wire the node flow
workflow.add_edge("load", "retrieve")
workflow.add_edge("retrieve", "reason")
workflow.add_edge("reason", "update_memory")  # 🔁 Add memory update here

# Compile the graph
graph = workflow.compile()
