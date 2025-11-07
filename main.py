from connection_db import database_connection
from sql_operations import search_and_save

def main():
    # Import database_connection function from "connection_db.py"
    engine_db = database_connection()
    
    # Ask for query input.
    print("Cole a query que deseja pesquisar e pressione enter 2x")
    
    # Read multi-line input to prevent query from skipping subsequent prompts.
    query_lines = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        if line == "":
            break
        query_lines.append(line)
    query = " ".join(query_lines)

    # Handle the empty query case.
    if not query:
        print("Erro, nenhuma query foi adicionada.")
        exit()
    
    # Read the chunksize number and handle any invalid input.
    blocksize = input("Digite quantas linhas deseja salvar dentro do arquivo?: ")
    try:
        blocksize_int = int(blocksize)
        blocksize = blocksize_int
    except ValueError:
        print(f"Valor digitado não é valido.")
        exit()
    
    # Import search_and_save function from "sql_operations.py"
    search_and_save(query, engine_db, blocksize)

if __name__ == "__main__":
    main()
