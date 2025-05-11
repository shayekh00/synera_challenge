from langchain_community.llms import Ollama
from agent_state import AgentState


llm = Ollama(model="tinyllama")

PLANNER_PROMPT = """
You are a workflow generation agent.

The user has requested:
"{prompt}"

You may only use tools described below, as if they are Python functions. 
Each tool must be used by assigning its output to a variable, like:

output = tool_name(arg1, arg2)

Use only the tools provided here:
{tools}

Here are some example workflows (format your output like these):
{examples}

Generate ONLY Python-style code. NO explanations. NO comments.
"""



def generate_plan(state: AgentState) -> AgentState:
    prompt = PLANNER_PROMPT.format(
        prompt=state["user_query"],
        tools="\n".join(state["retrieved_tools"]),
        examples="\n".join(state.get("retrieved_workflows", []))  
    )
    result = llm.invoke(prompt).strip()
    return {**state, "structured_plan": result}

