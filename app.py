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

# Esconder TUDO do Streamlit e fazer iframe ocupar tela toda
st.markdown("""
<style>
    #MainMenu, footer, header, .stApp > header, div[data-testid="stHeader"], 
    section[data-testid="stSidebar"], div[data-testid="stDecoration"] {
        display: none !important;
        visibility: hidden !important;
    }
    
    html, body, .stApp, [data-testid="stAppViewContainer"], 
    .main, .block-container, .stMainBlockContainer,
    [data-testid="stVerticalBlock"], [data-testid="element-container"] {
        padding: 0 !important;
        margin: 0 !important;
        max-width: 100% !important;
        width: 100% !important;
        height: 100vh !important;
        overflow: hidden !important;
        background: transparent !important;
    }
    
    .stApp {
        background: linear-gradient(135deg, #8B5CF6 0%, #A855F7 25%, #EC4899 50%, #F97316 75%, #FBBF24 100%) !important;
        background-size: 400% 400% !important;
        animation: gradientBG 15s ease infinite !important;
    }
    
    @keyframes gradientBG {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    iframe {
        border: none !important;
        width: 100% !important;
        height: 100vh !important;
        position: fixed !important;
        top: 0 !important;
        left: 0 !important;
    }
    
    .element-container {
        width: 100% !important;
        height: 100vh !important;
    }
</style>
""", unsafe_allow_html=True)

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
        
        html, body {{
            height: 100%;
            overflow: hidden;
        }}
        
        body {{
            background: linear-gradient(135deg, #8B5CF6 0%, #A855F7 25%, #EC4899 50%, #F97316 75%, #FBBF24 100%);
            background-size: 400% 400%;
            animation: gradientBG 15s ease infinite;
            height: 100%;
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
            padding: 15px;
            flex-shrink: 0;
        }}
        
        .header img {{
            width: 60px;
            height: auto;
            margin-bottom: 5px;
            filter: drop-shadow(0 4px 8px rgba(0,0,0,0.3));
        }}
        
        .header h1 {{
            color: white;
            font-size: 1.5rem;
            font-weight: 700;
            text-shadow: 0 2px 10px rgba(0,0,0,0.3);
        }}
        
        .header p {{
            color: rgba(255,255,255,0.9);
            font-size: 0.85rem;
        }}
        
        .color-dots {{
            display: flex;
            justify-content: center;
            gap: 6px;
            margin: 8px 0;
        }}
        
        .color-dot {{
            width: 8px;
            height: 8px;
            border-radius: 50%;
            animation: pulse 2s ease-in-out infinite;
        }}
        
        .dot-purple {{ background: white; animation-delay: 0s; }}
        .dot-pink {{ background: #FBBF24; animation-delay: 0.2s; }}
        .dot-orange {{ background: #10B981; animation-delay: 0.4s; }}
        .dot-yellow {{ background: #3B82F6; animation-delay: 0.6s; }}
        .dot-green {{ background: #EC4899; animation-delay: 0.8s; }}
        .dot-blue {{ background: white; animation-delay: 1s; }}
        
        @keyframes pulse {{
            0%, 100% {{ transform: scale(1); opacity: 0.8; }}
            50% {{ transform: scale(1.4); opacity: 1; }}
        }}
        
        .chat-wrapper {{
            flex: 1;
            display: flex;
            justify-content: center;
            padding: 0 15px 15px 15px;
            min-height: 0;
        }}
        
        .chat-container {{
            background: white;
            border-radius: 20px;
            width: 100%;
            max-width: 800px;
            box-shadow: 0 25px 50px rgba(0,0,0,0.3);
            overflow: hidden;
            display: flex;
            flex-direction: column;
        }}
        
        .chat-header {{
            background: linear-gradient(135deg, #8B5CF6, #A855F7);
            color: white;
            padding: 12px 20px;
            font-weight: 600;
            font-size: 1rem;
            display: flex;
            align-items: center;
            gap: 10px;
            flex-shrink: 0;
        }}
        
        .chat-header-icon {{
            width: 32px;
            height: 32px;
            background: white;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            flex-shrink: 0;
        }}
        
        .chat-header-icon img {{
            width: 22px;
            height: 22px;
        }}
        
        .chat-body {{
            flex: 1;
            display: flex;
            flex-direction: column;
            min-height: 0;
            position: relative;
        }}
        
        #chat-area {{
            flex: 1;
            overflow-y: auto;
            padding: 20px;
            display: flex;
            flex-direction: column;
            gap: 15px;
        }}
        
        .welcome-message {{
            background: linear-gradient(135deg, #F3E8FF, #FCE7F3);
            border-radius: 15px;
            padding: 20px;
            text-align: center;
        }}
        
        .welcome-message h3 {{
            color: #8B5CF6;
            margin-bottom: 10px;
        }}
        
        .welcome-message p {{
            color: #6B7280;
            font-size: 0.9rem;
        }}
        
        .message {{
            max-width: 80%;
            padding: 12px 16px;
            border-radius: 18px;
            font-size: 0.95rem;
            line-height: 1.4;
        }}
        
        .message.user {{
            background: linear-gradient(135deg, #8B5CF6, #A855F7);
            color: white;
            align-self: flex-end;
            border-bottom-right-radius: 4px;
        }}
        
        .message.bot {{
            background: #F3F4F6;
            color: #374151;
            align-self: flex-start;
            border-bottom-left-radius: 4px;
        }}
        
        .input-area {{
            padding: 15px 20px;
            border-top: 1px solid #E5E7EB;
            display: flex;
            gap: 10px;
            flex-shrink: 0;
            background: white;
        }}
        
        #user-input {{
            flex: 1;
            padding: 12px 18px;
            border: 2px solid #E5E7EB;
            border-radius: 25px;
            font-size: 0.95rem;
            outline: none;
            transition: border-color 0.3s;
        }}
        
        #user-input:focus {{
            border-color: #8B5CF6;
        }}
        
        #send-btn {{
            background: linear-gradient(135deg, #8B5CF6, #A855F7);
            color: white;
            border: none;
            border-radius: 50%;
            width: 48px;
            height: 48px;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: transform 0.2s, box-shadow 0.2s;
        }}
        
        #send-btn:hover {{
            transform: scale(1.05);
            box-shadow: 0 5px 15px rgba(139, 92, 246, 0.4);
        }}
        
        #send-btn svg {{
            width: 20px;
            height: 20px;
        }}
        
        .typing {{
            display: flex;
            gap: 4px;
            padding: 12px 16px;
            background: #F3F4F6;
            border-radius: 18px;
            align-self: flex-start;
            border-bottom-left-radius: 4px;
        }}
        
        .typing span {{
            width: 8px;
            height: 8px;
            background: #9CA3AF;
            border-radius: 50%;
            animation: typing 1.4s infinite;
        }}
        
        .typing span:nth-child(2) {{ animation-delay: 0.2s; }}
        .typing span:nth-child(3) {{ animation-delay: 0.4s; }}
        
        @keyframes typing {{
            0%, 100% {{ transform: translateY(0); }}
            50% {{ transform: translateY(-5px); }}
        }}
        
        .footer {{
            text-align: center;
            padding: 10px;
            color: rgba(255,255,255,0.9);
            font-size: 0.75rem;
            flex-shrink: 0;
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
                <div id="chat-area">
                    <div class="welcome-message">
                        <h3>Olá! Bem-vindo(a)! 👋</h3>
                        <p>Sou o assistente virtual do Valcapelli. Como posso ajudar você hoje?</p>
                    </div>
                </div>
                <div class="input-area">
                    <input type="text" id="user-input" placeholder="Digite sua mensagem..." autocomplete="off">
                    <button id="send-btn">
                        <svg fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 19l9 2-9-18-9 18 9-2zm0 0v-8"/>
                        </svg>
                    </button>
                </div>
            </div>
        </div>
    </div>
    
    <div class="footer">
        <a href="https://www.valcapelli.com" target="_blank">www.valcapelli.com</a> • Metafísica da Saúde • Cromoterapia
    </div>
    
    <script>
        const chatArea = document.getElementById('chat-area');
        const userInput = document.getElementById('user-input');
        const sendBtn = document.getElementById('send-btn');
        const API_KEY = "{api_key}";
        const FLOW_ID = "61a17804-9284-446d-8e60-3801aef9bb60";
        const HOST_URL = "https://langflow.inovai.app";
        
        function addMessage(text, isUser) {{
            const msg = document.createElement('div');
            msg.className = 'message ' + (isUser ? 'user' : 'bot');
            msg.textContent = text;
            chatArea.appendChild(msg);
            chatArea.scrollTop = chatArea.scrollHeight;
        }}
        
        function showTyping() {{
            const typing = document.createElement('div');
            typing.className = 'typing';
            typing.id = 'typing-indicator';
            typing.innerHTML = '<span></span><span></span><span></span>';
            chatArea.appendChild(typing);
            chatArea.scrollTop = chatArea.scrollHeight;
        }}
        
        function hideTyping() {{
            const typing = document.getElementById('typing-indicator');
            if (typing) typing.remove();
        }}
        
        async function sendMessage() {{
            const text = userInput.value.trim();
            if (!text) return;
            
            addMessage(text, true);
            userInput.value = '';
            showTyping();
            
            try {{
                const response = await fetch(HOST_URL + '/api/v1/run/' + FLOW_ID, {{
                    method: 'POST',
                    headers: {{
                        'Content-Type': 'application/json',
                        'x-api-key': API_KEY
                    }},
                    body: JSON.stringify({{
                        input_value: text,
                        output_type: 'chat',
                        input_type: 'chat'
                    }})
                }});
                
                const data = await response.json();
                hideTyping();
                
                let botResponse = 'Desculpe, não consegui processar sua mensagem.';
                if (data.outputs && data.outputs[0] && data.outputs[0].outputs && data.outputs[0].outputs[0]) {{
                    const output = data.outputs[0].outputs[0];
                    if (output.results && output.results.message && output.results.message.text) {{
                        botResponse = output.results.message.text;
                    }} else if (output.messages && output.messages[0] && output.messages[0].message) {{
                        botResponse = output.messages[0].message;
                    }} else if (output.artifacts && output.artifacts.message) {{
                        botResponse = output.artifacts.message;
                    }}
                }}
                
                addMessage(botResponse, false);
            }} catch (error) {{
                hideTyping();
                addMessage('Ops! Ocorreu um erro. Tente novamente.', false);
                console.error(error);
            }}
        }}
        
        sendBtn.addEventListener('click', sendMessage);
        userInput.addEventListener('keypress', (e) => {{
            if (e.key === 'Enter') sendMessage();
        }});
        
        userInput.focus();
    </script>
</body>
</html>
"""

# Renderizar página completa - altura grande para preencher tela
st.components.v1.html(full_page_html, height=2000, scrolling=False)
