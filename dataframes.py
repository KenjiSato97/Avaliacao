import pandas as pd
import numpy as np
from datetime import datetime
import random
import string

def create_dataframes():
    """
    Cria e retorna os dataframes necessários para o sistema de avaliação escolar:
    - df_aluno: Informações dos alunos
    - df_escola: Cadastro de escolas
    - df_prova: Registros de provas realizadas pelos alunos
    - df_gabarito: Gabaritos das provas por série/matéria
    """
    
    # Criação do df_escola (fazemos primeiro para referenciar nas outras tabelas)
    escolas = [
        {"id_escola": 1, "nomeEscola": "Escola Municipal Paulo Freire", 
         "endereco": "Rua das Flores, 123", "telefone": "(11) 3456-7890", "email": "paulofreire@edu.com"},
        {"id_escola": 2, "nomeEscola": "Colégio Estadual Machado de Assis", 
         "endereco": "Av. Principal, 456", "telefone": "(11) 2345-6789", "email": "machadodeassis@edu.com"},
        {"id_escola": 3, "nomeEscola": "Instituto Educacional Monteiro Lobato", 
         "endereco": "Rua dos Pinheiros, 789", "telefone": "(11) 3456-5678", "email": "monteirolobato@edu.com"}
    ]
    df_escola = pd.DataFrame(escolas)
    
    # Criação do df_aluno
    alunos = []
    series = ['1º ano', '2º ano', '3º ano', '4º ano', '5º ano']
    generos = ['Masculino', 'Feminino']
    localizacoes = ['Urbana', 'Rural', 'Periférica']
    
    for i in range(1, 51):  # Criar 50 alunos
        id_escola = random.randint(1, 3)
        escola_info = next(escola for escola in escolas if escola["id_escola"] == id_escola)
        
        aluno = {
            "id_aluno": i,
            "nomeAluno": f"Aluno {i}",
            "dataNascimento": f"{random.randint(2010, 2016)}-{random.randint(1, 12):02d}-{random.randint(1, 28):02d}",
            "genero": random.choice(generos),
            "serie": random.choice(series),
            "nomeEscola": escola_info["nomeEscola"],
            "localizacaoEscola": random.choice(localizacoes),
            "laudoMedico": random.choice([True, False, False, False])  # 25% de chance de ter laudo
        }
        alunos.append(aluno)
    
    df_aluno = pd.DataFrame(alunos)
    
    # Criação do df_prova
    provas = []
    materias = ['Português', 'Matemática', 'Ciências', 'História', 'Geografia']
    
    for aluno in alunos:
        # Cada aluno faz entre 1 e 3 provas
        for _ in range(random.randint(1, 3)):
            materia = random.choice(materias)
            
            prova = {
                "id_prova": len(provas) + 1,
                "id_aluno": aluno["id_aluno"],
                "nomeAluno": aluno["nomeAluno"],
                "materia": materia,
                "serie": aluno["serie"]
            }
            
            # Adicionar respostas às questões (de 1 a 10)
            for i in range(1, 11):
                prova[f"questao_{i}"] = random.choice(['A', 'B', 'C', 'D', ''])
            
            provas.append(prova)
    
    df_prova = pd.DataFrame(provas)
    
    # Criação do df_gabarito
    gabaritos = []
    
    # Um gabarito para cada combinação de série e matéria
    for serie in series:
        for materia in materias:
            gabarito = {
                "id_gabarito": len(gabaritos) + 1,
                "serie": serie,
                "materia": materia
            }
            
            # Definir respostas corretas para as questões de 1 a 10
            for i in range(1, 11):
                gabarito[f"questao_{i}"] = random.choice(['A', 'B', 'C', 'D'])
            
            gabaritos.append(gabarito)
    
    df_gabarito = pd.DataFrame(gabaritos)
    
    return {
        'df_aluno': df_aluno,
        'df_escola': df_escola,
        'df_prova': df_prova,
        'df_gabarito': df_gabarito
    }

def load_or_create_dataframes():
    """
    Tenta carregar os dataframes de arquivos existentes,
    se não existirem, cria novos dataframes.
    """
    try:
        df_aluno = pd.read_parquet('data/df_aluno.parquet')
        df_escola = pd.read_parquet('data/df_escola.parquet')
        df_prova = pd.read_parquet('data/df_prova.parquet')
        df_gabarito = pd.read_parquet('data/df_gabarito.parquet')
        
        return {
            'df_aluno': df_aluno,
            'df_escola': df_escola,
            'df_prova': df_prova,
            'df_gabarito': df_gabarito
        }
    
    except (FileNotFoundError, Exception):
        # Se os arquivos não existirem, cria novos dataframes
        return create_dataframes()

def save_dataframes(dataframes):
    """
    Salva os dataframes em arquivos parquet para uso futuro.
    
    Args:
        dataframes (dict): Dicionário contendo os dataframes
    """
    import os
    
    # Criar pasta data se não existir
    if not os.path.exists('data'):
        os.makedirs('data')
    
    # Salvar cada dataframe
    for name, df in dataframes.items():
        df.to_parquet(f'data/{name}.parquet')
    
    print("Dataframes salvos com sucesso!")

def calcular_resultado_prova(df_prova, df_gabarito):
    """
    Calcula o resultado de cada prova comparando com o gabarito correspondente.
    
    Args:
        df_prova: DataFrame com as respostas dos alunos
        df_gabarito: DataFrame com os gabaritos das provas
    
    Returns:
        DataFrame com os resultados das provas
    """
    # Criar uma cópia do df_prova para adicionar os resultados
    df_resultado = df_prova.copy()
    df_resultado['pontuacao'] = 0  # Inicializar coluna de pontuação
    
    # Para cada prova
    for idx, prova in df_prova.iterrows():
        # Encontrar o gabarito correspondente
        gabarito = df_gabarito[(df_gabarito['serie'] == prova['serie']) & 
                               (df_gabarito['materia'] == prova['materia'])]
        
        if not gabarito.empty:
            gabarito = gabarito.iloc[0]  # Pegar o primeiro gabarito encontrado
            
            # Comparar as respostas e calcular a pontuação
            pontuacao = 0
            for i in range(1, 11):
                questao = f'questao_{i}'
                # Verificar se a resposta do aluno não está vazia e corresponde ao gabarito
                if prova[questao] and prova[questao] == gabarito[questao]:
                    pontuacao += 1
                    
            # Atualizar a pontuação na cópia do dataframe
            df_resultado.at[idx, 'pontuacao'] = pontuacao
            
    return df_resultado

# Exemplo de uso
if __name__ == "__main__":
    # Criar ou carregar dataframes
    dfs = load_or_create_dataframes()
    
    # Exemplo de acesso aos dataframes
    df_aluno = dfs['df_aluno']
    df_escola = dfs['df_escola']
    df_prova = dfs['df_prova']
    df_gabarito = dfs['df_gabarito']
    
    # Exemplo de cálculo de resultados
    df_resultados = calcular_resultado_prova(df_prova, df_gabarito)
    
    # Salvar dataframes para uso futuro
    save_dataframes(dfs)