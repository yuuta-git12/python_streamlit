import random
import streamlit as st
import pandas as pd

dices = []

st.title("2つのサイコロを振るアプリ")

if st.button("サイコロを振る"):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    dice_sum = dice1 + dice2
    dices.append((dice1, dice2, dice_sum))
    st.write(f"1つ目のサイコロ:{dice1}/2つ目のサイコロ:{dice2}")

df = pd.DataFrame(dices, columns=["1つ目のサイコロ", "2つ目のサイコロ", "合計"])
st.dataframe(df)
st.write("試行回数", len(dices))