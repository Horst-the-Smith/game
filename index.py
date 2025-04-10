import streamlit as st
import csv

# CSVからアカウント情報を読み取る関数
def load_accounts(file_path):
    accounts = []
    try:
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                accounts.append(row)
    except Exception as e:
        st.error(f"エラーが発生しました: {e}")
    return accounts

# ログイン認証機能
def authenticate(username, password, accounts):
    for account in accounts:
        if account['username'] == username and account['password'] == password:
            return True
    return False

# Mainアプリ
def main():
    st.title("ログインアプリ")

    # CSVファイルからデータを読み込む
    accounts = load_accounts("accounts.csv")
    if not accounts:
        st.error("アカウント情報がありません。")
        return

    # 入力フォーム
    st.sidebar.header("ログイン")
    username = st.sidebar.text_input("ユーザー名")
    password = st.sidebar.text_input("パスワード", type="password")
    login_button = st.sidebar.button("ログイン")

    # 認証
    if login_button:
        if authenticate(username, password, accounts):
            st.success(f"ようこそ、{username}さん！")
        else:
            st.error("ログイン失敗：ユーザー名またはパスワードが間違っています。")

if __name__ == "__main__":
    main()