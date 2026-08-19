import pyodbc

# Connection string (fornecido na oficina)
CONNECTION_STRING = (
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=seu-servidor.database.windows.net;"
    "Database=seu-database;"
    "UID=seu_usuario;PWD=SenhaForte123!;"
    "Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30"
)

def get_connection():
    try:
        connection = pyodbc.connect(CONNECTION_STRING)
        print("✓ Conectado ao Azure SQL!")
        return connection
    except Exception as e:
        print(f"✗ Erro ao conectar: {e}")
        return None

def get_all_produtos():
    """Busca todos os produtos do banco"""
    connection = get_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Produtos")
        return cursor.fetchall()
    return []
