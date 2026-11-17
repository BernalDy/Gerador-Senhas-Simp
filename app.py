import secrets
import streamlit as st
import hashlib
import requests

minusculas = "abcdefghijklmnopqrstuvwxyz"
maiusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numeros = "0123456789"
simbolos = "!@#$%&*?"

def embaralhar(texto):
    caracteres = list(texto)
    secrets.SystemRandom().shuffle(caracteres)
    return "".join(caracteres)

def gerar_senha(tamanho, usar_maiusculas, usar_numeros, usar_simbolos):
    estoque = minusculas
    senha = secrets.choice(minusculas)
    if usar_maiusculas:
        estoque = estoque + maiusculas
        senha = senha + secrets.choice(maiusculas)
    if usar_numeros:
        estoque = estoque + numeros
        senha = senha + secrets.choice(numeros)
    if usar_simbolos:
        estoque = estoque + simbolos
        senha = senha + secrets.choice(simbolos)

    while len(senha) < tamanho:
        senha = senha + secrets.choice(estoque)
    return embaralhar(senha)

##Checando vazamento da senha 
def vezes_vazada(senha):
    hash_senha = hashlib.sha1(senha.encode("utf-8")).hexdigest().upper()
    prefixo = hash_senha[:5]
    resto = hash_senha[5:]

    endereco = "https://api.pwnedpasswords.com/range/" + prefixo
    resposta = requests.get(endereco, headers={"User-Agent": "gerador-de-senhas-estudo"})

    for linha in resposta.text.splitlines():
        sufixo, quantidade = linha.split(":")
        if sufixo == resto:
            return int(quantidade)
    return 0


st.title("Gerador de Senhas")
if "historico" not in st.session_state:
    st.session_state.historico = []

if "historico" not in st.session_state:
    st.session_state.historico = []
if "senha_atual" not in st.session_state:
    st.session_state.senha_atual = ""

st.warning("Demo online: use apenas senhas de teste. Para gerar ou verificar senhas reais, rode o app localmente (instruções no README).")  

tamanho = st.slider("Tamanho da senha", 5, 32, 8)
usar_maiusculas = st.checkbox("Letras maiúsculas", value=True)
usar_numeros = st.checkbox("Números", value=True)
usar_simbolos = st.checkbox("Símbolos", value=True)

if st.button("Gerar senha"):
    st.session_state.senha_atual = gerar_senha(tamanho, usar_maiusculas, usar_numeros, usar_simbolos)
    st.session_state.historico.append(st.session_state.senha_atual)

if st.session_state.senha_atual != "":
    st.code(st.session_state.senha_atual)

st.subheader("Últimas senhas geradas")
for item in st.session_state.historico[-5:]:
    st.code(item)

if st.button("Apagar histórico"):
    st.session_state.historico = []
    st.session_state.senha_atual = ""
    st.rerun()

st.subheader("Sua senha já vazou?")
senha_teste = st.text_input("Digite uma senha para testar", type="password")

if st.button("Verificar"):
    vezes = vezes_vazada(senha_teste)
    if vezes > 0:
        st.error(f"Essa senha apareceu {vezes} vezes em vazamentos. Não use.")
    else:
        st.success("Não encontrada em vazamentos conhecidos.")