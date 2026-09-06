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
## Technologies Used

* Python
* Streamlit
* LangChain
* LangGraph
* Groq
* Tavily Search API
* LangChain Community
* FAISS

## API Keys

The application requires a **Groq API key**.

The **Chatbot With Web** and **AI News** use cases also require a **Tavily API key**.

You can obtain keys from:

* **Groq:** https://console.groq.com/keys
* **Tavily:** https://app.tavily.com/

The application provides input fields in the Streamlit sidebar for entering the keys.

## How It Works

The application builds a different **LangGraph workflow** depending on the selected use case.

* The basic chatbot routes messages directly to the chatbot node.
* The web chatbot conditionally calls the Tavily search tool when required.
* The AI News workflow fetches news, summarizes the results, and saves the output as a Markdown file.

## Future Improvements

* Add conversation history
* Add user authentication
* Add persistent chat memory
* Add more search and productivity tools
* Improve error handling and logging
* Deploy the application online

![image alt](https://github.com/Ankit8823/Agentic_chatbot/blob/fe5bade1f413fdd5932a6b1f030393f9d87cfd92/Screenshot%20(10).png)
![image alt](https://github.com/Ankit8823/Agentic_chatbot/blob/7562dec9fe1b0b56c3759d8bdc797b2b3b330984/Screenshot%20(11).png)
![image alt](https://github.com/Ankit8823/Agentic_chatbot/blob/4ed7b76c6aea9c0fa04dd8c801de595856f68223/Screenshot%20(12).png)
![image alt](https://github.com/Ankit8823/Agentic_chatbot/blob/4ed7b76c6aea9c0fa04dd8c801de595856f68223/Screenshot%20(13).png)


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

 


