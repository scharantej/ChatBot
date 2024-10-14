
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    message = request.form['message']
    response = get_response_from_gemini(message)
    return render_template('chat.html', message=message, response=response)

def get_response_from_gemini(message):
    # Logic to send the message to the Gemini-1.5-Flash-002 server and receive the response
    # should be implemented here
    return "Hello, human."

if __name__ == '__main__':
    app.run()
