# pdf_loader.py

from langchain.document_loaders import PyPDFLoader

def load_pdf_documents(paths):
    all_docs = []
    for path in paths:
        loader = PyPDFLoader(path)
        docs = loader.load()
        all_docs.extend(docs)
    return all_docs
