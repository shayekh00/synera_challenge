from agent_state import AgentState

import re
def extract_code_only(text: str) -> str:
    lines = text.splitlines()
    return "\n".join([
        line for line in lines 
        if re.match(r"^\s*\w[\w\d_]*\s*=\s*\w[\w\d_]*\(.*\)$", line.strip()) or 
           re.match(r"^\s*\w[\w\d_]*,\s*\w[\w\d_]*\s*=\s*\w[\w\d_]*\(.*\)$", line.strip())
    ])


def format_output(state: AgentState) -> AgentState:
    clean_workflow = extract_code_only(state["structured_plan"])
    return {
        **state,
        "final_output": {
            "Title": state["user_query"],
            "Description": f"This workflow was generated for the task: {state['user_query']}",
            "workflow": clean_workflow
        }
    }
