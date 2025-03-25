import streamlit as st
from datetime import datetime

# Configuração da página
st.set_page_config(page_title="Cadastro de Aluno", layout="wide")

# Título da página
st.title("Cadastro de Aluno")

# Campos de entrada
with st.form("cadastro_form"):
    st.header("Informações do Aluno")
    
    # Nome
    nome = st.text_input("Nome do Aluno", placeholder="Digite o nome completo")
    
    # Áreas de Conhecimento
    st.subheader("Áreas de Conhecimento")
    areas_conhecimento = {
        "Linguagens": ["Português", "Inglês", "Arte", "Educação Física", "Espanhol"],
        "Matemática": [],
        "Ciências Humanas": ["História", "Geografia"],
        "Ciências Naturais": ["Ciências"],
        "Ciências da Religião": ["Religião"]
    }
    areas_selecionadas = {}
    for area, subareas in areas_conhecimento.items():
        if subareas:
            areas_selecionadas[area] = st.multiselect(area, subareas)
        else:
            areas_selecionadas[area] = st.checkbox(area)
        # Série
    serie = st.selectbox("Série", options=["1º ano", "2º ano", "3º ano", "4º ano", "5º ano", "6º ano", "7º ano", "8º ano", "9º ano", "Ensino Médio"])

        # Zona Rural ou Urbana
    zona = st.radio("Localização da Escola", options=["Zona Urbana", "Zona Rural"])

        # Nome da Escola
    nome_escola = st.text_input("Nome da Escola", placeholder="Digite o nome da escola")

        # Data de Nascimento
    data_nascimento = st.date_input(
        "Data de Nascimento", 
        min_value=datetime(1900, 1, 1), 
        max_value=datetime.today(), 
        format="DD/MM/YYYY"
    )

    # Unidade da Prova
    unidade_prova = st.text_input("Unidade da Prova", placeholder="Digite a unidade da prova")

    # Laudo
    st.subheader("Laudo Médico/Especialista")
    opcoes_laudo = [
        "Autismo", "TDAH", "TOD", "Esquizofrenia", "Deficiência Intelectual",
        "Baixa Acuidade Visual", "Surdocegueira", "Outros"
    ]
    laudo_selecionado = st.multiselect("Selecione as condições (se aplicável)", opcoes_laudo)
    if "Outros" in laudo_selecionado:
        outros_laudo = st.text_input("Especifique 'Outros'", placeholder="Descreva a condição")

    # Botão de envio
    submitted = st.form_submit_button("Enviar")

    # Processamento do formulário
    if submitted:
        # Verifica se todos os campos obrigatórios foram preenchidos
        if not nome or not serie or not zona or not nome_escola or not unidade_prova:
            st.error("Por favor, preencha todos os campos obrigatórios.")
        else:
            st.success("Formulário enviado com sucesso!")
            st.write("### Resumo do Cadastro")
            st.write(f"**Nome:** {nome}")
            st.write(f"**Áreas de Conhecimento Selecionadas:**")
            for area, subareas in areas_selecionadas.items():
                if isinstance(subareas, list):
                    st.write(f"- {area}: {', '.join(subareas) if subareas else 'Nenhuma selecionada'}")
                else:
                    st.write(f"- {area}: {'Sim' if subareas else 'Não'}")
            st.write(f"**Série:** {serie}")
            st.write(f"**Zona:** {zona}")
            st.write(f"**Nome da Escola:** {nome_escola}")
            st.write(f"**Data de Nascimento:** {data_nascimento.strftime('%d/%m/%Y')}")
            st.write(f"**Unidade da Prova:** {unidade_prova}")
            st.write(f"**Laudo Médico/Especialista:** {', '.join(laudo_selecionado) if laudo_selecionado else 'Nenhum'}")
            if "Outros" in laudo_selecionado and outros_laudo:
                st.write(f"**Outros (especificação):** {outros_laudo}")