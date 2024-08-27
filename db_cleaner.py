import os
import sqlite3

def listar_databases():
    database_folder = "databases/"
    print("Bancos de dados disponíveis:\n")
    databases = os.listdir(database_folder)
    for idx, db in enumerate(databases, 1):
        print(f"{idx}. {db}")
    print("")
    escolha = int(input("Escolha o número do banco de dados: "))
    if 1 <= escolha <= len(databases):
        return os.path.join(database_folder, databases[escolha - 1])
    else:
        print("Escolha inválida. Por favor, selecione um número válido.")
        return listar_databases()

def verificar_e_remover_hashes_vazios(db_path, opcao):
    # Conecta ao banco de dados
    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    # Busca todas as tabelas
    c.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = c.fetchall()

    # Itera sobre as tabelas
    for table in tables:
        table_name = table[0]
        # Preservar conteúdo da tabela 'links' se opção for 3
        if opcao != 3 and table_name == 'links':
            continue
        c.execute(f"SELECT * FROM {table_name};")
        rows = c.fetchall()
        # Verifica cada entrada na tabela
        for row in rows:
            hash_value = row[0]  # Assumindo que o campo 'hash' é o primeiro
            resume_value = row[1]  # Assumindo que o campo 'resume' é o segundo

            # Opção 1: Remover entradas com hashes vazios e resumes preenchidos
            if opcao == 1 and not hash_value and resume_value:
                c.execute(f"DELETE FROM {table_name} WHERE resume = ?;", (resume_value,))
                conn.commit()

            # Opção 2: Remover entradas com resumes vazios e hashes preenchidos
            elif opcao == 2 and not resume_value and hash_value:
                c.execute(f"DELETE FROM {table_name} WHERE hashes = ?;", (hash_value,))
                conn.commit()

            # Opção 3: Remover todas as entradas exceto na tabela 'links'
            elif opcao == 3 and table_name != 'links':
                c.execute(f"DELETE FROM {table_name};")
                conn.commit()

    # Fecha a conexão com o banco de dados
    conn.close()

# Função para mostrar as opções e executar a ação selecionada
def menu():
    print("\n\nSelecione uma opção:\n")
    print("1. Remover entradas com hashes vazios\n")
    print("2. Remover entradas com resumes vazios\n")
    print("3. Remover todas as entradas (exceto na tabela 'links')\n")
    opcao = int(input("Opção: "))
    return opcao

# Início do programa
def main():
    db_path = listar_databases()
    opcao = menu()
    verificar_e_remover_hashes_vazios(db_path, opcao)

# Execução do programa
if __name__ == "__main__":
    main()
