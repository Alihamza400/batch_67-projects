import streamlit as st

# Sidebar Navigation
page = st.sidebar.radio("Go to", ["Home", "Products", "Cart"])

if page == "Home":
    st.title("🏠 Home Page")
    st.write("Welcome to our eCommerce Store!")

elif page == "Products":
    st.title("🛒 Products")
    st.write("Browse our product collection.")

elif page == "Cart":
    st.title("🛍️ Shopping Cart")
    st.write("View items in your cart.")

