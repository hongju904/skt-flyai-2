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

# 실행
# streamlit run physiognomy.py

IMAGE_SIZE = (244,244)
BATCH_SIZE = 16

st.markdown("<h1 style='text-align: center; color: black;'>🫅관상 테스트🫅</h1>", unsafe_allow_html=True)
title = Image.open("title.png")
st.image(title, width=700)

option = st.selectbox(
    'How would you like to be contacted?',
    ('사진 촬영', '사진 업로드'))
if option == '사진 촬영':
   uploaded_file = st.camera_input("")
elif option == '사진 업로드':
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
    if st.button('분석'):
       start = True
    else:
       start = False

    if start:
        # progress bar
        st.write('AI가 당신의 관상을 분석중입니다.')
        my_bar = st.progress(0)
        for percent_complete in range(100):
            time.sleep(0.02)
            my_bar.progress(percent_complete + 1)

        # model load
        model = tf.keras.models.load_model('model_voicekeeper.h5')
        # 예측
        y_pred = model.predict(image)
        # df
        class_name = ['가축', '평민', '내시', '기생', '왕', '노비', '양반']
        df = pd.DataFrame({
        'Status':['가축', '평민', '내시', '기생', '왕', '노비', '양반'],
        'Percentage':y_pred[0]
        })
        # label
        label = np.argmax(y_pred, axis=1)
        # result 
        # result = class_name[int(label)]
        
        # 완료 아이콘
        st.success('분석 완료! 결과를 확인하세요', icon="✅")

        # 결과 확인
        with st.expander("결과 확인"):
            MAX = df['Status'].iloc[np.argmax(df['Percentage'])]

            if MAX == '가축':
                st.markdown("<h3 style='text-align: center; color: black;'>야생미 넘치는 가축</h3>", unsafe_allow_html=True)
                image2 = Image.open("cattle.jfif")
                st.image(image2, width=700)

            elif MAX == '평민':
                st.markdown("<h3 style='text-align: center; color: black;'>묵묵히 자기일 잘 하는 평민</h3>", unsafe_allow_html=True)
                image2 = Image.open("commons.png")
                st.image(image2, width=700)

            elif MAX == '내시':
                st.markdown("<h3 style='text-align: center; color: black;'>왕을 보좌하는 눈치빠른 내시</h3>", unsafe_allow_html=True)
                image2 = Image.open("eunuch.png")
                st.image(image2, width=700)

            elif MAX == '기생':
                st.markdown("<h3 style='text-align: center; color: black;'>언변이 뛰어난 기생</h3>", unsafe_allow_html=True)
                image2 = Image.open("gisaeng.jpg")
                st.image(image2, width=700)

            elif MAX == '왕':
                st.markdown("<h3 style='text-align: center; color: black;'>백성을 우선시하는 임금</h3>", unsafe_allow_html=True)
                image2 = Image.open("king.png")
                st.image(image2, width=700)

            elif MAX == '노비':
                st.markdown("<h3 style='text-align: center; color: black;'>백성들의 연예인, 망나니</h3>", unsafe_allow_html=True)
                image2 = Image.open("slave.png")
                st.image(image2, width=700)

            elif MAX == '양반':
                st.markdown("<h3 style='text-align: center; color: black;'>족보있는 집의 양반</h3>", unsafe_allow_html=True)
                image2 = Image.open("yangban.png")
                st.image(image2, width=700)

            state_graph = px.bar(df, x='Status', y='Percentage', color='Status', labels=False)
            state_graph.update_layout(
            autosize=False,
            width=650,
            height=400)
            st.plotly_chart(state_graph)
