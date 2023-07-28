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

st.title('streamlit beautification')
st.header('By sk')
st.subheader('kanye')

#uploading the images
img1 = st.file_uploader('/Users/admin/Desktop/Screenshots/tiger copy.jpg')
img2 = st.file_uploader('/Users/admin/Desktop/Screenshots/lionsit.jpg')

#button 1

if img1 and img2 is not None:
    img1 = Image.open(img1)
    img2 = Image.open(img2)
    col1,col2 = st.columns(2)
    col1.image(img1)
    col2.image(img2)
    img1.save('hi.jpg')
    img2.save('lol.jpg')
    img1 = cv2.imread('hi.jpg')
    img2 = cv2.imread('lol.jpg')
    btn1 = st.button('convert my image to graysclae')
    if btn1:
#converting the images into grayscale
        col3,col4 = st.columns(2)
        img1_gray = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
        col3.image(img1_gray)
        img2_gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
        col4.image(img2_gray)

#button 2

btn2 = st.button('bitwise')

if btn2:
#converting the images into grayscale
    img_and = cv2.bitwise_and(img1,img2)
    img_or = cv2.bitwise_or(img1,img2)
    img_xor = cv2.bitwise_xor(img1,img2)
    cv2.imshow('and',img_and)
    cv2.imshow('or',img_or)
    cv2.imshow('xor', img_xor)
    cv2.imshow('sus', mytext)


'''#button 3

btn3 = st.button('bitwise')
    
if btn3:
#resizing images
    img1 = cv2.resize(img1,(400,400))
    img2 = cv2.resize(img2,(400,400))
        

#button 4

btn4 = st.button('bitwise')
    
if btn4:
#converting the images into grayscale
    mytext = cv2.putText(img1, 'sussy', (50,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,25,0), 2)
    mytext = cv2.putText(img2, 'oh hi lol', (50,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,25,0), 2)

'''       
