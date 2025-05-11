
from langchain_community.llms import Ollama
from agent_state import AgentState

llm = Ollama(model="tinyllama")

PLANNER_PROMPT = """

"{user_prompt}"

Wrte ONLY python code only using Example Usage snippet from all the {tool_summaries}.

NOTHING ELSE.
"""


def retrieve_example_workflows(state: AgentState) -> AgentState:

    user_prompt = state["user_query"]
    tool_summaries = "\n".join(state["retrieved_tools"])  # already retrieved from FAISS
    # print("Tool summaries:", tool_summaries)

    prompt = PLANNER_PROMPT.format(
        user_prompt=user_prompt,
        tool_summaries=tool_summaries
    )

    result = llm.invoke(prompt).strip()
    return {**state, "retrieved_workflows": result}