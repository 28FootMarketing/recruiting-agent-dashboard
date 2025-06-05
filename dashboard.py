import streamlit as st

st.set_page_config(page_title="Recruiting Agent Dashboard", layout="wide")

st.title("All-Star AI Support Team")
st.markdown("Switch between your specialized recruiting agents below.")

agent_options = {
    "🏀 Jordan – The Closer": "https://agentjordan.streamlit.app",
    "🎯 Kobe – The Mamba Mentor": "https://agentkobe.streamlit.app",
    "🔥 Maya – The Motivator": "https://agentmaya.streamlit.app",
    "🔍 Magic – The Opportunity Connector": "https://agentmagic.streamlit.app",
    "📣 Lisa – Parent Communication & Retention": "https://agentlisa.streamlit.app",
    "📞 Candace – Direct Contact Support": "https://agentcandace.streamlit.app",
    "🧠 Kareem – Mindset & Growth Strategist": "https://agentkareem.streamlit.app",
    "🌅 Dawn – The Emotional Reset Bot": "https://agentdawn.streamlit.app"
}

selected_agent = st.selectbox("Select an Agent", list(agent_options.keys()))

if selected_agent:
    st.markdown(f"### Launching: {selected_agent}")
    st.markdown(f"[Click here to open]({agent_options[selected_agent]})", unsafe_allow_html=True)
