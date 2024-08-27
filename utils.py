import sqlite3
import hashlib
from functools import wraps

def memoize_to_db_gpt4(table_name):
    def decorator(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            try:
                concatenated_args = "\n".join(map(str, args)) + "\n" + "\n".join(f"{k}={v}" for k, v in kwargs.items())
                arg_hash = hashlib.sha256(concatenated_args.encode("utf-8")).hexdigest()

                with sqlite3.connect(f'databases/{self.nome_banco}') as conn:
                    cursor = conn.cursor()
                    cursor.execute(f"SELECT resume_gpt4 FROM {table_name} WHERE hashes = ?", (arg_hash,))
                    row = cursor.fetchone()

                    if row:
                        print(f"Resultado encontrado no cache para hash {arg_hash}.")
                        return row[0]
                    else:
                        print(f"Resultado não encontrado no cache para hash {arg_hash}. Chamando a função original.")
                        result = func(self, *args, **kwargs)
                        if result is not None:
                            cursor.execute(f"INSERT INTO {table_name} (hashes, resume_gpt4) VALUES (?, ?)", (arg_hash, result))
                            conn.commit()
                return result
            except Exception as e:
                print(f"Erro ao memoizar para o banco de dados: {e}")
                return None
        return wrapper
    return decorator
