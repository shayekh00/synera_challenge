from langchain_community.llms import Ollama
from memory.memory_manager import retrieve_relevant_memory
from agent_state import AgentState

llm = Ollama(model="tinyllama")

def reason_over_context(state: AgentState) -> AgentState:
    # Retrieve past memory
    # retrieved_chunks = retrieve_relevant_memory(
    #     query=state["user_query"],
    #     vector_store=state["vector_store"],
    #     state=state,
    # )

    # Build full prompt
    short_term_text = "\n".join(state.get("short_term_buffer", []))
    summary_text = "\n".join([doc.page_content for doc in state.get("summary_memory", [])])
    long_term_text = "\n".join(state.get("retrieved_chunks", ""))

    prompt = f"""You are an engineering assistant.

User query: {state['user_query']}

Recent conversation context:
{short_term_text}

Long-term memory context:
{long_term_text}

Summaries of past interactions:
{summary_text}

Respond to the user query above.
"""

    response = llm.invoke(prompt)

    return {
        **state,
        "latest_message": response
    }
