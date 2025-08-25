import streamlit as st
from groq import Groq
from datetime import datetime
import re

st.set_page_config(
    page_title="DeepSeek R1 CHatbot",
    layout="centered"
)

with st.sidebar:
    st.title("Chatbot Settings")
    api_key = st.text_input("Groq API Key", type="password")
    # API_KEY = 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
    st.markdown("[Get Groq API KEY](https://console.groq.com/keys)")

    temperature = st.slider("Temperature", 0.0, 1.0, 0.7)
    max_tokens = st.slider("Maximum Tokens", 100, 4096, 1024)
    top_p = st.slider("Top-P", 0.0, 1.0, 1.0)
    frequency_penality = st.slider("Frequency Penality", 0.0, 1.0, 0.0)

st.title("DeepSeek R1 ChatBot")
st.caption("Powered by Groq")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    avatar = "👤" if message["role"] == "user" else "🤖"
    with st.chat_message(message["role"], avatar=avatar):
        st.markdown(message["content"])
        st.caption(f"_{message["timestamp"]}_")

if prompt := st.chat_input("How can I help You?"):
    if not api_key:
        st.info("Please Enter Groq API Key to Continue")
        st.stop()
    
    timestamp = datetime.now().strftime("%H:%M:%S")
    st.session_state.messages.append({
        "role": "user",
        "content": prompt,
        "timestamp": timestamp
    })

    with st.chat_message("user", avatar="👤"):
        st.markdown(prompt)
        st.caption(f"_{timestamp}_")
    
    try:
        client=Groq(api_key=api_key)
        response = client.chat.completions.create(
            model= "deepseek-r1-distill-llama-70b",
            messages=[{"role":m["role"],"content":m["content"]} for m in st.session_state.messages],
            temperature=temperature,
            max_tokens=max_tokens,
            top_p=top_p,
            frequency_penalty=frequency_penality,
            stream=False
        )

        ai_response=response.choices[0].message.content
        ai_response = re.sub(r"<think>.*?</think>", "", ai_response, flags=re.DOTALL).strip()
        timestamp=datetime.now().strftime("%H:%M:%S")

        st.session_state.messages.append({
            "role":"assistant",
            "content":ai_response,
            "timestamp":timestamp
        })

        with st.chat_message("assistant",avatar="🤖"):
            st.markdown(ai_response)
            st.caption(f"_{timestamp}_")

    except Exception as e:
        st.error(f"Error gnenrating response:{str(e)}")

if st.sidebar.button("Clear Chat"):
    st.session_state.messages=[]
    st.rerun()
