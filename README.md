# DeepSeek R1 Chatbot (Powered by Groq)

A simple **Streamlit-based chatbot UI** that connects to **Groq's API** and runs the **DeepSeek-R1 Distill LLaMA-70B** model.  
This app provides an interactive chat interface with configurable parameters such as temperature, max tokens, top-p, and frequency penalty.

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/deepseek-groq-chatbot.git
   cd deepseek-groq-chatbot
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```
3. Install dependencies:
   ```
   pip install streamlit
   pip install groq
   ```

## Configuration:

1. Get your Groq API Key here:
   ```
   [Get your API Key](https://console.groq.com/keys)
   ```
2. Run the app:
   ```
   streamlit run main.py
   ```
3. In the sidebar:

   - Paste your Groq API key
   - Adjust parameters as needed
   - Start chatting
   - 
