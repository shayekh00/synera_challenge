from langgraph.graph import StateGraph
from agent_state import AgentState
from agents.tool_retriever import retrieve_relevant_tools
from agents.workflow_retriever import retrieve_example_workflows
from agents.formatter import format_output
from agents.explainer import explain_code

graph = StateGraph(AgentState)

graph.add_node("tool_retriever", retrieve_relevant_tools)
graph.add_node("workflow_retriever", retrieve_example_workflows)
graph.add_node("formatter", format_output)
graph.add_node("explainer", explain_code)

graph.set_entry_point("tool_retriever")
graph.add_edge("tool_retriever", "workflow_retriever")
graph.add_edge("workflow_retriever", "explainer")
graph.add_edge("explainer", "formatter")

compiled_graph = graph.compile()
