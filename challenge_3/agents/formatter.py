from agent_state import AgentState

import re
def extract_code_only(text: str) -> str:
    lines = text.splitlines()
    return "\n".join([
        line for line in lines 
        if re.match(r"^\s*\w[\w\d_]*\s*=\s*\w[\w\d_]*\(.*\)$", line.strip()) or 
           re.match(r"^\s*\w[\w\d_]*,\s*\w[\w\d_]*\s*=\s*\w[\w\d_]*\(.*\)$", line.strip())
    ])


def extract_code_block_only(workflow_text: str) -> str:
    """
    Extracts just the first Python code block from a mixed description/code string.
    """
    match = re.search(r"```python(.*?)```", workflow_text, re.DOTALL)
    if match:
        return match.group(1).strip()
    return workflow_text.strip()  # fallback: return whole thing if no code block found

def format_output(state: AgentState) -> AgentState:
    workflow_text = state["retrieved_workflows"]
    extracted_code = extract_code_block_only(workflow_text)

    return {
        **state,
        "final_output": {
            "Title": state["user_query"],
            "Description": f"This workflow was generated for the task: {state['description']}",
            "workflow": extracted_code
        }
    }

