import streamlit as st
from datetime import datetime

# Configuração da página
st.set_page_config(page_title="Cadastro de Aluno", layout="wide")


#sidebar para mudança de tela(opção de cadastro de aluno, cadastro de escola, consulta de aluno, acesso a material didático, acesso a provas, acesso a gabaritos)
st.sidebar.image("LOGO3_EVOLUTIVA.jpg", use_container_width=True)
st.sidebar.title("Menu")
st.sidebar.markdown("Escolha uma opção abaixo:")

#botões de navegação
if "page" not in st.session_state:
    st.session_state.page = "home"

if st.sidebar.button("Cadastro de Aluno", key="cadastro_aluno"):
    st.session_state.page = "cadastro_aluno"

if st.sidebar.button("Cadastro de Escola", key="cadastro_escola"):
    st.session_state.page = "cadastro_escola"

if st.sidebar.button("Consulta de Aluno", key="consulta_aluno"):
    st.session_state.page = "consulta_aluno"

if st.sidebar.button("Acesso a Material Didático", key="material_didatico"):
    st.session_state.page = "material_didatico"

if st.sidebar.button("Acesso a Provas", key="acesso_provas"):
    st.session_state.page = "acesso_provas"

if st.sidebar.button("Acesso a Gabaritos", key="acesso_gabaritos"):
    st.session_state.page = "acesso_gabaritos"

# Exibir o formulário apenas quando o botão "Cadastro de Aluno" for clicado
if st.session_state.page == "cadastro_aluno":
    # Título da página
    st.title("Cadastro de Aluno")
    # Campos de entrada
    with st.form("cadastro_form"):
        st.header("Informações do Aluno")
        
        col1, col2 = st.columns(2)

        with col1:
            # Nome
            nome = st.text_input("Nome do Aluno", placeholder="Digite o nome completo")

        with col2:
            # Data de Nascimento
            data_nascimento = st.date_input(
                "Data de Nascimento", 
                min_value=datetime(1900, 1, 1), 
                max_value=datetime.today(), 
                format="DD/MM/YYYY"
            )
        
        # Áreas de Conhecimento, Matérias e Série
        st.subheader("Áreas de Conhecimento")
        col1, col2, col3 = st.columns(3)

        with col1:
            areas_conhecimento = [
                "Selecione uma área",
                "Linguagens", 
                "Matemática", 
                "Ciências Humanas", 
                "Ciências Naturais", 
                "Ciências da Religião"
            ]
            area_selecionada = st.selectbox("Área de Conhecimento", options=areas_conhecimento)

        with col2:
            materia = [
                "Selecione uma matéria",
                "Português",
                "Inglês",
                "Arte",
                "Educação Física",
                "Espanhol",
                "Matemática",
                "História",
                "Geografia",
                "Ciências",
                "Religião"
            ]
            materia_selecionada = st.selectbox("Matéria", options=materia)
            

        with col3:
            serie = st.selectbox("Série", options=["1º Ano", "2º Ano", "3º Ano", "4º Ano", "5º Ano", "6º Ano", "7º Ano", "8º Ano", "9º Ano", "1º Ano Médio", "2º Ano Médio", "3º Ano Médio"])


            # Nome da Escola
        nome_escola = st.text_input("Nome da Escola", placeholder="Digite o nome da escola")

        col1, col2 = st.columns(2)

        with col1:
            # Zona Rural ou Urbana
            zona = st.radio("Localização da Escola", options=["Zona Urbana", "Zona Rural"])

        with col2:
            # Unidade da Prova
            unidade_prova = st.selectbox("Unidade da Prova", options="1ª Unidade, 2ª Unidade, 3ª Unidade, 4ª Unidade".split(", "))

        # Laudo
        st.subheader("Laudo Médico/Especialista")
        opcoes_laudo = [
            "Autismo", "TDAH", "TOD", "Esquizofrenia", "Deficiência Intelectual",
            "Baixa Acuidade Visual", "Surdocegueira", "Outros"
        ]
        laudo_selecionado = st.multiselect("Selecione as condições (se aplicável)", opcoes_laudo)
        outros_laudo = st.text_input("Outros (especificação)(se aplicável)", max_chars=100)
        # Questões
        st.subheader("Respostas das Questões")
        cols = st.columns(5)

        questoes = {}
        for i in range(1, 6):
            with cols[i - 1]:
                resposta = st.selectbox(
                    f"Questão {i}", options=["A", "B", "C", "D", "E"], key=f"q{i}"
                )
                questoes[f"Questão {i}"] = resposta

        cols = st.columns(5)

        for i in range(6, 11):
            with cols[i - 6]:
                resposta = st.selectbox(
                    f"Questão {i}", options=["A", "B", "C", "D", "E"], key=f"q{i}"
                )
                questoes[f"Questão {i}"] = resposta

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
                st.write(f"**Área de Conhecimento:** {area_selecionada}")
                st.write(f"**Matéria:** {materia_selecionada}")
                st.write(f"**Série:** {serie}")
                st.write(f"**Zona:** {zona}")
                st.write(f"**Nome da Escola:** {nome_escola}")
                st.write(f"**Data de Nascimento:** {data_nascimento.strftime('%d/%m/%Y')}")
                st.write(f"**Unidade da Prova:** {unidade_prova}")
                st.write(f"**Laudo Médico/Especialista:** {', '.join(laudo_selecionado) if laudo_selecionado else 'Nenhum'}")
                if "Outros" in laudo_selecionado and outros_laudo:
                    st.write(f"**Outros (especificação):** {outros_laudo}")
                st.write("### Respostas das Questões")
                for questao, resposta in questoes.items():
                    st.write(f"**{questao}:** {resposta}")