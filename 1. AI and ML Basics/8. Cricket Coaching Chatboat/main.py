import streamlit as st
import openai

# Page setup
st.set_page_config(page_title="Cricket Coach Chatbot", layout="centered")
st.title("🏏 Your Personal Cricket Coach")

# Load API key from secrets (do not hardcode)
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Guardrails: Define system behavior
SYSTEM_MESSAGE = {
    "role": "system",
    "content": (
        "You are a friendly and expert cricket coach. Provide helpful, technical, and beginner-friendly guidance "
        "on cricket skills like batting, bowling, fielding, fitness, and mental training. Avoid giving medical or legal advice."
    )
}

# Session state initialization
if "past_user_inputs" not in st.session_state:
    st.session_state.past_user_inputs = []
if "ai_generated_responses" not in st.session_state:
    st.session_state.ai_generated_responses = []

# Build full conversation history
def build_message_list():
    messages = [SYSTEM_MESSAGE]
    for user, ai in zip(st.session_state.past_user_inputs, st.session_state.ai_generated_responses):
        messages.append({"role": "user", "content": user})
        messages.append({"role": "assistant", "content": ai})
    return messages

# Generate AI response from OpenAI
def generate_response(user_prompt):
    messages = build_message_list()
    messages.append({"role": "user", "content": user_prompt})

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.7
    )
    return response['choices'][0]['message']['content']

# Chat form
with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("Ask your cricket coach anything:")
    submitted = st.form_submit_button("Send")

    if submitted and user_input:
        st.session_state.past_user_inputs.append(user_input)
        reply = generate_response(user_input)
        st.session_state.ai_generated_responses.append(reply)

# Display chat history
for user, ai in zip(reversed(st.session_state.past_user_inputs), reversed(st.session_state.ai_generated_responses)):
    st.markdown(f"**You:** {user}")
    st.markdown(f"**🏏 Coach:** {ai}")
    st.markdown("---")
