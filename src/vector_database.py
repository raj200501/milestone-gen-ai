# src/vector_database.py
import faiss
from langchain.embeddings import SentenceTransformerEmbeddings


class VectorDatabase:
    def __init__(self, model_name='all-MiniLM-L6-v2'):
        self.model = SentenceTransformerEmbeddings(model_name)
        self.index = None
        self.texts = []

    def add_texts(self, texts):
        embeddings = self.model.encode(texts)
        if self.index is None:
            self.index = faiss.IndexFlatL2(embeddings.shape[1])
        self.index.add(embeddings)
        self.texts.extend(texts)

    def search(self, query, top_k=5):
        query_embedding = self.model.encode([query])
        D, I = self.index.search(query_embedding, top_k)
        return [(self.texts[i], D[0][i]) for i in I[0]]


if __name__ == "__main__":
    db = VectorDatabase()
    with open("../data/milestone_policies.txt", 'r') as file:
        texts = file.readlines()
    db.add_texts(texts)
    print(db.search("What is the company's leave policy?"))
