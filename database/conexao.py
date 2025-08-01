import pyodbc

def conectar():
    return pyodbc.connect(
        "DRIVER={SQL Server};"
        "SERVER=FAVARETO\\SQLEXPRESS;"
        "DATABASE=BibliotecaDB;"
        "Trusted_Connection=yes;"
        "TrustServerCertificate=yes;"

    )