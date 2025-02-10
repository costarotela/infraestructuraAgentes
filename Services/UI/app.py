import streamlit as st
from Core.models.agent_models import AgentConfig

def render_agent_creation():
    with st.form("agent_creation"):
        name = st.text_input("Nombre del Agente")
        capabilities = st.multiselect("Capacidades", ["Ventas", "Soporte", "Análisis"])
        submitted = st.form_submit_button("Crear")
        if submitted:
            return AgentConfig(name=name, capabilities=capabilities)

st.title("Creación de Agentes AI")
render_agent_creation()
