# steramlit 

import streamlit as st


st.set_page_config(page_title="Growth mimdset project", page_icon="🌿")

# background
st.markdown("""
    <style>
    .stApp {
        background-image: url("https://i.pinimg.com/736x/27/c3/b2/27c3b2d608f1a4b0ccb6eafa294f92c8.jpg");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-position: center;
    }
    </style>
    """, unsafe_allow_html=True)


st.markdown("""
<style>
.progress-bar {
  width: 100%;
  background-color: #222;
  border-radius: 20px;
  overflow: hidden;
  box-shadow: 0 0 5px #00f2fe;
}

.progress-bar-fill {
  height: 25px;
  width: 80%;
  background: linear-gradient(90deg, #4facfe, #00f2fe);
  animation: fill 3s ease-in-out infinite;
}

@keyframes fill {
  0% {width: 0;}
  50% {width: 80%;}
  100% {width: 0;}
}
</style>

<div class="progress-bar">
  <div class="progress-bar-fill"></div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
    <h2 style="background: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet);
               -webkit-background-clip: text;
               color: transparent;
               font-weight: bold;">
        Growth Mindset Challenge: by Arsh Ali Azam!
    </h2>
    """, unsafe_allow_html=True)

st.title("☘️Growth Mindset")

st.header("🐣 Welcome to your growth Journey!")
st.write("Embrace Challenge, Learn from mistake, and unlock your full potential. This AI-powerd app helps you build a growth mindset with reflection, challenges, and achievements! 🧙‍♂️ ")

st.header("🌞Today's Growth Mindset Quote")
st.write('"Success is not final, failure is not fatal: it is the courage to contiune that counts."-Winston Churchill')

st.header("🤺What's Your Challenge Today?")
user_input = st.text_input("Describe a challenge you're facing: ")


if user_input:
    st.success(f"🧧you are Facing: {user_input}. Keep pushing forwards your gaol!")
else:
    st.warning("Tell us about your challenge to get started")


st.header("🪞Reflection on your Learning")
reflection = st.text_area("Write your reflection here:")
if reflection:
    st.success(f"🌟Great Insight: Your Reflection: {reflection}💫")
else:
    st.info("Reflecting on past experience help you grow! share your difficulties.")

st.header("🎀🥳Celebrate Your Wins!!")
achivment = st.text_input("🦈share Something you're recently accomplished:")

if achivment:
    st.success(f"🤩Amazing! You achivment: {achivment}")
else:
    st.info("🌠Big or small, every acheivment counts: share one now")


st.write("- - -")
st.write("**🏁Dream big. Start small. Act now**")
st.write("💖💖Created by Arsh Ali Azam💖💖")





























