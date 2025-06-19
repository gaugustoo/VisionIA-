# 🤖 VisionIA — Assistente Virtual com OpenAI + Flask

VisionIA é um chatbot inteligente desenvolvido em Python usando Flask, OpenAI e Twilio.  
Com interface web e integração opcional com WhatsApp, ele responde mensagens com base em inteligência artificial de linguagem.

---

## 🔥 Demonstração

🖥️ Interface web simples e funcional:  
![print da interface](static/background.jpg)

🌐 Deploy disponível em:  
[`https://visionia.onrender.com`](https://visionia.onrender.com) <!-- substitua com seu link real -->

---

## 🚀 Funcionalidades

- [x] Chatbot com IA usando OpenAI GPT
- [x] Integração web via Flask
- [x] Interface com HTML + CSS
- [x] Envio de mensagens via WhatsApp (Twilio)
- [x] Respostas inteligentes via API
- [x] Pronto para deploy em Render ou Replit

---

## 💻 Como rodar localmente

```bash
# Clone o projeto
git clone https://github.com/seu-usuario/visionia.git
cd visionia

# (Opcional) Crie ambiente virtual
python -m venv venv
source venv/bin/activate   # ou venv\Scripts\activate no Windows

# Instale as dependências
pip install -r requirements.txt

# Rode o servidor
python app.py