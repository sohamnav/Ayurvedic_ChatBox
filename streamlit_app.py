import streamlit as st
import openai
import os
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]
openai.api_key = st.secrets["OPENAI_API_KEY"]

def get_response(question):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "You are a helpful assistant."},
                  {"role": "user", "content": question}],
        max_tokens=50
    )
    return response['choices'][0]['message']['content']
st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://cdn.pixabay.com/photo/2023/08/29/18/29/ai-generated-8221937_640.png");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
html_temp = """ 
  <div style="background-color:orange ;padding:7px">
  <h2 style="color:black;text-align:center;"><b>Ayurvedic Research QA System<b></h2>
  </div>
  """ 
st.markdown(html_temp,unsafe_allow_html=True)
st.write("Ask your questions related to Ayurvedic research")
user_question = st.text_input("Ask your question here:")

if st.button("Get Answer"):
        if user_question:
            with st.spinner('Searching for answer...'):
                answer = get_response(user_question)
            st.success(answer)
            st.success('Thank you for using the ayurvedic chatbot. Hope your query is answered.')
        else:
            st.warning("Please enter a question.")

st.write(' ')
st.write(' ')
st.write(' ')
st.write(' ')
st.write(' ')
st.write(' ')
st.write(' ')
st.write(' ')
st.write(' ')
st.write(' ')
st.write(' ')
st.write(' ')
st.write(' ')


st.write('Developed by Sairam.V.A')
st.write('github-https://github.com/sairamadithya')
st.write('linktree-https://linktr.ee/sairamadithya')
