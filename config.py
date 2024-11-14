import os

# Set the OpenAI API key (can be stored in .env file)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "your-openai-api-key")
print(OPENAI_API_KEY)
# Set the Twilio phone number (can be stored in .env file)
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER", "your-twilio-phone-number")
