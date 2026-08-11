from langchain_chroma import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter

from config import DB_DIRECTORY
from embeddings.embedding import get_embedding


def create_vectorstore(documents):

    print("Documents received:", len(documents))

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_documents(documents)

    print("Chunks:", len(chunks))

    vector_db = Chroma.from_documents(
        documents=chunks,
        embedding=get_embedding(),
        persist_directory=DB_DIRECTORY
    )

    print("Stored:", vector_db._collection.count())

    return vector_db


def load_vectorstore():

    return Chroma(
        persist_directory=DB_DIRECTORY,
        embedding_function=get_embedding()
    )