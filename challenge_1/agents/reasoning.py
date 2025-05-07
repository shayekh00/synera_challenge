#reasoning.py

from langchain_community.llms import Ollama
from agent_state import AgentState 

# Initialize the Ollama LLM
llm = Ollama(model="tinyllama")  
# Define the reasoning prompt template
reasoning_template = """You are an engineering assistant.

User query:
{user_query}

Context:
{retrieved_chunks}

What is the recommended next action?
"""

def reason_over_context(state: AgentState) -> AgentState:
    # Fill in the prompt
    prompt = reasoning_template.format(
        user_query=state["user_query"],
        retrieved_chunks=state.get("retrieved_chunks", "No context provided.")
    )
    
    # Generate reasoning
    response = llm.invoke(prompt)
    
    # Store result in state and return
    return {**state, "reasoning": response}
