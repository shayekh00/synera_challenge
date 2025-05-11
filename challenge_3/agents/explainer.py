from langchain_community.llms import Ollama
from agent_state import AgentState

llm = Ollama(model="tinyllama")

EXPLAIN_PROMPT = """
You are an expert code interpreter.

Explain in clear, step-by-step language what this workflow is doing:

{code}

The explanation should focus on what each step does and why it contributes to solving the user’s task.
Do not just repeat the code. Do not output code or comments.
"""

def explain_code(state: AgentState) -> AgentState:
    code = state["retrieved_workflows"]
    prompt = EXPLAIN_PROMPT.format(code=code)
    explanation = llm.invoke(prompt).strip()

    return {"description": explanation} 
