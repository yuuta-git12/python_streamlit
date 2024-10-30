import random
import streamlit as st
import pandas as pd


# セッションを使ってdicesの中身が保持されるようにする
if "dices" not in st.session_state:  # セッションデータの初期化
    st.session_state.dices = []

st.title("2つのサイコロを振るアプリ")

multiple = st.toggle("複数回振る", False)

if not multiple:
    if st.button("サイコロを振る"):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        dice_sum = dice1 + dice2
        st.session_state.dices.append((dice1, dice2, dice_sum))
        st.write(f"1つ目のサイコロ:{dice1}/2つ目のサイコロ:{dice2}")
else:
    n = st.slider("回数", 1, 1000, 500)
    if st.button("サイコロを振る"):
        for _ in range(n):
            dice1 = random.randint(1, 6)
            dice2 = random.randint(1, 6)
            dice_sum = dice1 + dice2
            st.session_state.dices.append((dice1, dice2, dice_sum))
        st.write(f"{n}回振りました。")

reset_button = st.button("リセット")
if st.session_state.dices and reset_button:
    st.session_state.dices = []

df = pd.DataFrame(st.session_state.dices, columns=["1つ目のサイコロ", "2つ目のサイコロ", "合計"])
st.dataframe(df)
st.write("試行回数", len(st.session_state.dices))

if st.button("結果を表示"):
    st.bar_chart(df["合計"].value_counts())