from flask import Flask, request, jsonify, render_template
import os

app = Flask(__name__)

# Load or initialize your AI/ML models here if needed
# Example: from chatbot import respond_to_query

@app.route('/')
def home():
    # Return the main interface (if it exists in templates/)
    return render_template('index.html')

@app.route('/api/query', methods=['POST'])
def handle_query():
    user_query = request.json.get('query', '')
    # Placeholder for real NLP response
    bot_response = "This is a test response. Replace with model logic."
    # If you have a function like respond_to_query(user_query), use it here
    # bot_response = respond_to_query(user_query)
    return jsonify({'response': bot_response})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
