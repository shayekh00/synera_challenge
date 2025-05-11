import re
from agent_state import AgentState

def validate_plan(state: AgentState) -> AgentState:
    plan = state["structured_plan"]
    tools = {tool.split(":")[0].strip() for tool in state["retrieved_tools"]}
    errors = []
    
    for line in plan.strip().splitlines():
        match = re.match(r"(\w[\w\s]+)\(([^)]*)\)\s*->\s*(\w+)", line)
        if not match:
            errors.append(f"Invalid format: {line}")
            continue
        tool, _, _ = match.groups()
        if tool.strip() not in tools:
            errors.append(f"Unknown tool: {tool}")

    return {**state, "validation_errors": errors}
