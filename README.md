# 💬 Personal AI Chatbot using Google Gemini API

Welcome to the **Personal AI Chatbot** project! This repository contains a complete beginner-friendly implementation of a personal AI assistant using **Python**, **Gradio** for frontend UI, and **Google Gemini Pro API** for generating intelligent AI responses. This chatbot runs on your local machine and provides a clean, interactive interface to have conversations with an AI agent, making it a perfect project for learning how to connect frontend applications with powerful AI models using APIs.

---

## ✨ Project Overview

This project demonstrates:
- ✅ How to build a **simple AI chatbot**
- ✅ How to integrate **Google Gemini API** for AI responses
- ✅ How to create a **web-based chat UI** using Gradio
- ✅ How to manage API keys securely using `.env` files
- ✅ How to run a Python project with minimum setup and maximum functionality

It is designed to be:
- 🔵 **Beginner-friendly** — no advanced coding knowledge required
- 🟣 **Fast to set up** — just install dependencies and run
- 🟢 **Educational** — shows practical integration of Google AI services
- 🟡 **Customizable** — you can modify prompts and UI easily

---

## 🗂️ Project Folder Structure

Below is the simple and organized structure of the project repository:

personal-ai-chatbot/
│
├── main.py # Main Python file containing chatbot logic
├── requirements.txt # List of Python dependencies for the project
└── .env # API key file (not included in repo for security reasons)


---

## 🛠️ Technologies and Tools Used

- **Python 3** — main programming language
- **Gradio** — for creating the simple web interface to chat with the AI
- **Google Gemini Pro API** — provides the AI-powered responses
- **dotenv** — for secure handling of sensitive API keys
- **GitHub** — for version control and open-source hosting

---

## 📌 Prerequisites

Before you get started, make sure you have the following:
- ✅ Python 3 installed on your system
- ✅ Google API access and API key for Gemini Pro
- ✅ Basic knowledge of running Python scripts (helpful but not necessary)
- ✅ Git installed for cloning the repository (optional)

---

## 🚀 Getting Started

Here is a step-by-step guide to set up and run your own personal AI chatbot on your machine.

### Step 1: Clone the Repository
Open your terminal or command prompt and run:
git clone https://github.com/vedant4122006/personal-ai-chatbot.git
cd personal-ai-chatbot


### Step 2: Install Required Python Packages
Make sure you have `pip` installed. Then run the following command to install all dependencies:
pip install -r requirements.txt

### Step 3: Configure Google Gemini API Key
Since we are using Google Gemini API, you need to authenticate with your own API key:
- Create a `.env` file in the root directory of the project.
- Inside the `.env` file, paste your Google API key like this:
GOOGLE_API_KEY=your_actual_google_api_key_here

> **Note:** Never share your `.env` file publicly. It contains your private API key.

### Step 4: Run the Application
After completing the setup, you can run the chatbot using:
python main.py


This will start a **Gradio web application**, and you will see a link in the terminal, usually like `http://127.0.0.1:7860`. Open this link in your browser and start chatting with your AI Assistant.

---

## 🎉 Features Explained in Detail

- 📝 **Simple Web Interface**: The project uses Gradio to give a minimalistic chat window where you can enter messages and get AI responses in real-time.

- 🤖 **AI-Powered Responses**: By leveraging Google Gemini Pro API, you get access to a powerful conversational AI model capable of answering questions, generating responses, and assisting in various tasks.

- 🔐 **Secure API Handling**: API keys are handled using the `.env` file and `dotenv` library, ensuring your sensitive data remains secure.

- 🧹 **Clean Code Structure**: The project follows a simple Python structure with proper file separation making it easy to understand, modify, or expand further.

---

## 📸 Example Output

When you run the project, your chat interface will look like this:
👤 You: Hello, how are you?
🤖 AI: I'm doing great! How can I assist you today?

---

## 💡 Possible Extensions

Here are a few ways you can extend this project:
- Add voice input using Gradio’s audio components.
- Customize the prompt to make it act like a tutor, advisor, or assistant.
- Deploy the chatbot online using platforms like Render or Heroku.
- Style the UI with custom CSS or themes.

---


## 📃 License

This project is released under the **MIT License**. You are free to use, modify, and distribute it for educational and personal projects.

---

## 📞 Support

If you face any issues, feel free to:
- Open an issue on the [GitHub repository](https://github.com/vedant4122006/personal-ai-chatbot.git)
- Star the repo if you found it useful ⭐

---

## 💬 Final Words

This project is a great way to learn about practical AI integrations. Feel free to explore, modify, and make it your own. Have fun chatting with your AI Assistant! 🚀

