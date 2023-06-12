import streamlit as st
import streamlit_authenticator as stauth

import database as db


st.set_page_config(
    page_title="Multipage App",
    page_icon="👏",
)

# --- USER AUTHENTICATION ---
users = db.fetch_all_users()
usernames = [user["key"] for user in users]
names = [user["name"] for user in users]
hashed_passwords = [user["password"] for user in users]


authenticator = stauth.Authenticate(
    names,
    usernames,
    hashed_passwords,
    "sales_dashboard",
    "abcdef",
    cookie_expiry_days=30,
)

name, authentication_status, username = authenticator.login("Login", "main")

if authentication_status == False:
    st.error("Username/password is incorrect")

if authentication_status == None:
    st.warning("Please enter your username and password")


if authentication_status:
    authenticator.logout("Logout", "sidebar")
    st.sidebar.title(f"Welcome {name}")

    st.title("Main Page")

    st.sidebar.success("Select a page above.")

    # if "my_input" not in st.session_state:
    #     st.session_state["my_input"] = ""

    # my_input = st.text_input("Input a text here", st.session_state["my_input"])
    # submit = st.button("Submit")
    # if submit:
    #     st.session_state["my_input"] = my_input
    #     st.write("You have enteted: ", my_input)
