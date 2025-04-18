import streamlit as st
from datetime import datetime
from dataframes import load_or_create_dataframes, save_dataframes

# Configuração da página
st.set_page_config(page_title="Plataforma de Avaliação Pedagógica Municipal", layout="wide")
with open("styles.css") as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Cabeçalho para mudança de tela (opção de cadastro de aluno, cadastro de escola, consulta de aluno, acesso a material didático, acesso a provas, acesso a gabaritos)

# Botões de navegação
if "page" not in st.session_state:
    st.session_state.page = "home"

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    with st.expander("Cadastro", expanded=False): 
        st.write("Selecione uma das opções abaixo:")
        if st.button("Aluno", key="cadastro_aluno", use_container_width=True):
            st.session_state.page = "cadastro_aluno"
        if st.button("Escola", key="cadastro_escola", use_container_width=True): 
            st.session_state.page = "cadastro_escola"
        if st.button("Prova", key="cadastro_prova", use_container_width=True):
            st.session_state.page = "cadastro_prova"

with col2:
    with st.expander("Consulta", expanded=False): 
        st.write("Selecione uma das opções abaixo:")
        if st.button("Escola", key="consulta_escola", use_container_width=True):
            st.session_state.page = "consulta_escola"
        if st.button("Série", key="consulta_serie", use_container_width=True): 
            st.session_state.page = "consulta_serie"
        if st.button("Disciplina", key="consulta_disciplina", use_container_width=True):
            st.session_state.page = "consulta_disciplina"
        if st.button("Zona", key="consulta_zona", use_container_width=True):
            st.session_state.page = "consulta_zona"
        if st.button("Gênero", key="consulta_genero", use_container_width=True):
            st.session_state.page = "consulta_genero"
        if st.button("Aluno", key="consulta_aluno", use_container_width=True):
            st.session_state.page = "consulta_aluno"

with col3:
    with st.expander("Material Didático", expanded=False):
        st.write("Selecione uma das opções abaixo:")
        if st.button("E-books", key="material_ebooks", use_container_width=True):
            st.session_state.page = "material_ebooks"
        if st.button("Vídeos", key="material_videos", use_container_width=True):
            st.session_state.page = "material_videos"
        if st.button("Exercícios Práticos", key="material_exercicios", use_container_width=True):
            st.session_state.page = "material_exercicios"

with col4:
    with st.expander("Pedagógico", expanded=False):
        st.write("Selecione uma das opções abaixo:")
        if st.button("Cronograma", key="pedagogico_cronograma", use_container_width=True):
            st.session_state.page = "pedagogico_cronograma"
        if st.button("Conteúdo Programático", key="pedagogico_conteudo", use_container_width=True):
            st.session_state.page = "pedagogico_conteudo"

with col5:
    with st.expander("Acesso", expanded=False):
        st.write("Selecione uma das opções abaixo:")
        if st.button("Gestor", key="acesso_gestor", use_container_width=True):
            st.session_state.page = "acesso_gestor"
        if st.button("Professor", key="acesso_professor", use_container_width=True):
            st.session_state.page = "acesso_professor"
        if st.button("Aluno", key="acesso_aluno", use_container_width=True):
            st.session_state.page = "acesso_aluno"
        if st.button("Secretário", key="acesso_secretario", use_container_width=True):
            st.session_state.page = "acesso_secretario"
        if st.button("Prefeito", key="acesso_prefeito", use_container_width=True):
            st.session_state.page = "acesso_prefeito"

