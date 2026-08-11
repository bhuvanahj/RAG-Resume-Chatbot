from loaders.pdf_loader import PDFLoader
from services.vector_db import VectorDB

docs = PDFLoader.load_pdf(r"C:\RAG\data\KIT-CSE-BhuvanaShree-HJ-2027.pdf")
print("PDF Pages:", len(docs))

if docs:
    print(docs[0].page_content[:300])

create_vectorstore(docs)

db = VectorDB.create(docs)

print("Database Created Successfully")