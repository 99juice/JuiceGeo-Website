from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/whatsapp", methods=["POST"])
def whatsapp_reply():
    incoming_msg = request.values.get('Body', '').lower()
    response = MessagingResponse()
    reply = response.message()

    if "hi" in incoming_msg:
        reply.body("Hey! How can I help you today? 😊")
    elif "songs" in incoming_msg:
        reply.body("Here’s a playlist of Juice WRLD songs: https://99juice.github.io/JuiceGeo-Website/")
    elif "bye" in incoming_msg:
        reply.body("Goodbye! Hope to chat again soon! 👋")
    else:
        reply.body("I'm JuiceGeo’s bot! Ask me about Juice WRLD, songs, or anything else. 🔥")

    return str(response)

if __name__ == "__main__":
    app.run(debug=True)
