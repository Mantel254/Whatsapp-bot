from flask import Flask, request, jsonify
from twilio.twiml.messaging_response import MessagingResponse
import os
from bot.bot_logic import process_message
from config import TWILIO_PHONE_NUMBER

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"


# Twilio Webhook Route
@app.route("/webhook", methods=["GET","POST"])
def webhook():
    """Handles incoming messages from WhatsApp via Twilio."""
    # Get the message from the incoming request
    incoming_msg = request.form.get('Body', '').strip()
    sender = request.form.get('From', '').strip()

    # incoming_msg="Who is the Governor of Mombasa kenya?"
    # sender="whatsapp:+254727683579"


    # Ignore group messages by checking if "g.us" (typically found in group messages) is in the sender's ID
    if "g.us" in sender:
        return str(MessagingResponse())  # Return an empty response for group messages

    # Process the incoming message
    response_msg = process_message(incoming_msg)
    print(response_msg)
    # Create the Twilio response
    response = MessagingResponse()
    response.message(response_msg)

    return str(response)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
