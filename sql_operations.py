import pandas as pd
from connection_db import database_connection
import os
import openpyxl

def search_and_save(query, engine_db, blocksize):
    output_folder = "relatorios_excel"

    os.makedirs(output_folder, exist_ok=True)
    print(f"Pasta '{output_folder}' criada para salvar os arquivos.")
    print("-"*60)

    block_counter = 0

    try:
        for df_block in pd.read_sql_query(query, engine_db, chunksize=blocksize):
            block_counter +=  1
            print(f"Bloco {block_counter}") 
            print(f"Qnt linhas/colunas\n{df_block.shape}")

            file_name = f"arquivo_{block_counter}.xlsx"
            file_path = os.path.join(output_folder, file_name)

            print(f"Salvando bloco {block_counter} na pasta {file_path}")

            df_block.to_excel(
                file_path,
                index=False,
                engine="openpyxl"
            )
            print(f"Bloco {block_counter} salvo sem erros!")
            print("-"*60)

        print(f"Processo Concluido!\nTotal blocos lidos: {block_counter}\nArquivos estão salvos na pasta {output_folder}")

    except Exception as e:
        print(f"Erro ao gerar a consulta\nMotivo:{e}")
        exit()