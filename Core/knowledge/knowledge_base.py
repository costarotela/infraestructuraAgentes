from llama_index import GPTVectorStoreIndex, Document
from llama_index.readers.schema.base import Document

class KnowledgeBase:
    def __init__(self):
        self.index = None
        self.documents = []
    
    def load_data(self, documents_path: str):
        documents = SimpleDirectoryReader(documents_path).load_data()
        self.index = GPTVectorStoreIndex.from_documents(documents)
    
    def query(self, question: str) -> str:
        query_engine = self.index.as_query_engine()
        return query_engine.query(question)
