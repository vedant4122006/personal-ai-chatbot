import google.generativeai as genai
import os
from dotenv import load_dotenv
import gradio as gr

load_dotenv()
google_api_key = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=google_api_key)

model = genai.GenerativeModel("gemini-1.5-flash")

print("🤖 Gemini AI Chatbot Activated! Type 'exit' to quit.\n")

def chat_fn(message):
    response = model.generate_content(message)
    return response.text


gr.Interface(fn=chat_fn, inputs="text", outputs="text", title="My Personal AI Agent").launch()












'''while True:
    user_input = input("👤 You: ")

    if user_input.lower() in ['exit', 'quit']:
        print("🤖 Gemini: Chat ended. Goodbye!")
        break

    try:
        response = model.generate_content(user_input)
        print("🤖 Gemini:", response.text, "\n")
    except Exception as e:
        print("⚠️ Error:", e, "\n")'''

