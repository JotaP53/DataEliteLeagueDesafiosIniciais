import os
import sqlite3
from datetime import datetime
import shutil

# Conectar ao banco de dados SQLite (cria se não existir)
conn = sqlite3.connect('arquivos.db')
cursor = conn.cursor()

# Criar a tabela de arquivos, se ainda não existir
cursor.execute('''
CREATE TABLE IF NOT EXISTS arquivos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    data_criacao TEXT NOT NULL,
    tipo_extensao TEXT NOT NULL,
    categoria TEXT NOT NULL
)
''')

# Criar a tabela de categorias, se ainda não existir
cursor.execute('''
CREATE TABLE IF NOT EXISTS categorias (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_categoria TEXT NOT NULL
)
''')

# Função para categorizar o arquivo com base na extensão
def categorizar_arquivo(extensao):
    if extensao in ['.txt', '.pdf', '.docx']:
        return 'Documentos'
    elif extensao in ['.jpg', '.png', '.gif']:
        return 'Imagens'
    elif extensao in ['.mp4', '.mkv']:
        return 'Vídeos'
    else:
        return 'Outros'

# Função para escanear uma pasta e organizar os arquivos
def organizar_arquivos(diretorio):
    for nome_arquivo in os.listdir(diretorio):
        caminho_arquivo = os.path.join(diretorio, nome_arquivo)
        
        # Verificar se é um arquivo e não uma pasta
        if os.path.isfile(caminho_arquivo):
            # Extrair informações do arquivo
            nome, extensao = os.path.splitext(nome_arquivo)
            data_criacao = datetime.fromtimestamp(os.path.getctime(caminho_arquivo)).strftime('%Y-%m-%d %H:%M:%S')
            categoria = categorizar_arquivo(extensao)

            # Inserir as informações no banco de dados
            cursor.execute('''
            INSERT INTO arquivos (nome, data_criacao, tipo_extensao, categoria)
            VALUES (?, ?, ?, ?)
            ''', (nome_arquivo, data_criacao, extensao, categoria))
            
            # Criar a pasta da categoria se ela não existir
            pasta_categoria = os.path.join(diretorio, categoria)
            if not os.path.exists(pasta_categoria):
                os.makedirs(pasta_categoria)
            
            # Mover o arquivo para a pasta da categoria
            shutil.move(caminho_arquivo, os.path.join(pasta_categoria, nome_arquivo))
    
    # Salvar as alterações no banco de dados
    conn.commit()

# Exemplo: Escanear e organizar arquivos na pasta "meus_arquivos"
organizar_arquivos("meus_arquivos")

# Função para gerar relatórios de consulta SQL
def gerar_relatorios():
    # Listar os arquivos mais recentes
    print("Arquivos mais recentes:")
    cursor.execute('SELECT * FROM arquivos ORDER BY data_criacao DESC LIMIT 10')
    for row in cursor.fetchall():
        print(row)

    # Mostrar a quantidade de arquivos por categoria
    print("\nQuantidade de arquivos por categoria:")
    cursor.execute('SELECT categoria, COUNT(*) FROM arquivos GROUP BY categoria')
    for row in cursor.fetchall():
        print(f"Categoria: {row[0]}, Quantidade: {row[1]}")

    # Extensões mais comuns no sistema
    print("\nExtensões mais comuns:")
    cursor.execute('SELECT tipo_extensao, COUNT(*) FROM arquivos GROUP BY tipo_extensao')
    for row in cursor.fetchall():
        print(f"Extensão: {row[0]}, Quantidade: {row[1]}")

# Exemplo: Gerar relatórios
gerar_relatorios()

# Fechar a conexão com o banco de dados
conn.close()
