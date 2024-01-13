import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpeg", width=400)

with col2:
    st.title("Nazmussakib")
    content = """
    Hi, I am Sakib! I am a Python programmer. I graduated in 2023 with a Bachelor of Science in Computer Science & Engineering 
    from Daffodil International University in Bangladesh with a focus on using
    Python language. """
    st.info(content)

content2 = """
Below you can find some the app I have build in Python."""
st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")
