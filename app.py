import streamlit as st

st.set_page_config(page_title="Unit Convertor", page_icon="🎓")

# Rainbow header
st.markdown("""
    <h2 style="background: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet);
               -webkit-background-clip: text;
               color: transparent;
               font-weight: bold;">
        This is CONVERTOR!
    </h2>
    """, unsafe_allow_html=True)

# Background image styling
st.markdown("""
    <style>
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1507525428034-b723cf961d3e");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }

    div.stButton > button:first-child {
      background: linear-gradient(45deg, #00f260, #0575e6);
      color: white;
      padding: 15px 30px;
      font-size: 16px;
      border-radius: 12px;
      border: none;
      box-shadow: 0 0 10px #00f260, 0 0 20px #0575e6;
      transition: 0.4s ease-in-out;
      cursor: pointer;
    }

    div.stButton > button:first-child:hover {
      transform: rotate(3deg) scale(1.05);
    }
    </style>
    """, unsafe_allow_html=True)

# App title and instructions
st.title("🗺️Unit Convertor App♾️!!")
st.markdown("### Convert length, weight, and time instantly")
st.write("Welcome! Select a category, enter a value, and get the converted result in real time.")

# Category selection
category = st.selectbox("Select a Category", ["Length", "Weight", "Time"])

# Conversion function
def convert_units(category, value, unit):
    if category == "Length":
        if unit == "Kilometer to Miles":
            return value * 0.621371
        elif unit == "Kilometer to Meter":
            return value * 1000
        elif unit == "Meter to Kilometer":
            return value / 1000
        elif unit == "Miles to Kilometer":
            return value / 1.60934
        elif unit == "Meters to Feet":
            return value * 3.28084
        elif unit == "Feet to Meters":
            return value / 3.28084
        elif unit == "Centimeters to Inches":
            return value / 2.54
        elif unit == "Inches to Centimeters":
            return value * 2.54
        elif unit == "Millimeters to Inches":
            return value / 25.4
        elif unit == "Inches to Millimeters":
            return value * 25.4
        elif unit == "Yards to Meters":
            return value * 0.9144
        elif unit == "Meters to Yards":
            return value / 0.9144
        elif unit == "Miles to Yards":
            return value * 1760
        elif unit == "Yards to Miles":
            return value / 1760

    elif category == "Weight":
        if unit == "Kilogram to Pound":
            return value * 2.20462
        elif unit == "Pound to Kilogram":
            return value / 2.20462
        elif unit == "Milligrams to Grams":
            return value / 1000
        elif unit == "Grams to Milligrams":
            return value * 1000 
        elif unit == "Micrograms to Milligrams":
            return value / 1000
        elif unit == "Milligrams to Micrograms":
            return value * 1000

    elif category == "Time":
        if unit == "seconds to minutes":
            return value / 60
        elif unit == "minutes to seconds":
            return value * 60
        elif unit == "hours to minutes":
            return value * 60
        elif unit == "minutes to hours":
            return value / 60
        elif unit == "days to hours":
            return value * 24
        elif unit == "hours to days":
            return value / 24

# Unit selection based on category
if category == "Length":
    unit = st.selectbox("📏 Select a Conversion:", [
        "Kilometer to Miles", "Meter to Kilometer", "Kilometer to Miles", "Miles to Kilometer",
        "Meters to Feet", "Feet to Meters",
        "Centimeters to Inches", "Inches to Centimeters",
        "Millimeters to Inches", "Inches to Millimeters",
        "Yards to Meters", "Meters to Yards",
        "Miles to Yards", "Yards to Miles"
])
elif category == "Weight":
    unit = st.selectbox("⚖ Select a Conversion:", [
        "Kilogram to Pound", "Pound to Kilogram",
        "Milligrams to Grams", "Grams to Milligrams",
        "Micrograms to Milligrams", "Milligrams to Micrograms"
])
elif category == "Time":
    unit = st.selectbox("⏳Select a Conversion", [
        "seconds to minutes", "minutes to seconds", 
        "hours to minutes", "minutes to hours", 
        "days to hours", "hours to days"
])

# Input for value
value = st.number_input("Enter the value to convert")

# Custom styled Convert button (still functional)
if st.button("💎 CONVERT"):
    result = convert_units(category, value, unit)
    st.success(f"The result is {result:.2f}")
    st.balloons()


st.write("- - -")
st.write("🎀Create by Arsh ALi Azam🎀")