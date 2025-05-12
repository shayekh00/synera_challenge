import faiss
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores.faiss import FAISS
from graph_config import graph
from langchain_community.docstore.in_memory import InMemoryDocstore


def initialize_vector_store() -> FAISS:
    embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    dim = len(embedding_model.embed_query("test"))

    index = faiss.IndexFlatL2(dim)
    docstore = InMemoryDocstore()
    index_to_docstore_id = {}

    vector_store = FAISS(
        embedding_function=embedding_model.embed_query,
        index=index,
        docstore=docstore,
        index_to_docstore_id=index_to_docstore_id,
        normalize_L2=True,
    )

    return vector_store



if __name__ == "__main__":
    initial_state = {
        "user_query": "Can I use aluminum for this 80°C application?",
        "documents": ["docs/spec_sheet.pdf"],
        "short_term_buffer": [],
        "summary_memory": [],
        "vector_store": initialize_vector_store(),
        "latest_message": "",
        "memory_active": False,
    }

    result = graph.invoke(initial_state)
    print("🟢 First Run Output:")
    print(result["latest_message"])

        # Prepare for second run
    result["user_query"] = "What materials are better than aluminum for high temperatures?"
    result["documents"] = []  # Maybe no new docs
    result["latest_message"] = ""  # Reset message field

    # Second run
    result2 = graph.invoke(result)
    print("🟡 Second Run Output (using memory):")
    print(result2["latest_message"])
