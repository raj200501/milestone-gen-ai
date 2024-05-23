# src/app.py
from flask import Flask, request, jsonify, render_template
from chatbot import Chatbot

app = Flask(__name__)
bot = Chatbot()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/query', methods=['POST'])
def query():
    data = request.json
    query = data.get('text', '')
    response = bot.get_response(query)
    return jsonify(response)

@app.route('/chat', methods=['POST'])
def chat():
    query = request.form['query']
    response = bot.get_response(query)
    return render_template('index.html', query=query, response=response[0][0])

if __name__ == "__main__":
    app.run(debug=True)
