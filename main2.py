import streamlit as st

import openai


openai.api_key = "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"

engines = openai.Engine.list()

L = []
for i in engines.data:
    L.append(i["id"])

engine_Text = st.selectbox(
    'Which Engine would you like to select?',
    L)

st.title("Ask any question")
text = st.text_input("Enter the question here: ")

completion = openai.Completion.create(engine=engine_Text, prompt=text)

Completion_Text = completion.choices[0].text

st.text_area("The answer is:",Completion_Text)



