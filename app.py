import streamlit as st
import base64
from pathlib import Path

# Configuração da página com favicon personalizado
st.set_page_config(
    page_title="ChatBot Valcapelli - Viva numa boa!",
    page_icon="image.png",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Pegar API key dos secrets
api_key = st.secrets["API_KEY"]

# CSS personalizado inspirado no site Valcapelli
st.markdown("""
<style>
    /* Importar fonte */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');
    
    /* Reset e configurações gerais */
    * {
        font-family: 'Poppins', sans-serif;
    }
    
    /* Esconder elementos padrão do Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Background gradiente colorido */
    .stApp {
        background: linear-gradient(135deg, #8B5CF6 0%, #A855F7 25%, #EC4899 50%, #F97316 75%, #FBBF24 100%);
        background-size: 400% 400%;
        animation: gradientBG 15s ease infinite;
    }
    
    @keyframes gradientBG {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    /* Container principal */
    .main-container {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 24px;
        padding: 2rem;
        margin: 1rem auto;
        max-width: 1200px;
        box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.25);
    }
    
    /* Header estilizado */
    .header {
        text-align: center;
        padding: 1.5rem 0;
        margin-bottom: 1rem;
    }
    
    .header img {
        width: 120px;
        height: auto;
        margin-bottom: 1rem;
        filter: drop-shadow(0 4px 6px rgba(0, 0, 0, 0.1));
    }
    
    .header h1 {
        background: linear-gradient(135deg, #8B5CF6, #EC4899, #F97316);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-size: 2.5rem;
        font-weight: 700;
        margin: 0;
        text-shadow: none;
    }
    
    .header p {
        color: #6B7280;
        font-size: 1.1rem;
        margin-top: 0.5rem;
    }
    
    /* Slogan */
    .slogan {
        background: linear-gradient(135deg, #8B5CF6, #A855F7);
        color: white;
        padding: 1rem 2rem;
        border-radius: 50px;
        text-align: center;
        font-size: 1.2rem;
        font-weight: 500;
        margin: 1rem auto;
        max-width: 400px;
        box-shadow: 0 10px 25px rgba(139, 92, 246, 0.3);
    }
    
    /* Container do chat */
    .chat-container {
        background: white;
        border-radius: 16px;
        padding: 1rem;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
        border: 2px solid #E5E7EB;
    }
    
    /* Footer */
    .custom-footer {
        text-align: center;
        padding: 1.5rem;
        color: #9CA3AF;
        font-size: 0.9rem;
    }
    
    .custom-footer a {
        color: #8B5CF6;
        text-decoration: none;
        font-weight: 500;
    }
    
    .custom-footer a:hover {
        text-decoration: underline;
    }
    
    /* Cores decorativas */
    .color-dots {
        display: flex;
        justify-content: center;
        gap: 0.5rem;
        margin: 1rem 0;
    }
    
    .color-dot {
        width: 12px;
        height: 12px;
        border-radius: 50%;
        animation: pulse 2s ease-in-out infinite;
    }
    
    .dot-purple { background: #8B5CF6; animation-delay: 0s; }
    .dot-pink { background: #EC4899; animation-delay: 0.2s; }
    .dot-orange { background: #F97316; animation-delay: 0.4s; }
    .dot-yellow { background: #FBBF24; animation-delay: 0.6s; }
    .dot-green { background: #10B981; animation-delay: 0.8s; }
    .dot-blue { background: #3B82F6; animation-delay: 1s; }
    
    @keyframes pulse {
        0%, 100% { transform: scale(1); opacity: 1; }
        50% { transform: scale(1.2); opacity: 0.8; }
    }
    
    /* Responsividade */
    @media (max-width: 768px) {
        .header h1 {
            font-size: 1.8rem;
        }
        .main-container {
            margin: 0.5rem;
            padding: 1rem;
        }
    }
</style>
""", unsafe_allow_html=True)

# Função para converter imagem em base64
def get_image_base64(image_path):
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except:
        return None

# Obter logo em base64
logo_base64 = get_image_base64("image.png")
logo_html = f'<img src="data:image/png;base64,{logo_base64}" alt="Valcapelli Logo">' if logo_base64 else ''

# Layout principal
st.markdown(f"""
<div class="main-container">
    <div class="header">
        {logo_html}
        <h1>ChatBot Valcapelli</h1>
        <p>Seu assistente de bem-estar e autoconhecimento</p>
    </div>
    
    <div class="color-dots">
        <div class="color-dot dot-purple"></div>
        <div class="color-dot dot-pink"></div>
        <div class="color-dot dot-orange"></div>
        <div class="color-dot dot-yellow"></div>
        <div class="color-dot dot-green"></div>
        <div class="color-dot dot-blue"></div>
    </div>
    
    <div class="slogan">✨ Viva numa boa! ✨</div>
    
    <div class="chat-container">
""", unsafe_allow_html=True)

# Embed do chat Langflow
langflow_chat_html = f"""
<script
  src="https://cdn.jsdelivr.net/gh/logspace-ai/langflow-embedded-chat@v1.0.7/dist/build/static/js/bundle.min.js">
</script>
<langflow-chat
    window_title="ChatBot Valcapelli"
    flow_id="61a17804-9284-446d-8e60-3801aef9bb60"
    host_url="https://langflow.inovai.app"
    api_key="{api_key}"
    chat_trigger_style="position: relative; width: 100%; height: 600px;"
    chat_window_style="width: 100%; height: 100%; border-radius: 12px;">
</langflow-chat>
"""

st.components.v1.html(langflow_chat_html, height=650)

# Fechar container e adicionar footer
st.markdown("""
    </div>
    
    <div class="custom-footer">
        <p>Desenvolvido com 💜 | <a href="https://www.valcapelli.com" target="_blank">www.valcapelli.com</a></p>
        <p>Metafísica da Saúde • Cromoterapia • Bem-estar</p>
    </div>
</div>
""", unsafe_allow_html=True)
