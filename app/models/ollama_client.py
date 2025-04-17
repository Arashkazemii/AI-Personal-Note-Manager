from ollama import chat
# This is a simple client for the Ollama API
class ollamaClient():
    def __init__(self, model_name: str):
        self.model_name = model_name
    # This function sends a message to the model and returns the response
    def chat_respond(self, messages: list, stream: bool = False):
        return chat(
            model=self.model_name,
            messages=messages,
            stream=stream,
        )

# Example usage:
# ollama = ollamaClient("llama3.1:8b")
# respond = ollama.chat_respond(messages=[{'role': 'user', 'content': 'Why is the sky blue?'}], stream=False)
# print(respond)