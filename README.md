# ChatGPT Terminal Bot

A simple, command-line chatbot that uses the OpenAI API (`gpt-3.5-turbo`) to provide conversational AI directly in your terminal. This script maintains conversation history for context-aware responses.



## Features

- **Interactive Chat:** Have a real-time conversation with ChatGPT from your terminal.
- **Context-Aware:** The bot remembers the previous turns in the conversation to provide relevant answers.
- **Simple & Minimal:** A single Python file with minimal dependencies.
- **Easy to Configure:** Just add your OpenAI API key to get started.
- **Error Handling:** Basic error handling for API connection issues.

## Prerequisites

- Python 3.7+
- An OpenAI account and a valid API key. You can get one from the [OpenAI Platform](https://platform.openai.com/api-keys).

## Installation & Setup

Follow these steps to get the chatbot running on your local machine.

### 1. Save the Code

Save the Python code into a file named `chat_bot.py`.

### 2. Install Dependencies

You only need the `openai` library. You can install it using pip:

```bash
pip install openai
```

### 3. Configure Your API Key

You must provide your OpenAI API key for the script to work. There are two ways to do this:

#### Option 1: Hardcode the Key (Simple but not recommended)

Open the `chat_bot.py` file and replace `"sk-YourAPI"` with your actual OpenAI API key.

```python
# Paste your key here or set it via env variable
openai.api_key = "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" # <--- PASTE YOUR KEY HERE
```

**Warning:** Hardcoding keys is a security risk. Do not commit this file to a public repository (like GitHub) with your key inside it.

#### Option 2: Use an Environment Variable (Recommended & More Secure)

This method keeps your API key separate from the code.

1.  **Set the Environment Variable:**

    *   **On macOS/Linux:**
        ```bash
        export OPENAI_API_KEY="sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
        ```
        To make this permanent, add the line to your shell profile file (e.g., `~/.zshrc`, `~/.bashrc`).

    *   **On Windows (Command Prompt):**
        ```cmd
        set OPENAI_API_KEY="sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
        ```

    *   **On Windows (PowerShell):**
        ```powershell
        $env:OPENAI_API_KEY="sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
        ```

2.  **Modify the Python Script:**
    Update the script to read the key from the environment variable. Replace the original API key line with this:

    ```python
    import openai
    import os # <-- Add this import

    # Set the API key from an environment variable
    openai.api_key = os.getenv("OPENAI_API_KEY")

    if not openai.api_key:
        raise ValueError("OpenAI API key not found. Please set the OPENAI_API_KEY environment variable.")
    ```

## How to Use

1.  Open your terminal or command prompt.
2.  Navigate to the directory where you saved `chat_bot.py`.
3.  Run the script:

    ```bash
    python chat_bot.py
    ```

4.  You will see a prompt. Start typing your questions and press Enter.

    ```
    🤖 ChatGPT Terminal Bot
    Type 'exit' to quit.
    🧑 You: Hello! Can you explain what a Large Language Model is in simple terms?
    🤖 GPT: Of course! Imagine a very, very well-read person who has read almost every book and article on the internet. A Large Language Model (LLM) is like that person's brain, but in a computer. It learns patterns, grammar, facts, and reasoning skills from all that text. When you ask it a question, it uses what it learned to predict the most likely sequence of words to form a helpful and coherent answer.
    🧑 You: What are some famous examples?
    🤖 GPT: Some of the most well-known examples of Large Language Models include OpenAI's GPT series (like GPT-3.5 and GPT-4), Google's LaMDA and PaLM, and Meta's LLaMA. These models power many popular chatbots and AI applications you might see today.
    🧑 You: exit
    👋 Goodbye!
    ```

## Code Breakdown

### `chat_with_gpt(message, history)`

-   This function is the core of the chatbot.
-   It takes the user's `message` and the ongoing `history` of the conversation.
-   It appends the new user message to the history.
-   It sends a request to the OpenAI `chat.completions.create` endpoint using the `gpt-3.5-turbo` model.
-   The `messages` payload includes a system prompt (`"You are a helpful assistant."`) and the entire conversation history, which gives the model context.
-   It parses the response, extracts the reply text, and adds it to the history.
-   Finally, it returns the `reply` and the updated `history`.

### `main()`

-   This function serves as the main application loop.
-   It initializes an empty `chat_history` list.
-   It enters a `while True` loop to continuously prompt the user for input.
-   If the user types `exit`, the loop breaks and the program terminates.
-   For any other input, it calls `chat_with_gpt`, prints the model's response, and updates the history for the next turn.

### `if __name__ == "__main__":`

-   This is standard Python practice. It ensures that the `main()` function is called only when the script is executed directly (not when imported as a module).
