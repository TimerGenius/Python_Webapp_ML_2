#importing the libraries 
import streamlit as st
import cv2
from PIL import Image

#background for application

bg = f'''
<style>
.stApp{{
background-image:url('https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/9720e55c-d222-4769-90b8-aec2262c0988/ddvtmz1-cadfaa7f-6da9-4b59-a0fe-6ed5742af38c.jpg/v1/fill/w_1192,h_670,q_70,strp/bruh_by_jukeboxfromao_ddvtmz1-pre.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9NzIwIiwicGF0aCI6IlwvZlwvOTcyMGU1NWMtZDIyMi00NzY5LTkwYjgtYWVjMjI2MmMwOTg4XC9kZHZ0bXoxLWNhZGZhYTdmLTZkYTktNGI1OS1hMGZlLTZlZDU3NDJhZjM4Yy5qcGciLCJ3aWR0aCI6Ijw9MTI4MCJ9XV0sImF1ZCI6WyJ1cm46c2VydmljZTppbWFnZS5vcGVyYXRpb25zIl19.OTeZgFcV45DZqyg43rAeGzSld3mOIMTCffVyi3SGM8o');
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
