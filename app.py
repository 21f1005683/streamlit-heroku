import streamlit as st
import pandas as pd
st.write("""
Build a streamlit web application for the following usecase and host the application using heroku.
UseCase : Multiplication of 2 given numbers.
""")

def user_input():
  num1 = st.number_input("First Number")
  num2 = st.number_input("Second Number")
  
  data={'First': num1,
        'Second':num2
       }
  
  numbers = pd.DataFrame(data, index=[0])
  return numbers

df=user_input()



n1=df['First']
n2=df['Second']
p=n1*n2
st.subheader('The product is')
st.write(p)
