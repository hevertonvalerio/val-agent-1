import streamlit as st
import base64

# Configuração da página com favicon personalizado
st.set_page_config(
    page_title="ChatBot Valcapelli - Viva numa boa!",
    page_icon="image.png",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Pegar API key dos secrets
api_key = st.secrets["API_KEY"]

# Função para converter imagem em base64
def get_image_base64(image_path):
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except:
        return None

# Obter logo em base64
logo_base64 = get_image_base64("image.png")

# CSS + HTML + Chat tudo em um único componente
full_page_html = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Poppins', sans-serif;
        }}
        
        body {{
            background: linear-gradient(135deg, #8B5CF6 0%, #A855F7 25%, #EC4899 50%, #F97316 75%, #FBBF24 100%);
            background-size: 400% 400%;
            animation: gradientBG 15s ease infinite;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
        }}
        
        @keyframes gradientBG {{
            0% {{ background-position: 0% 50%; }}
            50% {{ background-position: 100% 50%; }}
            100% {{ background-position: 0% 50%; }}
        }}
        
        .header {{
            text-align: center;
            padding: 20px;
            background: rgba(255,255,255,0.95);
            border-radius: 0 0 30px 30px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        }}
        
        .header img {{
            width: 80px;
            height: auto;
            margin-bottom: 10px;
        }}
        
        .header h1 {{
            background: linear-gradient(135deg, #8B5CF6, #EC4899, #F97316);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            font-size: 1.8rem;
            font-weight: 700;
        }}
        
        .header p {{
            color: #6B7280;
            font-size: 0.9rem;
        }}
        
        .color-dots {{
            display: flex;
            justify-content: center;
            gap: 8px;
            margin: 10px 0;
        }}
        
        .color-dot {{
            width: 10px;
            height: 10px;
            border-radius: 50%;
            animation: pulse 2s ease-in-out infinite;
        }}
        
        .dot-purple {{ background: #8B5CF6; animation-delay: 0s; }}
        .dot-pink {{ background: #EC4899; animation-delay: 0.2s; }}
        .dot-orange {{ background: #F97316; animation-delay: 0.4s; }}
        .dot-yellow {{ background: #FBBF24; animation-delay: 0.6s; }}
        .dot-green {{ background: #10B981; animation-delay: 0.8s; }}
        .dot-blue {{ background: #3B82F6; animation-delay: 1s; }}
        
        @keyframes pulse {{
            0%, 100% {{ transform: scale(1); }}
            50% {{ transform: scale(1.3); }}
        }}
        
        .chat-wrapper {{
            flex: 1;
            display: flex;
            justify-content: center;
            align-items: stretch;
            padding: 20px;
            min-height: 500px;
        }}
        
        .chat-container {{
            background: white;
            border-radius: 20px;
            width: 100%;
            max-width: 900px;
            box-shadow: 0 25px 50px rgba(0,0,0,0.3);
            overflow: hidden;
            display: flex;
            flex-direction: column;
        }}
        
        .chat-header {{
            background: linear-gradient(135deg, #8B5CF6, #A855F7);
            color: white;
            padding: 15px 20px;
            font-weight: 600;
            font-size: 1.1rem;
            display: flex;
            align-items: center;
            gap: 10px;
        }}
        
        .chat-header-icon {{
            width: 35px;
            height: 35px;
            background: white;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
        }}
        
        .chat-header-icon img {{
            width: 25px;
            height: 25px;
        }}
        
        .chat-body {{
            flex: 1;
            padding: 0;
            min-height: 450px;
        }}
        
        langflow-chat {{
            display: block;
            width: 100%;
            height: 100%;
        }}
        
        .footer {{
            text-align: center;
            padding: 15px;
            color: white;
            font-size: 0.85rem;
            text-shadow: 0 2px 4px rgba(0,0,0,0.3);
        }}
        
        .footer a {{
            color: white;
            text-decoration: underline;
        }}
    </style>
</head>
<body>
    <div class="header">
        <img src="data:image/png;base64,{logo_base64}" alt="Logo">
        <h1>ChatBot Valcapelli</h1>
        <p>Seu assistente de bem-estar e autoconhecimento</p>
        <div class="color-dots">
            <div class="color-dot dot-purple"></div>
            <div class="color-dot dot-pink"></div>
            <div class="color-dot dot-orange"></div>
            <div class="color-dot dot-yellow"></div>
            <div class="color-dot dot-green"></div>
            <div class="color-dot dot-blue"></div>
        </div>
    </div>
    
    <div class="chat-wrapper">
        <div class="chat-container">
            <div class="chat-header">
                <div class="chat-header-icon">
                    <img src="data:image/png;base64,{logo_base64}" alt="Logo">
                </div>
                <span>✨ Viva numa boa! - Converse comigo</span>
            </div>
            <div class="chat-body">
                <script src="https://cdn.jsdelivr.net/gh/logspace-ai/langflow-embedded-chat@v1.0.7/dist/build/static/js/bundle.min.js"></script>
                <langflow-chat
                    window_title="ChatBot Valcapelli"
                    flow_id="61a17804-9284-446d-8e60-3801aef9bb60"
                    host_url="https://langflow.inovai.app"
                    api_key="{api_key}"
                    online="true"
                    open_on_load="true"
                    height="100%">
                </langflow-chat>
            </div>
        </div>
    </div>
    
    <div class="footer">
        <p>Desenvolvido com 💜 | <a href="https://www.valcapelli.com" target="_blank">www.valcapelli.com</a></p>
        <p>Metafísica da Saúde • Cromoterapia • Bem-estar</p>
    </div>
</body>
</html>
"""

# Esconder elementos do Streamlit
st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stApp > header {display: none;}
    .block-container {padding: 0 !important; max-width: 100% !important;}
    iframe {border: none !important;}
</style>
""", unsafe_allow_html=True)

# Renderizar página completa
st.components.v1.html(full_page_html, height=800, scrolling=False)
