# QueryToExcel - Exportador de Grandes Consultas SQL

Este projeto é um script em Python desenhado para resolver o problema de exportar grandes volumes de dados (milhões de linhas) de um banco de dados SQL para arquivos Excel.

Ele contorna a limitação de \~1 milhão de linhas do Excel ao executar uma consulta SQL e dividir o resultado em "blocos" (chunks), salvando cada bloco em um arquivo `.xlsx` separado dentro de uma pasta de relatórios.

## 🚀 Funcionalidades Principais

  * **Conexão Flexível:** Conecta-se a qualquer banco de dados compatível com SQLAlchemy (Oracle, PostgreSQL, MySQL, SQLite, etc.) através de uma string de conexão.
  * **Query Dinâmica:** Permite que o usuário insira qualquer consulta SQL (simples ou complexa, com múltiplas linhas) diretamente no terminal no momento da execução.
  * **Tamanho de Bloco Configurável:** O usuário define dinamicamente quantas linhas deseja salvar em cada arquivo Excel.
  * **Processamento de Baixo Consumo de Memória:** Utiliza a função `chunksize` do Pandas para processar a consulta em pedaços, evitando o esgotamento da memória RAM, mesmo ao lidar com milhões de registros.
  * **Exportação Organizada:** Salva todos os arquivos Excel gerados (ex: `arquivo_1.xlsx`, `arquivo_2.xlsx`) em uma pasta dedicada criada automaticamente (`relatorios_excel`)

## 📋 Pré-requisitos

  * Python 3.8 ou superior
  * Acesso a um banco de dados SQL (Oracle, PostgreSQL, SQLite, etc.)

## 🛠️ Como Usar

### 1\. Preparação do Ambiente

Clone este repositório (ou baixe os arquivos) para um diretório local.

### 2\. Instalação

Instale todas as dependências necessárias listadas no `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 3\. Configuração da Conexão

Crie um arquivo chamado `.env` na raiz do projeto. Dentro dele, adicione sua string de conexão do SQLAlchemy:

```ini
# Exemplo para SQLite (usado nos testes)
DB_CONNECT="sqlite:///meu_banco.db"

# Exemplo para Oracle
# DB_CONNECT="oracle+oracledb://USUARIO:SENHA@HOST:PORTA/SERVICE_NAME"

# Exemplo para PostgreSQL
# DB_CONNECT="postgresql+psycopg2://USUARIO:SENHA@HOST:PORTA/NOME_DO_BANCO"
```

### 4\. Execução

Rode o script principal `main.py` a partir do seu terminal:

```bash
python main.py
```

O script irá solicitar três coisas:

1.  **A Conexão:** Ele tentará se conectar ao banco usando a string do `.env`.
2.  **A Query:** Você deve colar sua consulta SQL (pode ter múltiplas linhas). Pressione `Enter` em uma linha vazia para confirmar.
3.  **O Tamanho do Bloco:** Digite o número de linhas que você quer em cada arquivo Excel (ex: `1000000`).

O script então começará a processar e salvar os arquivos na pasta `relatorios_excel`.

## ⚙️ Estrutura do Projeto

```
.
├── .env                # (Arquivo local) Armazena a string de conexão do banco
├── .gitignore          # Configuração do Git para ignorar arquivos sensíveis e gerados
├── connection_db.py    # Módulo para criar e testar a conexão com o banco (Engine)
├── main.py             # Ponto de entrada principal do script. Coleta o input do usuário.
├── requirements.txt    # Lista de dependências do Python
└── sql_operations.py   # Módulo com a lógica principal de consulta e exportação
```