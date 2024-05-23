# src/rag_pipeline.py
from transformers import pipeline
from vector_database import VectorDatabase


class RAGPipeline:
    def __init__(self):
        self.db = VectorDatabase()
        self.generator = pipeline('text-generation', model='gpt-4')

    def load_texts(self, texts):
        self.db.add_texts(texts)

    def answer_query(self, query):
        relevant_texts = self.db.search(query)
        context = " ".join([text for text, _ in relevant_texts])
        return self.generator(query + context, max_length=150)


if __name__ == "__main__":
    rag = RAGPipeline()
    with open("../data/milestone_policies.txt", 'r') as file:
        texts = file.readlines()
    rag.load_texts(texts)
    print(rag.answer_query("What is the company's leave policy?"))