if st.session_state.page == "home":
    st.title("Plataforma de Avaliação Pedagógica Municipal")
    st.write("""
    1. Conhecimento  
    2. Pensamento Científico, Crítico e Criativo  
    3. Repertório Cultural  
    4. Comunicação  
    5. Cultura Digital  
    6. Trabalho e Projeto de Vida  
    7. Argumentação  
    8. Autoconhecimento e Autocuidado  
    9. Empatia e Cooperação  
    10. Responsabilidade e Cidadania
    """)

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

        col1, col2 = st.columns(2)
        with col1:
        # Gênero
            genero = st.selectbox("Gênero", options=["Selecione o gênero", "Masculino", "Feminino"])
        with col2:
            serie = st.selectbox("Série", options=["Selecione uma série", "1º Ano", "2º Ano", "3º Ano", "4º Ano", "5º Ano", "6º Ano", "7º Ano", "8º Ano", "9º Ano", "1º Ano Médio", "2º Ano    Médio", "3º Ano Médio"])

        # Nome da Escola
        nome_escola = st.text_input("Nome da Escola", placeholder="Digite o nome da escola")

        col1, col2 = st.columns(2)

        with col1:
            # Zona Rural ou Urbana
            zona = st.radio("Localização da Escola", options=["Zona Urbana", "Zona Rural"])

        # Laudo
        st.subheader("Laudo Médico/Especialista")
        opcoes_laudo = [
            "Autismo", "TDAH", "TOD", "Esquizofrenia", "Deficiência Intelectual",
            "Baixa Acuidade Visual", "Surdocegueira", "Outros"
        ]
        laudo_selecionado = st.multiselect("Selecione as condições (se aplicável)", opcoes_laudo)
        outros_laudo = st.text_input("Outros (especificação)(se aplicável)", max_chars=100)

        # Botão de envio
        submitted = st.form_submit_button("Enviar")

        # Processamento do formulário
        if submitted:
            # Verifica se todos os campos obrigatórios foram preenchidos
            if not nome or genero == "Selecione o gênero" or serie == "Selecione uma série" or not zona or not nome_escola:
                st.error("Por favor, preencha todos os campos obrigatórios.")
            else:
                st.success("Formulário enviado com sucesso!")
                st.write("### Resumo do Cadastro")
                st.write(f"**Nome:** {nome}")
                st.write(f"**Gênero:** {genero}")
                st.write(f"**Série:** {serie}")
                st.write(f"**Zona:** {zona}")
                st.write(f"**Nome da Escola:** {nome_escola}")
                st.write(f"**Data de Nascimento:** {data_nascimento.strftime('%d/%m/%Y')}")
                st.write(f"**Laudo Médico/Especialista:** {', '.join(laudo_selecionado) if laudo_selecionado else 'Nenhum'}")
                if "Outros" in laudo_selecionado and outros_laudo:
                    st.write(f"**Outros (especificação):** {outros_laudo}")

if st.session_state.page == "cadastro_escola":
    st.title("Cadastro de Escola")
    st.write("Esta página é para o cadastro de escolas.")
    # Adicione aqui o código para o cadastro de escolas
    # Esta seção pode incluir campos como Nome da Escola, Endereço, Telefone, Email, etc.
    # Além disso, pode haver validações e um botão para salvar as informações no banco de dados.
    # Exemplo de campos:
    with st.form("cadastro_escola_form"):
        nome_escola = st.text_input("Nome da Escola", placeholder="Digite o nome da escola")
        endereco = st.text_input("Endereço", placeholder="Digite o endereço da escola")
        telefone = st.text_input("Telefone", placeholder="Digite o telefone da escola")
        email = st.text_input("Email", placeholder="Digite o email da escola")
        
        submitted = st.form_submit_button("Enviar")
        
        if submitted:
            if not nome_escola or not endereco or not telefone or not email:
                st.error("Por favor, preencha todos os campos obrigatórios.")
            else:
                st.success("Cadastro de Escola enviado com sucesso!")
                st.write(f"**Nome da Escola:** {nome_escola}")
                st.write(f"**Endereço:** {endereco}")
                st.write(f"**Telefone:** {telefone}")
                st.write(f"**Email:** {email}")

