```python
import openai
import re
from tiktoken import Tokenizer
from embedder import SemanticEmbedder
from agent import Agent

class QueryExecutor:
    def __init__(self, agent: Agent):
        self.agent = agent
        self.tokenizer = Tokenizer()
        self.semantic_embedder = SemanticEmbedder()

    def execute_query(self, query: str, context: str):
        """
        Transforms user queries into AI responses using semantic context.
        :param query: The user's query in natural language.
        :param context: The code context or any additional information needed for the query.
        :return: The AI's response to the query.
        """
        # Tokenize the query and context
        tokenized_query = self.tokenizer.tokenize(query)
        tokenized_context = self.tokenizer.tokenize(context)

        # Create semantic embeddings from the context
        context_embedding = self.semantic_embedder.embed_code(tokenized_context)

        # Prepare the prompt for the AI model
        prompt = self._create_prompt(tokenized_query, context_embedding)

        # Query the AI model
        response = self.agent.query_ai_model(prompt)

        # Process the response
        processed_response = self._process_response(response)

        return processed_response

    def _create_prompt(self, tokenized_query, context_embedding):
        """
        Creates a prompt for the AI model by combining the tokenized query and context embeddings.
        :param tokenized_query: The tokenized user query.
        :param context_embedding: The semantic embedding of the context.
        :return: A string prompt for the AI model.
        """
        # Combine the tokenized query with the context embedding
        prompt = f"{tokenized_query}\nContext:\n{context_embedding}\n"
        return prompt

    def _process_response(self, response):
        """
        Processes the AI model's response to extract the relevant code or information.
        :param response: The raw response from the AI model.
        :return: The processed response.
        """
        # Use regex to extract code from the response if necessary
        code_match = re.search(r'```(.*?)```', response, re.DOTALL)
        if code_match:
            return code_match.group(1).strip()
        else:
            return response

    def query_ai_model(self, prompt):
        """
        Queries the OpenAI model with the given prompt.
        :param prompt: The prompt to send to the AI model.
        :return: The response from the AI model.
        """
        try:
            response = openai.Completion.create(
                engine="gpt-4-turbo",
                prompt=prompt,
                max_tokens=150
            )
            return response.choices[0].text.strip()
        except Exception as e:
            print(f"An error occurred while querying the AI model: {e}")
            return ""

# Example usage
if __name__ == "__main__":
    agent = Agent()  # Assuming Agent class is already implemented
    executor = QueryExecutor(agent)
    user_query = "How do I implement a binary search in Python?"
    code_context = "def binary_search(array, target):"
    result = executor.execute_query(user_query, code_context)
    print(result)
```