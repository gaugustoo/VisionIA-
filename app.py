from flask import Flask, render_template, request
from twilio.twiml.messaging_response import MessagingResponse
import openai

app = Flask(__name__)
openai.api_key = "SUA_CHAVE_API"  # Substitua pela sua chave da OpenAI

def get_ai_response(user_input):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_input}]
    )
    return response.choices[0].message["content"]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.form["mensagem"]
    response = get_ai_response(user_input)
    return response

@app.route("/whatsapp", methods=["POST"])
def whatsapp_chat():
    user_input = request.form["Body"]
    response_text = get_ai_response(user_input)

    resp = MessagingResponse()
    resp.message(response_text)
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True){{