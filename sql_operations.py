import pandas as pd
from connection_db import database_connection
import os
import openpyxl
import time
from datetime import datetime

def convert_byte_to_hex(valor):
    if isinstance(valor, bytes):
        return valor.hex().upper()
    return valor

def search_and_save(query, engine_db, blocksize):
    output_folder = "relatorios_excel"

    os.makedirs(output_folder, exist_ok=True)
    print(f"Pasta '{output_folder}' criada para salvar os arquivos.")
    print("-"*60)

    block_counter = 0
    
    coluns_to_convert = []
    
    start_timer = time.time()

    try:
        for df_block in pd.read_sql_query(query, engine_db, chunksize=blocksize):
            block_counter +=  1
            print(f"Bloco {block_counter}") 
            print(f"Qnt linhas/colunas\n{df_block.shape}")
            
            # Verify a 
            if block_counter == 1:
                for col_name in df_block.select_dtypes(include=['object']).columns:
                    data_notnull = df_block[col_name].dropna()
                    
                    if not data_notnull.empty:
                        first_data = data_notnull.iloc[0]
                        
                        if isinstance(first_data, bytes):
                            coluns_to_convert.append(col_name)
            if not coluns_to_convert:
                print("Nenhuma coluna 'bytes' (RAW) detectada.")

            if coluns_to_convert:
                for colun in coluns_to_convert:
                    if colun in df_block.columns:
                        df_block[colun] = df_block[colun].apply(convert_byte_to_hex)
                    
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
        end_timer = time.time()
        final_time = end_timer-start_timer
        minutes = int(final_time // 60) 
        seconds = int(final_time % 60)
        print(f"Tempo total para a operação: {minutes} minutos e {seconds} segundos.")

    except Exception as e:
        print(f"Erro ao gerar a consulta\nMotivo:{e}")
        exit()