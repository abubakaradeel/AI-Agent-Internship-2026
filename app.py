from openai import OpenAI
import streamlit as st

st.title("AI Workspace")

api_key = "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"

client = OpenAI(api_key=api_key, base_url="https://api.groq.com/openai/v1")

with st.sidebar:
    model_choice = st.selectbox("Model", [
        "llama-3.3-70b-versatile",
        "llama-3.1-8b-instant",
        "gemma2-9b-it",
    ])

    system_prompt = st.text_area(
        "System Prompt",
        value="You are a helpful assistant.",
    )

    dark_mode = st.toggle("Dark Mode")

if dark_mode:
    st.markdown(
        "<style>.stApp { background-color: #1e1e1e; color: #ffffff; }</style>",
        unsafe_allow_html=True,
    )

if "messages" not in st.session_state:
    st.session_state.messages = []

if "total_tokens" not in st.session_state:
    st.session_state.total_tokens = 0

st.write("Quick templates:")
templates = {
    "Summarize Text": "Summarize the following text clearly.",
    "Explain Code": "Explain what this code does, step by step.",
    "Generate Ideas": "Generate 10 creative ideas on a topic of your choice.",
    "Rewrite Content": "Rewrite the following text to be clearer and more professional.",
    "Translate": "Translate the following text into English.",
    "Create Email": "Write a professional email for a common work situation.",
    "Brainstorm": "Let's brainstorm. Suggest interesting directions to explore.",
}

picked_prompt = None
cols = st.columns(3)
for i, (name, text) in enumerate(templates.items()):
    if cols[i % 3].button(name):
        picked_prompt = text

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

typed_prompt = st.chat_input("What is up?")
prompt = picked_prompt or typed_prompt

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            response = client.chat.completions.create(
                model=model_choice,
                messages=[
                    {"role": "system", "content": system_prompt}
                ] + [
                    {"role": m["role"], "content": m["content"]}
                    for m in st.session_state.messages
                ],
            )
            reply = response.choices[0].message.content
            st.markdown(reply)

            st.session_state.total_tokens += response.usage.total_tokens
            st.caption(f"{response.usage.total_tokens} tokens")

            st.session_state.messages.append({"role": "assistant", "content": reply})
        except Exception as e:
            st.error(f"Error: {e}")

st.sidebar.write("Total tokens used:", st.session_state.total_tokens)