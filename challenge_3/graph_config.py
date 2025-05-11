from langgraph.graph import StateGraph
from agent_state import AgentState
from agents.tool_retriever import retrieve_relevant_tools
from agents.workflow_retriever import retrieve_example_workflows
from agents.planner import generate_plan
from agents.validator import validate_plan
from agents.formatter import format_output

graph = StateGraph(AgentState)

graph.add_node("tool_retriever", retrieve_relevant_tools)
graph.add_node("workflow_retriever", retrieve_example_workflows)
graph.add_node("planner", generate_plan)
graph.add_node("validator", validate_plan)
graph.add_node("formatter", format_output)

graph.set_entry_point("tool_retriever")
graph.add_edge("tool_retriever", "workflow_retriever")
graph.add_edge("workflow_retriever", "planner")
graph.add_edge("planner", "validator")
graph.add_edge("validator", "formatter")

compiled_graph = graph.compile()
