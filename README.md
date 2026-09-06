# Agentic Chatbot

An agentic AI chatbot built with LangGraph, LangChain, Groq, Tavily, and Streamlit.

The application supports basic conversations, web-powered answers, and AI news summarization through separate stateful LangGraph workflows.

## Features

- Basic chatbot conversation
- Web search using Tavily
- AI news retrieval and summarization
- Multiple Groq models
- Stateful graph-based workflow using LangGraph
- Streamlit user interface
- Markdown export for AI news summaries

## Available Use Cases

### Basic Chatbot

Chat with an AI assistant using a Groq language model.

### Chatbot With Web

Ask questions that require current information. The chatbot can use Tavily web search to find relevant results before generating an answer.

### AI News

Select a time frame to fetch and summarize recent artificial intelligence news:

- Daily
- Weekly
- Monthly

The generated summary is saved as a Markdown file in the `AINews` folder.

## Project Structure

```text
Agentic_chatbot/
├── app.py
├── requirements.txt
├── README.md
└── src/
    └── langgraphagenticai/
        ├── graph/
        │   └── graph_builder.py
        ├── LLM/
        │   └── groqllm.py
        ├── nodes/
        │   ├── basic_chatbot_node.py
        │   ├── chatbot_with_tools_node.py
        │   └── ai_news_node.py
        ├── state/
        │   └── state.py
        ├── tools/
        │   └── search_tool.py
        └── ui/
            └── streamlitui/
