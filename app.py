import streamlit as st

st.set_page_config(
    page_title="ChatBot Valcapelli - Viva numa boa!",
    page_icon="💬",
    layout="wide"
)

st.title("💬ChatBot Valcapelli - Viva numa boa!")

# Pegar API key dos secrets
api_key = st.secrets["API_KEY"]

# Embed do chat Langflow
langflow_chat_html = f"""
<script
  src="https://cdn.jsdelivr.net/gh/logspace-ai/langflow-embedded-chat@v1.0.7/dist/build/static/js/bundle.min.js">
</script>
<langflow-chat
    window_title="Chat V3"
    flow_id="61a17804-9284-446d-8e60-3801aef9bb60"
    host_url="https://langflow.inovai.app"
    api_key="{api_key}">
</langflow-chat>
"""

st.components.v1.html(langflow_chat_html, height=700)
