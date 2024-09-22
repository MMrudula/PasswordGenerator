import streamlit as st
import random
import string
def generate_password(length,use_digits,use_special_chars,use_uppercase):
    characters = string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation
    if use_uppercase:
        characters += string.ascii_uppercase
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
generate_password(10,True,True,False)
print(generate_password(10,True,True,True))
#user preferences 
st.title('Secure Password Generator')
st.sidebar.header('Password Options')
length = st.sidebar.slider('Password Length', min_value=6, max_value=20, value=12, step=1)
use_digits = st.sidebar.checkbox('Include Digits', value=True)
use_special_chars = st.sidebar.checkbox('Include Special Characters', value=True)
use_uppercase = st.sidebar.checkbox('Include Uppercase Letters', value=True)
