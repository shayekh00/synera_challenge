from langchain_community.llms import Ollama
from agent_state import AgentState

llm = Ollama(model="tinyllama")  
TOOL_LIST = """
Available tools:
- Graft Tree: Converts a list into a tree structure.
- Modulus: Computes modulus (e.g. x % 2).
- Dispatch: Splits a list based on a boolean mask.
- Addition: Adds two lists elementwise or a value to a list.
- Combine: Merges branches of data.
- Flatten Tree: Converts tree back to flat list.
"""

PROMPT_TEMPLATE = """
You are a Synera workflow synthesis agent.

User asked: "{user_prompt}"

{tools}

Return a valid ordered sequence of tool invocations needed to solve the task.
Format each tool as: TOOL_NAME(input1, input2, ...) -> output_var
"""

def synthesize_workflow(state: AgentState) -> AgentState:
    user_prompt = state.get("user_query", "Build me a workflow to add 3 to all uneven numbers in the list")
    
    prompt = PROMPT_TEMPLATE.format(
        user_prompt=user_prompt,
        tools=TOOL_LIST
    )

    response = llm.invoke(prompt)

    return {**state, "tool_plan": response}
