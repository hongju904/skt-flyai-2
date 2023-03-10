import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import time
import plotly.express as px

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, MaxPooling2D, Rescaling
from tensorflow.keras import Input
from tensorflow.keras.applications.resnet50 import ResNet50
from tensorflow.keras import callbacks

# μ€ν
# streamlit run physiognomy.py

IMAGE_SIZE = (244,244)
BATCH_SIZE = 16

st.markdown("<h1 style='text-align: center; color: black;'>π«κ΄μ νμ€νΈπ«</h1>", unsafe_allow_html=True)
title = Image.open("title.png")
st.image(title, width=700)

option = st.selectbox(
    'How would you like to be contacted?',
    ('μ¬μ§ μ΄¬μ', 'μ¬μ§ μλ‘λ'))
if option == 'μ¬μ§ μ΄¬μ':
   uploaded_file = st.camera_input("")
elif option == 'μ¬μ§ μλ‘λ':
   uploaded_file = st.file_uploader("", label_visibility='collapsed')

# img show
if uploaded_file:
    image = Image.open(uploaded_file)
    # img size 
    image = image.resize(IMAGE_SIZE)
    # img show
    st.image(image, width=700)
    image = np.array(image)
    image = image.reshape(-1, 244, 244, 3)
    
    # button
    if st.button('λΆμ'):
       start = True
    else:
       start = False

    if start:
        # progress bar
        st.write('AIκ° λΉμ μ κ΄μμ λΆμμ€μλλ€.')
        my_bar = st.progress(0)
        for percent_complete in range(100):
            time.sleep(0.02)
            my_bar.progress(percent_complete + 1)

        # model load
        model = tf.keras.models.load_model('model_voicekeeper.h5')
        # μμΈ‘
        y_pred = model.predict(image)
        # df
        class_name = ['κ°μΆ', 'νλ―Ό', 'λ΄μ', 'κΈ°μ', 'μ', 'λΈλΉ', 'μλ°']
        df = pd.DataFrame({
        'Status':['κ°μΆ', 'νλ―Ό', 'λ΄μ', 'κΈ°μ', 'μ', 'λΈλΉ', 'μλ°'],
        'Percentage':y_pred[0]
        })
        # label
        label = np.argmax(y_pred, axis=1)
        # result 
        # result = class_name[int(label)]
        
        # μλ£ μμ΄μ½
        st.success('λΆμ μλ£! κ²°κ³Όλ₯Ό νμΈνμΈμ', icon="β")

        # κ²°κ³Ό νμΈ
        with st.expander("κ²°κ³Ό νμΈ"):
            MAX = df['Status'].iloc[np.argmax(df['Percentage'])]

            if MAX == 'κ°μΆ':
                st.markdown("<h3 style='text-align: center; color: black;'>μΌμλ―Έ λμΉλ κ°μΆ</h3>", unsafe_allow_html=True)
                image2 = Image.open("cattle.jfif")
                st.image(image2, width=700)

            elif MAX == 'νλ―Ό':
                st.markdown("<h3 style='text-align: center; color: black;'>λ¬΅λ¬΅ν μκΈ°μΌ μ νλ νλ―Ό</h3>", unsafe_allow_html=True)
                image2 = Image.open("commons.png")
                st.image(image2, width=700)

            elif MAX == 'λ΄μ':
                st.markdown("<h3 style='text-align: center; color: black;'>μμ λ³΄μ’νλ λμΉλΉ λ₯Έ λ΄μ</h3>", unsafe_allow_html=True)
                image2 = Image.open("eunuch.png")
                st.image(image2, width=700)

            elif MAX == 'κΈ°μ':
                st.markdown("<h3 style='text-align: center; color: black;'>μΈλ³μ΄ λ°μ΄λ κΈ°μ</h3>", unsafe_allow_html=True)
                image2 = Image.open("gisaeng.jpg")
                st.image(image2, width=700)

            elif MAX == 'μ':
                st.markdown("<h3 style='text-align: center; color: black;'>λ°±μ±μ μ°μ μνλ μκΈ</h3>", unsafe_allow_html=True)
                image2 = Image.open("king.png")
                st.image(image2, width=700)

            elif MAX == 'λΈλΉ':
                st.markdown("<h3 style='text-align: center; color: black;'>λ°±μ±λ€μ μ°μμΈ, λ§λλ</h3>", unsafe_allow_html=True)
                image2 = Image.open("slave.png")
                st.image(image2, width=700)

            elif MAX == 'μλ°':
                st.markdown("<h3 style='text-align: center; color: black;'>μ‘±λ³΄μλ μ§μ μλ°</h3>", unsafe_allow_html=True)
                image2 = Image.open("yangban.png")
                st.image(image2, width=700)

            state_graph = px.bar(df, x='Status', y='Percentage', color='Status', labels=False)
            state_graph.update_layout(
            autosize=False,
            width=650,
            height=400)
            st.plotly_chart(state_graph)
