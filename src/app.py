import random
import streamlit as st

st.title("文字列から単語を選択するアプリ")

text = st.text_input("スペース区切りで単語を入力してください")

words = text.replace("　", " ").split(" ")

st.write("入力した単語：", words)

if st.button("一つ選ぶ"):
    choice = random.choice(words)
    st.write("返された単語：", choice)

st.write("`文字列の表示`")