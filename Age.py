import streamlit as st
from datetime import date

def calculate_age(birthdate):
    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

# Streamlit UI
st.set_page_config(page_title="Age Calculator", page_icon="⏳", layout="centered")
st.title("🎂 Age Calculator App")

# Sidebar for user input
st.sidebar.header("Enter Your Birthdate")
birthdate = st.sidebar.date_input("Select your birthdate", min_value=date(1900, 1, 1), max_value=date.today())

# Calculate age
if st.sidebar.button("Calculate Age"):
    age = calculate_age(birthdate)
    st.success(f"🎉 You are {age} years old!")

# Custom styling
st.markdown(
    """
    <style>
        body {
            font-family: 'Poppins', sans-serif;
            background: linear-gradient(to right, #ff7e5f, #feb47b);
            color: white;
        }
        .stButton>button {
            background-color: #ff6f61;
            color: white;
            font-size: 18px;
            padding: 10px 20px;
            border-radius: 10px;
            transition: 0.3s;
        }
        .stButton>button:hover {
            background-color: #ff4a3d;
        }
    </style>
    """,
    unsafe_allow_html=True
)