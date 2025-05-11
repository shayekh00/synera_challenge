# Utility functions for document loaders

def load_document(file_path):
    """
    Load a document from the given file path.
    
    Args:
        file_path (str): The path to the document file.
        
    Returns:
        str: The content of the document.
    """
    with open(file_path, 'r') as file:
        return file.read()

def save_document(file_path, content):
    """
    Save the given content to a document at the specified file path.
    
    Args:
        file_path (str): The path to the document file.
        content (str): The content to be saved.
    """
    with open(file_path, 'w') as file:
        file.write(content)