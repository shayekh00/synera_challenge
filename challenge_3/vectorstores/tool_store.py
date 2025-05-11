import faiss
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEmbeddings

# Example tool registry (you'll likely load from a file/DB later)
TOOL_REGISTRY = [
    {
        "tool_name": "Graft Tree",
        "description": "Converts a list into a tree structure.",
        "inputs": ["list"],
        "outputs": ["tree"]
    },
    {
        "tool_name": "Modulus",
        "description": "Computes modulus (e.g. x % 2).",
        "inputs": ["list", "int"],
        "outputs": ["mask"]
    },
    {
        "tool_name": "Dispatch",
        "description": "Splits a list based on a boolean mask.",
        "inputs": ["list", "mask"],
        "outputs": ["true_branch", "false_branch"]
    },
    # Add more tools here...
]

def format_tool(tool: dict) -> str:
    return (
        f"Tool: {tool['tool_name']}\n"
        f"Inputs: {', '.join(tool['inputs'])}\n"
        f"Outputs: {', '.join(tool['outputs'])}\n"
        f"Description: {tool['description']}"
    )

def initialize_tool_store() -> FAISS:
    embed_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    tool_docs = [
        Document(page_content=format_tool(tool), metadata={"tool_name": tool["tool_name"]})
        for tool in TOOL_REGISTRY
    ]

    return FAISS.from_documents(tool_docs, embed_model)
