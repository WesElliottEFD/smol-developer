# Smol-Developer Integration with BloopAI's Code Understanding

Welcome to the Smol-Developer project's integration with BloopAI's advanced code understanding and processing features, utilizing GPT-4-turbo for enhanced code generation and adaptation to existing codebases.

## Getting Started

### Prerequisites

Before you begin, ensure you have Python 3.8 or higher installed on your system. You can download Python from the official website: https://www.python.org/downloads/

### Installation

To set up your environment for Smol-Developer with BloopAI integration, you need to install the following libraries:

```bash
pip install openai ast tiktoken
```

If you plan to use cloud functions with the `modal` library, please ensure it is also installed and configured according to the Smol-Developer documentation.

## Usage

### Agent Class

The `Agent` class is the core of the integration, handling user queries and managing file processing. It is implemented in `agent.py`. To use it in your project, import the `Agent` class in your `main.py` and `debugger.py` files.

### Language Model Integration

The OpenAI model references have been updated to GPT-4-turbo. You can find the updated configurations in `main.py`, `main_no_modal.py`, `debugger.py`, and `debugger_no_modal.py`.

### Semantic Embedding

Semantic embeddings are created using the `embedder.py` file. This process uses NLP techniques to analyze the codebase and enhance the AI's understanding of the existing code.

### Semantic Query Execution

To execute semantic queries, use the `execute.py` file. This will transform user queries into AI responses, using the semantic context provided by the embeddings.

### Query Processing

For query processing, refer to `compiler.py` and `execute.py`. These files compile and execute queries, utilizing regex and text processing.

### Language-Specific Processing

For TypeScript and Python, use `language_typescript.py` and `language_python.py` respectively. These files are tailored to handle the syntax and semantics of the specific programming languages.

### Feature Integration

The integration can be toggled on or off using an environment variable or a configuration file. To enable or disable the feature, set the `TOGGLE_FEATURE_ENV` environment variable or modify the `config.json` file accordingly.

## Documentation

For more detailed instructions on how to use the new features, please refer to the documentation within each file. The `readme.md` file will be regularly updated to reflect the latest usage guidelines.

## Contributing

If you wish to contribute to the project or suggest improvements, please review the guidelines in the `CONTRIBUTING.md` file and submit your pull requests.

## License

This project is licensed under the MIT License - see the `LICENSE.md` file for details.

## Acknowledgments

- BloopAI for providing the advanced code understanding features.
- OpenAI for the GPT-4-turbo model.

For further review of BloopAI's features, visit their repository: https://github.com/BloopAI/bloop.git

Happy coding!