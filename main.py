import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Configure Gemini
genai.configure(api_key=api_key)

# Load Gemini Pro model
model = genai.GenerativeModel("gemini-pro")

# Take input from user
user_input = input("👤 You: ")

# Get response from Gemini
response = model.generate_content(user_input)

print("\n🤖 Gemini: ", response.text)
