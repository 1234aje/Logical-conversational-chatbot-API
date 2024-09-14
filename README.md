# LangChain Integration System
This repository provides a system that integrates with LangChain, leveraging LLMs (Large Language Models) for enhanced reasoning and decision-making. The system operates statelessly, ensuring each request is processed independently, and the user state isn't stored between interactions.

## Features
- **Stateless Operation**: The system doesn't retain session information, making each interaction unique and lightweight.
- **LangChain Integration**: Uses LangChain's capabilities to manage complex chains of operations, improving the reasoning capabilities of the LLM.
- **API-Based Architecture**: Exposes multiple API endpoints for seamless integration with external systems.

# Table of Contents
- Prerequisites
- Installation
- Environment Setup
- API Documentation

# Prerequisites
Ensure you have the following installed before proceeding:

- Python 3.7+
- pip (Python package manager)
  
Additionally, you will need API keys for:

- OpenAI for LLM integration.

# Installation
### Clone the repository:


```bash
Copy code
git clone https://github.com/1234aje/Logical-conversational-chatbot-API.git
cd Logical-conversational-chatbot-API
```
### Install dependencies:

```bash
Copy code
pip install -r requirement.txt
```
**Verify installations** : Ensure the following dependencies are installed:

- LangChain
- OpenAI
- FastAPI
- Uvicorn
- Python-dotenv
  
These can be found in the ``` requirement.txt```: 

# API Documentation
The system provides a set of API endpoints to interact with the LangChain framework. Each endpoint is stateless, meaning that no user session information is preserved between requests.

1. ```/ask``` - **Interact with the LLM**
**Description**: This endpoint allows you to send a query to the LLM integrated with LangChain, which processes the request and returns the response.

- **Method**: ```POST```
- **Endpoint**: ```/ask```
## Request Body
```prompt``` (string): The input question for the LLM.
