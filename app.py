import streamlit as st

st.set_page_config(
    page_title="AURA AI",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 AURA AI")

st.subheader("Assistente Inteligente de Comunicação")

st.success("Sistema iniciado com sucesso!")

st.write("---")

st.header("🎤 Escuta Inteligente")

st.info("Ainda não há nenhuma vocalização registrada.")

col1, col2 = st.columns(2)

with col1:
    if st.button("🎤 Iniciar Escuta"):
        st.write("Em desenvolvimento...")

with col2:
    if st.button("📚 Histórico"):
        st.write("Em desenvolvimento...")

st.write("---")

st.metric("Exemplos Gravados", 0)
st.metric("Precisão da IA", "0%")
