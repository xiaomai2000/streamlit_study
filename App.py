import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Welcome to Finance P&L reporting tool! 👋")

st.sidebar.success("Select a function above.")

st.markdown(
    """
    "Finance P&L reporting tool" is built to automate the monthly P&L reports.

    **👈 Select a function from the sidebar**

"""
)

