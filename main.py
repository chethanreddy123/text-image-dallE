import streamlit as st
import time
import os
import openai
openai.organization = "org-0ypSMwDVq8KPrWQ2VoclmvC7"
openai.api_key = "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"

st.sidebar.title('Developer\'s Contact')
st.sidebar.markdown('[![Chethan-Reddy]'
                '(https://img.shields.io/badge/Author-Chethan%20Reddy-brightgreen)]'
                '(https://www.linkedin.com/in/chethan-reddy-0201791ba/)') 

st.sidebar.success("Created Using OpenAI Dall - E")

st.title("Text to image using DALL - E")

text = st.text_input('Enter the Text to generate image: ', 'lion with dog')

check = st.button("Click Here to Generate!")


with st.spinner('Wait for it...'):
    time.sleep(5)

if check == True:
    st.caption("Hold on it might take a min!!")
    response = openai.Image.create(
    prompt=text,
    n=1,
    size="1024x1024"
    )
    image_url = response['data'][0]['url']
    st.image(
                image_url,
                width=400, # Manually Adjust the width of the image as per requirement
            )
    st.success('Done!')
