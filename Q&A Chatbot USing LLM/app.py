# Q&A Chatbot
from langchain.llms import OpenAI

#from dotenv import load_dotenv

#load_dotenv()  # take environment variables from .env.

import streamlit as st
import os


## Function to load OpenAI model and get respones

def get_openai_response(question):
    # Retrieve the API key from environment variables
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY environment variable not set.")
    
    # Initialize the OpenAI model
    llm = OpenAI(openai_api_key=api_key, model_name="text-davinci-003", temperature=0.5)
    
    # Generate a response for the given question
    response = llm.generate(question)
    
    return response

##initialize our streamlit app

st.set_page_config(page_title="Q&A Demo")

st.header("Langchain Application")

input=st.text_input("Input: ",key="input")
response=get_openai_response(input)

submit=st.button("Ask the question")

## If ask button is clicked

if submit:
    st.subheader("The Response is")
    st.write(response)




