#!/usr/bin/env python
# coding: utf-8

# # Streamlit App Generation

# # Taylor Stacey

# In[1]:


pip install streamlit langchain openai


# In[3]:


import streamlit as st
from langchain.llms import OpenAI


# In[4]:


st.image('DSU_Logo.png', width=100)
st.title('🦜🔗 Quickstart App')


# In[5]:


openai_api_key = st.sidebar.text_input('OpenAI API Key')


# In[6]:


def generate_response(input_text):
  llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
  st.info(llm(input_text))


# In[7]:


with st.form('my_form'):
  text = st.text_area('Enter text:', 'What are the three key pieces of advice for learning how to code?')
  submitted = st.form_submit_button('Submit')
  if not openai_api_key.startswith('sk-'):
    st.warning('Please enter your OpenAI API key!', icon='⚠')
  if submitted and openai_api_key.startswith('sk-'):
    generate_response(text)

