import google.generativeai as genai
import streamlit as st

f = open("keys/.gemini_api_key.txt")
key = f.read()

# Read the API key and configure genai
genai.configure(api_key=key)

#########################################

# set page title
st.title(":blue[💬 AI Data Science Tutor with Google GenAI]")
#########################################

# init a gemini model
model = genai.GenerativeModel(model_name="models/gemini-1.5-pro-latest", 
                              system_instruction="""You are a helpful AI Teaching Assistant,
                              Given a Data Science topic, help the user understand it.
                              You also answer all followup questions as well.
                              if a question is not related to data science, the response should be,
                              'I may not be able to provide information about this topic' """)

# if chat history not in session, init one
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

#init the chat object
chat = model.start_chat(history=st.session_state["chat_history"])

for msg in chat.history:
    st.chat_message(msg.role).write(msg.parts[0].text)

user_input = st.chat_input()

if user_input:
    st.chat_message("user").write(user_input)
    response = chat.send_message(user_input)
    st.chat_message("ai").write(response.text)
    st.session_state["chat_history"] = chat.history