if st.session_state.page == "cadastro_prova":
    st.title("Cadastro de Prova")
    # Nome do Aluno
    st.subheader("Nome do Aluno")
    nome_aluno = st.text_input("Nome do Aluno", placeholder="Digite o nome completo")
    # Área de Conhecimento e Matéria
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
        serie_prova = st.selectbox("Série", options=["Selecione uma série", "1º Ano", "2º Ano", "3º Ano", "4º Ano", "5º Ano", "6º Ano", "7º Ano", "8º Ano", "9º Ano", "1º Ano Médio", "2º Ano Médio", "3º Ano Médio"])
            
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
    submitted = st.button("Enviar Respostas")

    if submitted:
        # Verifica se o nome do aluno foi preenchido
        if not nome_aluno or materia_selecionada == "Selecione uma matéria" or  area_selecionada == "Selecione uma área" or serie_prova == "Selecione uma série":
           st.error("Por favor, preencha todos os campos obrigatórios.")
        else:  
            st.success("Respostas enviadas com sucesso!")
            st.write("### Resumo do Cadastro")
            st.write(f"**Nome do Aluno:** {nome_aluno}")
            st.write(f"**Área de Conhecimento:** {area_selecionada}")
            st.write(f"**Matéria:** {materia_selecionada}")
            st.write(f"**Série:** {serie_prova}")
            for questao, resposta in questoes.items():
                st.write(f"**{questao}:** {resposta}")




if st.session_state.page == "consulta_aluno":
    st.title("Consulta de Aluno")
    st.write("Esta página é para a consulta de alunos.")
    # Adicione aqui o código para a consulta de alunos
    # Esta seção pode incluir campos como Nome do Aluno, Data de Nascimento, etc.
    # Além disso, pode haver validações e um botão para buscar as informações no banco de dados.
    # Exemplo de campos:
    with st.form("consulta_aluno_form"):
        nome_aluno = st.text_input("Nome do Aluno", placeholder="Digite o nome completo")
        data_nascimento = st.date_input(
            "Data de Nascimento", 
            min_value=datetime(1900, 1, 1), 
            max_value=datetime.today(), 
            format="DD/MM/YYYY"
        )
        
        submitted = st.form_submit_button("Consultar")
        
        if submitted:
            if not nome_aluno or not data_nascimento:
                st.error("Por favor, preencha todos os campos obrigatórios.")
            else:
                st.success("Consulta realizada com sucesso!")
                st.write(f"**Nome do Aluno:** {nome_aluno}")
                st.write(f"**Data de Nascimento:** {data_nascimento.strftime('%d/%m/%Y')}")

if st.session_state.page == "consulta_escola":
    st.title("Consulta de Escola")
    st.write("Esta página é para a consulta de escolas.")
    # Adicione aqui o código para a consulta de escolas
    # Esta seção pode incluir campos como Nome da Escola, Endereço, Telefone, Email, etc.
    # Além disso, pode haver validações e um botão para buscar as informações no banco de dados.
    # Exemplo de campos:
    with st.form("consulta_escola_form"):
        nome_escola = st.text_input("Nome da Escola", placeholder="Digite o nome da escola")
        
        submitted = st.form_submit_button("Consultar")
        
        if submitted:
            if not nome_escola:
                st.error("Por favor, preencha o campo obrigatório.")
            else:
                st.success("Consulta de Escola realizada com sucesso!")
                st.write(f"**Nome da Escola:** {nome_escola}")

if st.session_state.page == "consulta_serie":
    st.title("Consulta de Série")
    st.write("Esta página é para a consulta de séries.")
    # Adicione aqui o código para a consulta de séries
    # Esta seção pode incluir campos como Nome da Série, Ano, etc.
    # Além disso, pode haver validações e um botão para buscar as informações no banco de dados.
    # Exemplo de campos:
    with st.form("consulta_serie_form"):
        nome_serie = st.selectbox("Série", options=["Selecione uma série", "1º Ano", "2º Ano", "3º Ano", "4º Ano", "5º Ano", "6º Ano", "7º Ano", "8º Ano", "9º Ano", "1º Ano Médio", "2º Ano Médio", "3º Ano Médio"])
        
        submitted = st.form_submit_button("Consultar")
        
        if submitted:
            if not nome_serie:
                st.error("Por favor, preencha o campo obrigatório.")
            else:
                st.success("Consulta de Série realizada com sucesso!")
                st.write(f"**Nome da Série:** {nome_serie}")

