from database.conexao import conectar

def testar_conexao():
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("SELECT @@VERSION")  # Apenas um comando simples para testar
        resultado = cursor.fetchone()
        print("Conexão bem-sucedida!")
        print("Versão do SQL Server:", resultado[0])
        conexao.close()
    except Exception as e:
        print("Erro ao conectar no banco de dados:")
        print(e)

if __name__ == "__main__":
    testar_conexao()