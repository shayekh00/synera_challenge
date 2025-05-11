from agent_state import AgentState

import re


def extract_code_block_only(text: str) -> str:
    """
    Extracts the first Python (or generic) code block from text using triple backticks.
    Prioritizes ```python blocks, falls back to ``` blocks if necessary.
    """
    # Try to extract ```python ... ``` first
    match = re.search(r"```python\s*(.*?)```", text, re.DOTALL | re.IGNORECASE)
    if match:
        return match.group(1).strip()

    # Fallback: extract any triple-backtick code block
    match = re.search(r"```\s*(.*?)```", text, re.DOTALL)
    if match:
        return match.group(1).strip()

    # No code block found
    return ""  # Explicitly return empty string if no block is found


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

