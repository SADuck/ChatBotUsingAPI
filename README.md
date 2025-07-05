# 🤖 ChatGPT Terminal Bot

A simple and clean terminal-based chatbot powered by **OpenAI GPT-3.5** using the official OpenAI API.  
Talk to ChatGPT right from your command line!

---

## 🚀 Features

- ✅ Terminal-based interface
- 🧠 Uses GPT-3.5 (ChatCompletion API)
- 📜 Maintains chat history for context-aware conversations
- 🔧 Easy to set up and run

---

## 📦 Requirements

- Python 3.7+
- OpenAI Python SDK (`openai`)

---

## 🔧 Installation

1. **Clone the repository:**
```bash
git clone https://github.com/YOUR_USERNAME/chatgpt-terminal-bot.git
cd chatgpt-terminal-bot

    Install dependencies:

pip install openai

🔐 Setup Your API Key

You need an OpenAI API key to use the chatbot.
Get it from: https://platform.openai.com/account/api-keys
Option 1: Hardcode it (for testing only)

Replace this line in chatgpt_terminal_bot.py:

openai.api_key = "sk-YourAPI"

Option 2: Use environment variable (recommended)

Set the key securely:

# For PowerShell
$env:OPENAI_API_KEY="sk-YourAPI"

In the script:

openai.api_key = os.getenv("OPENAI_API_KEY")

▶️ How to Run

python chatgpt_terminal_bot.py

Example:

🤖 ChatGPT Terminal Bot
Type 'exit' to quit.

🧑 You: Hello!
🤖 GPT: Hi there! How can I assist you today?
