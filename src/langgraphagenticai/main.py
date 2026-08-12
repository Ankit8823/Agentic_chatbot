import streamlit as st
from src.langgraphagenticai.ui.streamlitui.loadui import LoadStreamlitUI

def load_langgraph_agenticai_app():
    """

    Loads and runs the langgraph agentticai applications with streamlit ui.
    this functions initializas the ui ,handles user input ,configures the llm model,
    sets up the graph based on the selected use case ,and displays the output while
    implementing exception handling for robustness.
    """
    ##load ui
    ui=LoadStreamlitUI()
    user_input=ui.load_streamlit_ui()

    if not user_input:
        st.error("Error: failed to load user input from the UI")
        return 
    user_message=st.chat_input("Enter your message")

     