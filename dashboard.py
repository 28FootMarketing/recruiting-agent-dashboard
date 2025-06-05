
import streamlit as st
import importlib

st.set_page_config(page_title="Recruiting AI Agent Dashboard", page_icon="🤖", layout="centered")
st.title("🏆 Athletic Recruiting Agent Hub")
st.subheader("Switch between your all-star AI support team")

agents = {
    "Jordan – Onboarding Specialist": "jordan",
    "Kobe – Recruiting Education Coach": "kobe",
    "Maya – Nurture & Motivation": "maya",
    "Magic – Opportunity Connector": "magic",
    "Lisa – Parent Communication & Retention": "lisa",
    "Candace – Case Manager & Progress Tracker": "candace",
    "Kareem – Wisdom & Mindset Coach": "kareem",
    "Dawn – Emotional Wellness & Clarity Coach": "dawn"
}

choice = st.selectbox("🤖 Select an Agent", list(agents.keys()))
st.markdown("---")
selected_module = agents[choice]

st.info(f"You have selected **{choice}**. Please wait while we load their interface.")
try:
    module = importlib.import_module(selected_module)
    module.run()
except:
    st.warning(f"🔧 {choice.split('–')[0]} is not available yet. Please ensure `{selected_module}.py` is in the directory.")
