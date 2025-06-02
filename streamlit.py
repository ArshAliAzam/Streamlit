import streamlit as st
import asyncio
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig

# Set up API key and client
gemini_api_key = "AIzaSyBa0m6kJeBlyUb6GRrWS8lnuyzlqwk8aN8"  # Don't hardcode in production

client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=client
)

config = RunConfig(
    model=model,
    model_provider=client,
    tracing_disabled=True
)

# Async function to run the agent
async def run_agent(user_input):
    agent = Agent(name="Assistant", instructions="You are a helpful assistant.")
    result = await Runner.run(starting_agent=agent, input=user_input, run_config=config)
    return result.final_output

# Streamlit UI
st.set_page_config(page_title="Gemini Assistant", page_icon="🤖")
st.title("🎬 Agent AI")
st.write("""Hi! My name is Charles. I am a Agent created By 'ARSH ALI AZAM'.
         I can Help u in Any thing About AI🤍
         """)

user_input = st.text_input("Enter your question:")

if st.button("Ask"):
    if not user_input.strip():
        st.warning("Please enter a question.")
    else:
        try:
            final_output = asyncio.run(run_agent(user_input))
            st.markdown("### Charles is Answering...:")
            st.write(final_output)
        except RuntimeError:
            # Workaround for already running event loop in Streamlit
            final_output = asyncio.get_event_loop().run_until_complete(run_agent(user_input))
            st.markdown("### Charles is Answering...:")
            st.write(final_output)
