import pandas as pd
from connection_db import database_connection

engine_db = database_connection()

query = '''
    SELECT * FROM dados
'''

blocksize = 10_000
block_counter = 0

try:
    for df_block in pd.read_sql_query(query, engine_db, chunksize=blocksize):
        block_counter +=  1
        print(f"Bloco {block_counter}") 
        print(f"Formato linhas/ colunas:\n{df_block}")

        print("Amostra do bloco: ")
        print(df_block.head (2))

    print(f"Total blocos lidos: {block_counter}")

except Exception as e:
    print(f"Erro ao gerar a consulta\nMotivo:{e}")
    exit()