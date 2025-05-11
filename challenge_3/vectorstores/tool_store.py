import faiss
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEmbeddings

# Example tool registry (we'll likely load from a file/DB later)
TOOL_REGISTRY = [
    {
        "tool_name": "number_slider",
        "description": "Generates a list of numbers within a given range. Used to simulate a numeric input list.",
        "inputs": ["start", "step", "end"],
        "outputs": ["list"],
        "example_usage": "number_slider = synera.number_slider(0, 5, 10)"
    },
    {
        "tool_name": "graft_tree",
        "description": "Converts a flat list into a tree structure where each element becomes a separate branch.",
        "inputs": ["list"],
        "outputs": ["tree"],
        "example_usage": "tree = synera.graft_tree(number_slider)"
    },
    {
        "tool_name": "panel",
        "description": "Creates a constant value panel (e.g. for passing into other functions).",
        "inputs": ["value"],
        "outputs": ["panel"],
        "example_usage": 'item = synera.panel("2")'
    },
    {
        "tool_name": "modulus",
        "description": "Computes element-wise modulus between a list and an integer.",
        "inputs": ["list", "int"],
        "outputs": ["mask"],
        "example_usage": "result = synera.modulus(tree, item)"
    },
    {
        "tool_name": "dispatch",
        "description": "Splits a list into two parts based on a boolean mask.",
        "inputs": ["list", "mask"],
        "outputs": ["true_branch", "false_branch"],
        "example_usage": "list_a, list_b = synera.dispatch(tree, result)"
    },
    {
        "tool_name": "addition",
        "description": "Adds a constant or element-wise value to a list.",
        "inputs": ["list", "value_or_list"],
        "outputs": ["result"],
        "example_usage": "result = synera.addition(item_a, list_a)"
    },
    {
        "tool_name": "combine",
        "description": "Merges two branches into a unified list.",
        "inputs": ["list1", "list2"],
        "outputs": ["combined"],
        "example_usage": "list = synera.combine(result_1, list_b)"
    },
    {
        "tool_name": "flatten_tree",
        "description": "Flattens a tree structure into a single list.",
        "inputs": ["tree"],
        "outputs": ["list"],
        "example_usage": "tree_1 = synera.flatten_tree(list, default)"
    },
    {
        "tool_name": "integer",
        "description": "Casts or extracts integers from structured outputs.",
        "inputs": ["tree_or_list"],
        "outputs": ["list_of_integers"],
        "example_usage": "output = synera.integer(tree_1)"
    }
]

def format_tool(tool: dict) -> str:
    return (
        f"Tool: {tool['tool_name']}\n"
        f"Inputs: {', '.join(tool['inputs'])}\n"
        f"Outputs: {', '.join(tool['outputs'])}\n"
        f"Description: {tool['description']}\n"
        f"Example Usage: {tool['example_usage']}\n"
    )

def initialize_tool_store() -> FAISS:
    embed_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    tool_docs = [
        Document(page_content=format_tool(tool), metadata={"tool_name": tool["tool_name"]})
        for tool in TOOL_REGISTRY
    ]

    return FAISS.from_documents(tool_docs, embed_model)
