# agents/context_loader.py

from pathlib import Path
from langchain_core.documents import Document
from agent_state import AgentState
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
# Text & tabular loaders
from langchain_community.document_loaders import (
    PyPDFLoader,
    CSVLoader,
    UnstructuredWordDocumentLoader,
    UnstructuredExcelLoader,
    UnstructuredFileLoader,
)

# OCR for images
from PIL import Image
import pytesseract


# Define loaders per file type
def load_pdf(path): return PyPDFLoader(path).load()
def load_csv(path): return CSVLoader(path).load()
def load_docx(path): return UnstructuredWordDocumentLoader(path).load()
def load_xlsx(path): return UnstructuredExcelLoader(path).load()
def load_generic(path): return UnstructuredFileLoader(path).load()


# Image handler
def load_image_as_text(path):
    try:
        text = pytesseract.image_to_string(Image.open(path))
        return [Document(page_content=text, metadata={"source": path})]
    except Exception as e:
        print(f"⚠️ OCR failed for {path}: {e}")
        return []

# File extension map
loader_map = {
    ".pdf": load_pdf,
    ".csv": load_csv,
    ".docx": load_docx,
    ".xlsx": load_xlsx,
    ".txt": load_generic,
    ".md": load_generic,
    ".pptx": load_generic,
    ".png": load_image_as_text,
    ".jpg": load_image_as_text,
    ".jpeg": load_image_as_text,
}

def load_documents(state: AgentState) -> AgentState:
    docs = []
    for path in state["documents"]:
        ext = Path(path).suffix.lower()
        loader = loader_map.get(ext)
        if not loader:
            raise ValueError(f"❌ Unsupported file type: {ext}")
        docs.extend(loader(path))

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(docs)

    embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    db = FAISS.from_documents(chunks, embedding_model)

    return {**state, "vectorstore": db}
