import os
import mysql.connector
from mysql.connector import Error
import math

def save_sql(data):
    
    host = os.getenv("HOST_MYSQL")
    user = os.getenv("USUARIO_MYSQL")
    password = os.getenv("SENHA_MYSQL")
    database = os.getenv("BANCO_MYSQL")
    tabela = os.getenv("TABELA_MYSQL")
    
    try:
        conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
            )
        cursor = conn.cursor()

        todas_colunas = set()
        for d in data:
            for k in d.keys():
                if k is None or (isinstance(k, float) and math.isnan(k)) or str(k).lower() == 'nan':
                    continue  
                todas_colunas.add(str(k).strip())
        todas_colunas = sorted(todas_colunas)

        colunas_sql = ', '.join([f'`{col}` TEXT' for col in todas_colunas])
        cursor.execute(f"CREATE TABLE IF NOT EXISTS `{tabela}` ({colunas_sql})")

        for dado in data:
            values = []
            for col in todas_colunas:
                val = dado.get(col, None)
                if isinstance(val, float) and math.isnan(val):
                    val = None
                values.append(val)

            placeholders = ', '.join(['%s'] * len(values))
            colunas_formatadas = ', '.join([f'`{col}`' for col in todas_colunas])
            cursor.execute(
                f"INSERT INTO `{tabela}` ({colunas_formatadas}) VALUES ({placeholders})",
                values
            )
    
        print( 
              f"Dados salvos na tabela '{tabela}' do banco de dados '{database}' com sucesso."
        )
        
        conn.commit()

    except Error as e:
        raise e

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()