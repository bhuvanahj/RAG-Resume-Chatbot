from loaders.pdf_loader import PDFLoader
from vectorstore.vector_store import create_vectorstore

def initialize_database():

    print("INITIALIZE DATABASE CALLED")

    docs = PDFLoader.load_pdf(
        r"data\KIT-CSE-BhuvanaShree-HJ-2027.pdf"
    )

    print("PDF Pages:", len(docs))

    create_vectorstore(docs)

    print("VECTORSTORE CREATED")