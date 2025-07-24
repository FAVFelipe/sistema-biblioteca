from flask import Flask, request, jsonify
from flask_cors import CORS
import pyodbc
from datetime import datetime

app = Flask(__name__)
CORS(app)

def conectar():
    return pyodbc.connect(
        "DRIVER={SQL Server};"
        "SERVER=FAVARETO\\SQLEXPRESS;"
        "DATABASE=BibliotecaDB;"
        "Trusted_Connection=yes;"
        "TrustServerCertificate=yes;"
    )

@app.route("/emprestimo", methods=["POST"])
def emprestimo():
    dados = request.json
    ra = dados.get("ra")
    codigo = dados.get("codigo_livro")
    retirada_str = dados.get("data_retirada")
    entrega_str = dados.get("data_entrega")

    try:
        # Converte as datas de string ("23/07/2025") para datetime
        data_retirada = datetime.strptime(retirada_str, "%d/%m/%Y")
        data_entrega = datetime.strptime(entrega_str, "%d/%m/%Y")

        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute(
            "INSERT INTO Emprestimos (ra, codigo_livro, data_retirada, data_entrega) VALUES (?, ?, ?, ?)",
            (ra, codigo, data_retirada, data_entrega)
        )
        conexao.commit()
        return jsonify({"mensagem": "Empréstimo registrado com sucesso"}), 200

    except Exception as e:
        return jsonify({"erro": "Erro ao registrar o empréstimo", "detalhes": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)