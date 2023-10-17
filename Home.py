import streamlit as st

#imporţ face_rec

st.set_page_config(page_title='Attendance System')

st.header('Attendance System using Face Recognition')

with st.spinner("Loading Models and Conneting to Redis db ..."):
    import face_rec
    
st.success('Model loaded sucesfully')
st.success('Redis db sucessfully connected')