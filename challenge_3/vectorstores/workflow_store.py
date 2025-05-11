from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEmbeddings

# Example past workflows (you can replace this with dynamic ingestion later)
WORKFLOWS = [
    {
        "description": "Add 3 to all odd numbers in a list",
        "steps": """number_slider = number_slider(0, 5, 10)
tree = graft_tree(number_slider)
item_b = panel("2")
result = modulus(tree, item_b)
list_a, list_b = dispatch(tree, result)
item_a = panel("3")
result_1 = addition(item_a, list_a)
list = combine(result_1, list_b)
tree_1 = flatten_tree(list)
output = integer(tree_1)"""
    },
    {
        "description": "Double all even numbers in a list",
        "steps": """input_list = number_slider(0, 5, 10)
tree = graft_tree(input_list)
even_mask = modulus(tree, 2)
odds, evens = dispatch(tree, even_mask)
doubled_evens = addition(evens, evens)
combined = combine(odds, doubled_evens)
output = flatten_tree(combined)"""
    },
]


def format_workflow(flow: dict) -> str:
    return f"# {flow['description']}\n{flow['steps']}"


def initialize_workflow_store() -> FAISS:
    embed_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    workflow_docs = [
        Document(page_content=format_workflow(flow))
        for flow in WORKFLOWS
    ]

    return FAISS.from_documents(workflow_docs, embed_model)
