import streamlit as st

# Sidebar Title
st.sidebar.title("🏀 All-Star AI Support Team")

# Agent Selector
agent_option = st.sidebar.radio("Choose Your AI Agent", [
    "🏁 Jordan – Onboarding",
    "🐍 Kobe – Education Coach",
    "🔥 Maya – Nurture + Motivation",
    "🎩 Magic – Opportunity Connector",
    "📣 Lisa – Parent Communication",
    "📲 Candace – Communication Agent",
    "🧠 Kareem – Mental Performance",
    "🧭 Dawn – Emotional Reset",
    "🛡️ Bill – System Manager (Utility)"
])

# Placeholder for agent outputs
st.title("🤖 Welcome to the AI Recruiting Dashboard")

# Agent Logic
if agent_option == "🏁 Jordan – Onboarding":
    st.header("Jordan – Onboarding Specialist")
    st.markdown("Jordan greets new users, captures basic info, and sets expectations.")
    # Call Jordan’s chatbot logic here

elif agent_option == "🐍 Kobe – Education Coach":
    st.header("Kobe – Recruiting Education Coach")
    st.markdown("Kobe delivers training, challenge prompts, and motivation.")
    # Call Kobe’s logic here

elif agent_option == "🔥 Maya – Nurture + Motivation":
    st.header("Maya – Nurturing Strategist")
    st.markdown("Maya keeps athletes engaged through uplifting nudges and content.")
    # Call Maya’s logic here

elif agent_option == "🎩 Magic – Opportunity Connector":
    st.header("Magic – Matchmaking Assistant")
    st.markdown("Magic helps athletes connect to the right schools based on stats and needs.")
    # Call Magic’s logic here

elif agent_option == "📣 Lisa – Parent Communication":
    st.header("Lisa – Family Liaison")
    st.markdown("Lisa simplifies updates, sets reminders, and bridges communication with parents.")
    # Call Lisa’s logic here

elif agent_option == "📲 Candace – Communication Agent":
    st.header("Candace – Outreach Coordinator")
    st.markdown("Candace sends emails, SMS, or makes calls based on athlete activity.")
    # Call Candace’s communication logic here

elif agent_option == "🧠 Kareem – Mental Performance":
    st.header("Kareem – Mental Toughness Trainer")
    st.markdown("Kareem delivers confidence-building routines and mindset content.")
    # Call Kareem’s logic here

elif agent_option == "🧭 Dawn – Emotional Reset":
    st.header("Dawn – Emotional Check-in Agent")
    st.markdown("Dawn provides mood check-ins, tough love, and recovery flows.")
    # Call Dawn’s logic here

elif agent_option == "🛡️ Bill – System Manager":
    st.header("Bill – The General (System Utility)")
    st.markdown("Bill keeps all agents functioning, logs activity, and triggers alerts.")
    # Backend monitoring or alert messages here

# Optional: Add a footer or logo
st.markdown("---")
st.caption("Facilitate The Process | Powered by 28 Foot Marketing")
import streamlit as st
from streamlit.components.v1 import html

st.set_page_config(layout="wide", page_title="AI Recruiting Dashboard")

st.sidebar.title("🎮 Select AI Agent")
agent = st.sidebar.radio("Choose your assistant:", ["Jordan", "Kobe", "Candace", "Magic", "Lisa", "Bill"])

st.title("🏀 AI Recruiting Staff: 3D Interactive Dashboard")

# Injecting a free 3D animation (placeholder iframe)
html("""
<div style='text-align:center'>
  <iframe src='https://my.spline.design/rotatingcube-3dmodel' width='500' height='400' frameborder='0'></iframe>
</div>
""", height=420)

st.subheader(f"Agent: {agent}")
st.write("**Quote:**", {
    "Jordan": "Breaks the ice and gets players set up fast.",
    "Kobe": "Delivers sharp, consistent training lessons.",
    "Candace": "Handles text, email, and coach check-ins like a pro.",
    "Magic": "Introduces athletes to exposure opportunities.",
    "Lisa": "Keeps parents updated, engaged, and supported.",
    "Bill": "Monitors the entire system and calls out issues."
}[agent])

# Fake real-time feedback
st.success(f"{agent} completed 3 tasks this hour.")

if agent == "Bill":
    st.warning("🚨 Alert: Magic has not sent this week's opportunity email.")
