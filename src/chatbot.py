# src/chatbot.py
from rag_pipeline import RAGPipeline


class Chatbot:
    def __init__(self):
        self.rag_pipeline = RAGPipeline()
        with open("../data/milestone_policies.txt", 'r') as file:
            texts = file.readlines()
        self.rag_pipeline.load_texts(texts)

    def get_response(self, query):
        return self.rag_pipeline.answer_query(query)


if __name__ == "__main__":
    bot = Chatbot()
    query = "What is the company's leave policy?"
    response = bot.get_response(query)
    print(f"Query: {query}\nResponse: {response}")
