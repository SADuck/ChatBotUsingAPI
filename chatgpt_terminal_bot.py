import openai
import os

# Paste your key here or set it via env variable
openai.api_key = "sk-YourAPI"

def chat_with_gpt(message, history=None):
    if history is None:
        history = []

    history.append({"role": "user", "content": message})

    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."}
            ] + history,
        )

        reply = response.choices[0].message.content.strip()
        history.append({"role": "assistant", "content": reply})
        return reply, history

    except Exception as e:
        return f"⚠️ Error: {e}", history

def main():
    print("🤖 ChatGPT Terminal Bot\nType 'exit' to quit.")
    chat_history = []

    while True:
        user_input = input("🧑 You: ")
        if user_input.lower() == "exit":
            print("👋 Goodbye!")
            break

        response, chat_history = chat_with_gpt(user_input, chat_history)
        print("🤖 GPT:", response)

if __name__ == "__main__":
    main()
