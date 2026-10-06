import streamlit as st
from openai import OpenAI

#Passo 1: Definindo o funcionamento do chat

#Definindo o Título
st.write("# Chatbot com IA")
#Verificar se existe uma sessão para armazenar as mensagens
if not "lista_mensagens" in st.session_state:
    st.session_state["lista_mensagens"] = []
#Input do chat em campo de mensagem
texto_usuario = st.chat_input("Pergunte qualquer coisa")
    # Conectar a API da openAI
Modelo_ia = OpenAI(api_key="[YOUR-GOOGLEAI-API-KEY]",base_url="https://generativelanguage.googleapis.com/v1beta/openai")
#Para cada mensagem enviada pelo usuário:
    #Loop para exibir as mensagens na tela
for mensagem in st.session_state["lista_mensagens"]:
    role = mensagem["role"]
    content = mensagem["content"]
    st.chat_message(role).write(content)
    # Mostrar a mensagem que o usuário enviou como "user"
if texto_usuario:
    print(texto_usuario)
    st.chat_message("user").write(texto_usuario)
    mensagem_usuario = {"role": "user", "content": texto_usuario}
    #Armazenar na lista mensagem
    st.session_state["lista_mensagens"].append(mensagem_usuario)
    #ia respondeu
    resposta_ia = Modelo_ia.chat.completions.create(messages=st.session_state["lista_mensagens"], model="gemini-3.1-flash-lite")
    print(resposta_ia)
    texto_resposta_ia = resposta_ia.choices[0].message.content

    st.chat_message("assistant").write(texto_resposta_ia)
    mensagem_ia = {"role": "assistant", "content": texto_resposta_ia}
    #Armazenar na lista mensagem
    st.session_state["lista_mensagens"].append(mensagem_ia)

print(st.session_state["lista_mensagens"])


#Usar o framework Streamlit para fazer o front e backend com Python
    # rodar com o comando streamlit run app.py
    # para interomper, ctrl+c

#Usar a IA da OpenAI
    #gerar uma chave no google AI Studio e colar no lugar de [YOUR-GOOGLEAI-API-KEY]
    # o model usado é "gemini-3.1-flash-lite" mas pode estar indisponível, se esse for o caso, verificar models disponíveis em: https://ai.google.dev/gemini-api/docs/openai?hl=pt-br