if st.session_state.page == "consulta_disciplina":
    st.title("Consulta de Disciplina")
    st.write("Esta página é para a consulta de disciplinas.")
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
    with st.form("consulta_disciplina_form"):
        nome_disciplina = materia_selecionada = st.selectbox("Matéria", options=materia)
        submitted = st.form_submit_button("Consultar")
        if submitted:
            if not nome_disciplina:
                st.error("Por favor, preencha o campo obrigatório.")
            else:
                st.success("Consulta de Disciplina realizada com sucesso!")
                st.write(f"**Nome da Disciplina:** {nome_disciplina}")

if st.session_state.page == "consulta_zona":
    st.title("Consulta de Zona")
    st.write("Esta página é para a consulta de zonas.")
    # Adicione aqui o código para a consulta de zonas
    # Esta seção pode incluir campos como Zona Rural ou Urbana, Nome da Escola, etc.
    # Além disso, pode haver validações e um botão para buscar as informações no banco de dados.
    # Exemplo de campos:
    with st.form("consulta_zona_form"):
        zona = st.radio("Localização da Escola", options=["Zona Urbana", "Zona Rural"])
        
        submitted = st.form_submit_button("Consultar")
        
        if submitted:
            if not zona:
                st.error("Por favor, preencha o campo obrigatório.")
            else:
                st.success("Consulta de Zona realizada com sucesso!")
                st.write(f"**Localização da Escola:** {zona}")

if st.session_state.page == "consulta_genero":
    st.title("Consulta de Gênero")
    st.write("Esta página é para a consulta de gêneros.")
    # Adicione aqui o código para a consulta de gêneros
    # Esta seção pode incluir campos como Gênero, Nome da Escola, etc.
    # Além disso, pode haver validações e um botão para buscar as informações no banco de dados.
    # Exemplo de campos:
    with st.form("consulta_genero_form"):
        genero = st.selectbox("Gênero", options=["Selecione o gênero", "Masculino", "Feminino"])
        
        submitted = st.form_submit_button("Consultar")
        
        if submitted:
            if not genero:
                st.error("Por favor, preencha o campo obrigatório.")
            else:
                st.success("Consulta de Gênero realizada com sucesso!")
                st.write(f"**Gênero:** {genero}")                

if st.session_state.page == "material_ebooks":
    st.title("Material Didático - E-books")
    st.write("Esta página é para o acesso a E-books.")
    # Adicione aqui o código para o acesso a E-books
    # Esta seção pode incluir links ou arquivos para download de E-books.

if st.session_state.page == "material_videos":
    st.title("Material Didático - Vídeos")
    st.write("Esta página é para o acesso a vídeos.")

if st.session_state.page == "material_exercicios":
    st.title("Material Didático - Exercícios Práticos")
    st.write("Esta página é para o acesso a exercícios práticos.")
    # Adicione aqui o código para o acesso a exercícios práticos
    # Esta seção pode incluir links ou arquivos para download de exercícios práticos.

if st.session_state.page == "pedagogico_cronograma":
    st.title("Cronograma Pedagógico")
    st.write("Esta página é para o acesso ao cronograma pedagógico.")
    # Adicione aqui o código para o acesso ao cronograma pedagógico
    # Esta seção pode incluir links ou arquivos para download do cronograma pedagógico.

if st.session_state.page == "pedagogico_conteudo":
    st.title("Conteúdo Programático")
    st.write("Esta página é para o acesso ao conteúdo programático.")
    # Adicione aqui o código para o acesso ao conteúdo programático
    # Esta seção pode incluir links ou arquivos para download do conteúdo programático.

if st.session_state.page == "acesso_gestor":
    st.title("Acesso - Gestor")
    st.write("Esta página é para o login do gestor.")
    # Adicione aqui o código para o acesso do gestor
    with st.form("login_gestor_form"):
        username = st.text_input("Usuário", placeholder="Digite seu usuário")
        password = st.text_input("Senha", type="password", placeholder="Digite sua senha")
        
        submitted = st.form_submit_button("Entrar")
        
        if submitted:
            if not username or not password:
                st.error("Por favor, preencha todos os campos obrigatórios.")
            else:
                # Aqui você pode adicionar a lógica de autenticação
                # Exemplo: verificar usuário e senha em um banco de dados
                if username == "gestor" and password == "1234":  # Exemplo de validação simples
                    st.success("Login realizado com sucesso!")
                    st.write(f"Bem-vindo, {username}!")
                else:
                    st.error("Usuário ou senha inválidos.")
    # Esta seção pode incluir informações ou links relevantes para o gestor.

