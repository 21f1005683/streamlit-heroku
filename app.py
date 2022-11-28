import streamlit as st
import pandas as pd
st.write("""
#Add 2 numbers
""")

def user_input():
  num1 = st.number_input("First Number",min_value=-999999999, max_value=999999999)
  num2 = st.number_input("Second Number",min_value=-999999999, max_value=999999999)
  
  data={'First': num1,
        'Second':num2
       }
  
  numbers = pd.DataFrame(data, index=[0])
  return numbers

df=user_input()

st.subheader('User Input')
st.write(df.to_dict())