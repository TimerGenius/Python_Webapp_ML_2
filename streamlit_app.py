#importing the libraries 
import streamlit as st
import cv2
from PIL import Image

#background for application

bg = f'''
<style>
.stApp{{
background-image:url('https://media.tenor.com/_4YgA77ExHEAAAAd/rick-roll.gif');
background-size: cover;
}}
</style>'''

st.markdown(bg,unsafe_allow_html=True)

st.title('You were rickrolled by saurish')
st.header('cry about it lol')