if st.session_state.page == "acesso_professor":
    st.title("Acesso - Professor")
    st.write("Esta página é para o login do professor.")
    # Adicione aqui o código para o acesso do professor
    with st.form("login_professor_form"):
        username = st.text_input("Usuário", placeholder="Digite seu usuário")
        password = st.text_input("Senha", type="password", placeholder="Digite sua senha")
        
        submitted = st.form_submit_button("Entrar")
        
        if submitted:
            if not username or not password:
                st.error("Por favor, preencha todos os campos obrigatórios.")
            else:
                # Aqui você pode adicionar a lógica de autenticação
                # Exemplo: verificar usuário e senha em um banco de dados
                if username == "professor" and password == "1234":  # Exemplo de validação simples
                    st.success("Login realizado com sucesso!")
                    st.write(f"Bem-vindo, {username}!")
                else:
                    st.error("Usuário ou senha inválidos.")
    # Esta seção pode incluir informações ou links relevantes para o professor.

if st.session_state.page == "acesso_aluno":
    st.title("Acesso - Aluno")
    st.write("Esta página é para o login do aluno.")    
    # Adicione aqui o código para o acesso do aluno
    with st.form("login_aluno_form"):
        username = st.text_input("Usuário", placeholder="Digite seu usuário")
        password = st.text_input("Senha", type="password", placeholder="Digite sua senha")
        
        submitted = st.form_submit_button("Entrar")
        
        if submitted:
            if not username or not password:
                st.error("Por favor, preencha todos os campos obrigatórios.")
            else:
                # Aqui você pode adicionar a lógica de autenticação
                # Exemplo: verificar usuário e senha em um banco de dados
                if username == "aluno" and password == "1234":  # Exemplo de validação simples
                    st.success("Login realizado com sucesso!")
                    st.write(f"Bem-vindo, {username}!")
                else:
                    st.error("Usuário ou senha inválidos.")
    # Esta seção pode incluir informações ou links relevantes para o aluno.

if st.session_state.page == "acesso_secretario":
    st.title("Acesso - Secretário")
    st.write("Esta página é para o login do secretário.")
    # Adicione aqui o código para o acesso do secretário
    with st.form("login_secretario_form"):
        username = st.text_input("Usuário", placeholder="Digite seu usuário")
        password = st.text_input("Senha", type="password", placeholder="Digite sua senha")
        
        submitted = st.form_submit_button("Entrar")
        
        if submitted:
            if not username or not password:
                st.error("Por favor, preencha todos os campos obrigatórios.")
            else:
                # Aqui você pode adicionar a lógica de autenticação
                # Exemplo: verificar usuário e senha em um banco de dados
                if username == "secretario" and password == "1234":  # Exemplo de validação simples
                    st.success("Login realizado com sucesso!")
                    st.write(f"Bem-vindo, {username}!")
                else:
                    st.error("Usuário ou senha inválidos.")
    # Esta seção pode incluir informações ou links relevantes para o secretário.

if st.session_state.page == "acesso_prefeito":
    st.title("Acesso - Prefeito")
    st.write("Esta página é para o login do prefeito.")
    # Adicione aqui o código para o acesso do prefeito
    with st.form("login_prefeito_form"):
        username = st.text_input("Usuário", placeholder="Digite seu usuário")
        password = st.text_input("Senha", type="password", placeholder="Digite sua senha")
        
        submitted = st.form_submit_button("Entrar")
        
        if submitted:
            if not username or not password:
                st.error("Por favor, preencha todos os campos obrigatórios.")
            else:
                # Aqui você pode adicionar a lógica de autenticação
                # Exemplo: verificar usuário e senha em um banco de dados
                if username == "prefeito" and password == "1234":
                    st.success("Login realizado com sucesso!")
                    st.write(f"Bem-vindo, {username}!")
                else:
                    st.error("Usuário ou senha inválidos.")
    # Esta seção pode incluir informações ou links relevantes para o prefeito.
