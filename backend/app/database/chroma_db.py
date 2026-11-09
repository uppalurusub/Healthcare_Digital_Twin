"""
database/chroma_db.py

Enterprise ChromaDB Manager

Features
--------
- Persistent ChromaDB
- LangChain Compatible
- Loguru Logging
- Collection Management
- Similarity Search
- Add/Delete Documents
- Metadata Search
"""

from __future__ import annotations

from typing import Any, Dict, List, Optional

from app.config.settings import settings
logger = settings.get_logger()

from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEmbeddings


class ChromaDBManager:
    """
    Enterprise Chroma Database Manager
    """

    def __init__(
        self,
        persist_directory: str,
        collection_name: str,
        embedding_model: str = "sentence-transformers/all-MiniLM-L6-v2",
    ) -> None:

        logger.info("Initializing ChromaDB Manager")

        self.persist_directory = persist_directory
        self.collection_name = collection_name
        self.embedding_model = embedding_model

        logger.info("Loading embedding model: {}", embedding_model)

        self.embeddings = HuggingFaceEmbeddings(
            model_name=embedding_model
        )

        logger.info("Connecting to ChromaDB")

        self.vectorstore = Chroma(
            collection_name=self.collection_name,
            embedding_function=self.embeddings,
            persist_directory=self.persist_directory,
        )

        logger.success(
            "Connected to Chroma Collection '{}'",
            self.collection_name,
        )

    # ==========================================================
    # Add Documents
    # ==========================================================

    def add_documents(
        self,
        documents: List[Document],
    ) -> List[str]:

        logger.info(
            "Adding {} documents",
            len(documents),
        )

        ids = self.vectorstore.add_documents(documents)

        logger.success(
            "{} documents inserted",
            len(ids),
        )

        return ids

    # ==========================================================
    # Similarity Search
    # ==========================================================

    def similarity_search(
        self,
        query: str,
        k: int = 5,
    ) -> List[Document]:

        logger.info("Similarity Search")

        logger.debug("Query : {}", query)

        docs = self.vectorstore.similarity_search(
            query=query,
            k=k,
        )

        logger.success(
            "{} documents retrieved",
            len(docs),
        )

        return docs

    # ==========================================================
    # Similarity Search with Score
    # ==========================================================

    def similarity_search_with_score(
        self,
        query: str,
        k: int = 5,
    ):

        logger.info("Similarity Search With Score")

        return self.vectorstore.similarity_search_with_score(
            query=query,
            k=k,
        )

    # ==========================================================
    # Metadata Search
    # ==========================================================

    def metadata_search(
        self,
        query: str,
        metadata_filter: Dict[str, Any],
        k: int = 5,
    ) -> List[Document]:

        logger.info("Metadata Search")

        logger.debug("Filter : {}", metadata_filter)

        return self.vectorstore.similarity_search(
            query=query,
            k=k,
            filter=metadata_filter,
        )

    # ==========================================================
    # Get Retriever
    # ==========================================================

    def as_retriever(
        self,
        search_type: str = "similarity",
        k: int = 5,
    ):

        logger.info("Creating Retriever")

        return self.vectorstore.as_retriever(
            search_type=search_type,
            search_kwargs={"k": k},
        )

    # ==========================================================
    # Delete Documents
    # ==========================================================

    def delete_documents(
        self,
        ids: List[str],
    ) -> None:

        logger.warning(
            "Deleting {} documents",
            len(ids),
        )

        self.vectorstore.delete(ids=ids)

        logger.success("Documents deleted")

    # ==========================================================
    # Delete Collection
    # ==========================================================

    def delete_collection(self):

        logger.warning(
            "Deleting collection '{}'",
            self.collection_name,
        )

        self.vectorstore.delete_collection()

        logger.success("Collection deleted")

    # ==========================================================
    # Count Documents
    # ==========================================================

    def count(self) -> int:

        collection = self.vectorstore._collection

        total = collection.count()

        logger.info(
            "Total Documents : {}",
            total,
        )

        return total

    # ==========================================================
    # Peek Documents
    # ==========================================================

    def peek(
        self,
        limit: int = 5,
    ):

        logger.info("Peeking Collection")

        return self.vectorstore._collection.peek(limit)

    # ==========================================================
    # Collection Information
    # ==========================================================

    def collection_info(self) -> Dict[str, Any]:

        collection = self.vectorstore._collection

        info = {
            "collection_name": self.collection_name,
            "documents": collection.count(),
        }

        logger.info(info)

        return info

    # ==========================================================
    # Health Check
    # ==========================================================

    def health_check(self) -> bool:

        try:

            count = self.count()

            logger.success(
                "ChromaDB Health Check Passed ({} docs)",
                count,
            )

            return True

        except Exception as ex:

            logger.exception(ex)

            return False