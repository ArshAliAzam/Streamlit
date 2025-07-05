import google.generativeai as genai
import streamlit as st

# 🔐 Set your Gemini API key
genai.configure(api_key="AIzaSyDuughEzMQozAS4i4hZbm3MUEuIPCIxWsw")

# 🎯 Load Gemini model (you can use gemini-1.5-pro, too)
model = genai.GenerativeModel("gemini-1.5-flash")

# ⚙️ Streamlit page setup
st.set_page_config(page_title="Charles - Gemini AI", page_icon="🤖")

# 🎨 Set background image using custom CSS
st.markdown(
    """
    <style>
    .stApp {
        background-image: url('https://images.unsplash.com/photo-1503264116251-35a269479413?auto=format&fit=crop&w=1600&q=80');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        font-family: 'Arial', sans-serif;
    }
    .block-container {
        background-color: rgba(255, 255, 255, 0.85);
        padding: 2rem;
        border-radius: 16px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 🧠 Title and intro
st.title("🎬 Charles - Gemini AI Assistant")
st.markdown("""
Hi! My name is **Charles** 🤖  
I'm an AI assistant powered by Google's **Gemini 1.5 Flash**, created by *Arsh Ali Azam*.  
Ask me anything about AI, coding, or tech — I'm here to help!
""")

# ✏️ User input
user_input = st.text_input("Enter your question:")

# 🔘 Handle response
if st.button("Ask"):
    if not user_input.strip():
        st.warning("Please enter something.")
    else:
        try:
            response = model.generate_content(user_input)
            st.markdown("### Charles says:")
            st.write(response.text)
        except Exception as e:
            st.error(f"❌ Error: {e}")
