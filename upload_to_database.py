import streamlit_authenticator as stauth

import database as db

usernames = ["mdasif", "mdnoman"]
names = ["Md Asif", "Md Noman"]
passwords = ["123456", "654321"]

hashed_passwords = stauth.Hasher(passwords).generate()

for username, name, hash_password in zip(usernames, names, hashed_passwords):
    db.insert_user(username, name, hash_password)
