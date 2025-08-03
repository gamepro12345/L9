import streamlit as st

st.title("ユーザー情報入力")

# session_stateの初期化
if 'user_name' not in st.session_state:
    st.session_state.user_name = ""
if 'user_class' not in st.session_state:
    st.session_state.user_class = ""
if 'user_hobby' not in st.session_state:
    st.session_state.user_hobby = ""

# ユーザー名の入力
name = st.text_input("あなたの名前を入力してください")
grade = st.selectbox("学年を選択してください",["小５", "小６", "中１", "中２", "中３"])
hobby = st.multiselect("趣味を選んでください", ["読書", "スポーツ", "音楽", "ゲーム","その他"])

if st.button("情報を保存"):
    st.session_state.user_name = name
    st.session_state.user_class = grade
    st.session_state.user_hobby = hobby

    st.success("情報を保存しました!")
