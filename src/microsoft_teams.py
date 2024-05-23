# src/microsoft_teams.py
import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv
from rag_pipeline import RAGPipeline

load_dotenv()

app = Flask(__name__)
rag = RAGPipeline()
with open("../data/milestone_policies.txt", 'r') as file:
    texts = file.readlines()
rag.load_texts(texts)

@app.route('/teams', methods=['POST'])
def teams():
    data = request.json
    query = data['text']
    response = rag.answer_query(query)
    return jsonify({"text": response})

if __name__ == "__main__":
    app.run(port=5000)
