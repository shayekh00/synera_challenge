from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEmbeddings

# Example past workflows (you can replace this with dynamic ingestion later)
WORKFLOWS = [
        {
            "description": "Add 3 to all odd numbers in a list",
            "steps": """number_slider = synera.number_slider(0, 5, 10)\r\ntree = synera.graft_tree(number_slider)\r\nitem_b = synera.panel(\"2\")\r\nresult = synera.modulus(tree, item_b)\r\nlist_a, list_b = synera.dispatch(tree, result)\r\nitem_a = synera.panel(\"3\")\r\nresult_1 = synera.addition(item_a, list_a)\r\nlist, indices = synera.combine(result_1, list_b)\r\ntree_1 = synera.flatten_tree(list, default)\r\noutput = synera.integer(tree_1)\r\n"""
        },
        {
            "description": "Double all even numbers in a list",
            "steps": """tree = graft_tree(input_list)
                        mask = modulus(tree, 2)
                        odds, evens = dispatch(tree, mask)
                        doubled_evens = addition(evens, evens)
                        combined = combine(odds, doubled_evens)
                        output = flatten_tree(combined)"""
        },
]


def format_workflow(flow: dict) -> str:
    return flow["steps"]  



def initialize_workflow_store() -> FAISS:
    embed_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    workflow_docs = [
        Document(page_content=format_workflow(flow))
        for flow in WORKFLOWS
    ]

    return FAISS.from_documents(workflow_docs, embed_model)
