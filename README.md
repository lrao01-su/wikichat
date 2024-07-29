# WikiChat Bot

WikiChat Bot is an interactive chatbot that demonstrates the power of Retrieval Augmented Generation (RAG) using OpenAI, LlamaIndex, and Chainlit. This project showcases how to enhance large language model (LLM) applications by developing an LLM-powered conversational assistant with access to Wikipedia content.

## Project Overview

This bot allows users to query Wikipedia content using natural language, dynamically indexing chosen Wikipedia pages to provide informed responses. By combining the strengths of OpenAI's language models, LlamaIndex's efficient retrieval capabilities, and Chainlit's interactive interface, WikiChat Bot offers a sophisticated example of how to augment LLMs with external knowledge sources.

## Features

- Dynamic Wikipedia page indexing based on user requests
- Retrieval Augmented Generation (RAG) for enhanced LLM responses
- Real-time chat interface using Chainlit
- Integration with OpenAI's GPT models
- Vector-based search using LlamaIndex
- Customizable settings for model selection and Wikipedia page requests

## Technologies Used

- Python
- OpenAI API
- LlamaIndex
- Chainlit
- Pydantic
- Wikipedia API

## How It Works

1. **Wikipedia Indexing**: The bot dynamically indexes specified Wikipedia pages.
2. **Vector Search**: LlamaIndex creates a vector store for efficient content retrieval.
3. **Natural Language Processing**: OpenAI's GPT models process and respond to user queries.
4. **Retrieval Augmented Generation**: The system augments LLM responses with relevant information from the indexed Wikipedia content.
5. **Interactive Chat Interface**: Chainlit provides a smooth, real-time user experience.

## Key Components

- `index_wikipages.py`: Handles Wikipedia page indexing and vector store creation.
- `chat_agent.py`: Manages the chat interface and integrates the various components.

## Learning Outcomes

This project provided hands-on experience with:

- Building and deploying AI-powered chatbots
- Working with large language models and the OpenAI API
- Implementing vector search capabilities using LlamaIndex
- Creating interactive web interfaces with Chainlit
- Handling asynchronous operations in Python
- Error handling and logging in production-like environments

## Future Improvements

- Implement caching to improve response times
- Add support for multi-language Wikipedia pages
- Enhance error handling and user feedback
- Implement user authentication and session management

## References

This project was developed with guidance and references from (Founder of Data Centric) the LlamaIndex documentation and component guides. Key references include:

1. LlamaIndex Documentation: [https://gpt-index.readthedocs.io/en/latest/](https://gpt-index.readthedocs.io/en/latest/)
2. LlamaIndex Components Guide: [https://gpt-index.readthedocs.io/en/latest/core_modules/data_modules/index/index.html](https://gpt-index.readthedocs.io/en/latest/core_modules/data_modules/index/index.html)
3. LlamaIndex Query Engine Guide: [https://gpt-index.readthedocs.io/en/latest/core_modules/query_modules/query_engine/root.html](https://gpt-index.readthedocs.io/en/latest/core_modules/query_modules/query_engine/root.html)
4. LlamaIndex Agent Guide: [https://gpt-index.readthedocs.io/en/latest/core_modules/agent_modules/agents/root.html](https://gpt-index.readthedocs.io/en/latest/core_modules/agent_modules/agents/root.html)