from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()

def database_connection():
    DB_STRING = os.getenv("DB_CONNECT")

    # Check if the DB_CONNECT variable is in the .env file and if it is empty.
    if not DB_STRING:
        print('ERRO: Variavel DB_CONNECT não foi encontrada ou está vazia, verifique no arquivo .env a string de conexão.')
        exit()
    print('String de conexão carregada, iniciando criação da engine')

    # Create the engine and test the connection string from the .env file.
    try:
        engine = create_engine(os.getenv('DB_CONNECT'))
        print('Engine criada')
    except Exception as e:
        print(f'Erro ao criar engine, verifique a string no arquivo .env\nErro: {e}')
        exit()

    # Confirm the connection to the database. If it fails, show the reason.
    try:
        with engine.connect() as connection:
            print("Conexão realizada no banco: ")
    except Exception as e:
        print("Não conectou meu bruxo :(\nMotivo: ",e)
        exit()

    return engine