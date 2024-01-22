```python
import openai
from tiktoken import Tokenizer

class SemanticEmbedder:
    def __init__(self, openai_api_key):
        self.tokenizer = Tokenizer()
        self.openai_api_key = openai_api_key
        openai.api_key = self.openai_api_key

    def embed_code(self, code):
        """
        Create semantic embeddings for the given code using OpenAI's Codex.

        :param code: A string containing the source code to embed.
        :return: A semantic embedding of the code.
        """
        try:
            response = openai.Embedding.create(
                input=code,
                engine="code-davinci-002",  # Assuming GPT-4-turbo is referred to as "code-davinci-002"
                user="bloop-ai-user"  # Placeholder for actual user identification if needed
            )
            return response['data']
        except openai.error.OpenAIError as e:
            print(f"An error occurred while creating embeddings: {e}")
            return None

    def tokenize_code(self, code):
        """
        Tokenize the given code using the tiktoken library.

        :param code: A string containing the source code to tokenize.
        :return: A list of tokens.
        """
        return self.tokenizer.tokenize(code)

    def process_codebase(self, codebase):
        """
        Process an entire codebase to create semantic embeddings for each file.

        :param codebase: A dictionary with filenames as keys and code strings as values.
        :return: A dictionary with filenames as keys and their semantic embeddings as values.
        """
        embeddings = {}
        for filename, code in codebase.items():
            embeddings[filename] = self.embed_code(code)
        return embeddings
```