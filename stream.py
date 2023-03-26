import streamlit as st
import pandas as pd

st.set_page_config(page_title="Streamlit Example App")

menu_items = {"Home": "/", "Data": "/data", "About": "/about"}
menu_selection = st.sidebar.selectbox("Go to", list(menu_items.keys()),index=0)
if menu_selection != "Home":
    st.sidebar.write("Selected:", menu_selection)
page = menu_items[menu_selection]


data = pd.DataFrame({
    "Name": ["Daniel", "Bob", "Charlie", "David", "Emily", "Frank"],
    "Age": [25, 32, 18, 47, 22, 36],
    "Gender": ["F", "M", "M", "M", "F", "M"]

})

min_age = st.sidebar.slider("Minimum age", min_value=0, max_value=100, value=0)
filtered_data = data[data["Age"]>=min_age]

st.title("Streamlit Example App")
if page == "/data":
    st.write("Data")
    st.write(filtered_data)
else:
    st.write("Home")
    st.write(data)

if "counter" not in st.session_state:

    st.session_state.counter = 330000000

st.write(f"Counter: {st.session_state.counter}")

if st.button("increment"):
    st.session_state.counter +=1

col1, col2 = st.columns([2, 1])
with col1:
    st.write("This is column 1")
    if st.checkbox("Show more"):
        st.write("You clicked the checkbox!")
with col2:
    st.write("This is column 2")
    if st.button("Click me"):
        st.write("You clicked the button!")
