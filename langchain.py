import openai

# OpenAI API key setup
openai.api_key = 'your_openai_api_key_here'

# Define company-specific policies
company_policies = {
    "vacation policy": "Milestones provides 20 days of paid vacation per year.",
    "remote work policy": "Remote work is available under certain conditions, depending on team and project needs.",
    "sick leave policy": "Employees are entitled to 10 paid sick days per year."
}

def ask_gpt4(question, company_name="Milestones"):
    """
    This function uses GPT-4 to answer questions that are not directly related to the predefined policies.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Ensure you use the correct model name
            messages=[
                {"role": "system", "content": "You are a knowledgeable HR assistant."},
                {"role": "user", "content": f"{question}"}
            ],
            max_tokens=150
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return str(e)

def handle_query(query):
    """
    This function first checks if the query matches a predefined company policy. If it does, it returns that.
    If not, it forwards the query to GPT-4.
    """
    query = query.lower()
    for key in company_policies:
        if key in query:
            return company_policies[key]
    return ask_gpt4(query, "Milestones")

# Example usage
if __name__ == "__main__":
    user_queries = [
        "What is the vacation policy?",
        "Can you tell me about remote work benefits?",
        "How do I install VPN on my machine?"
    ]

    for query in user_queries:
        print("Question:", query)
        print("Answer:", handle_query(query))
        print()