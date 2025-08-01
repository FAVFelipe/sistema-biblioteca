from flask import Flask, request, jsonify
from flask_cors import CORS
import pyodbc
from datetime import datetime
from models.emprestimo import emprestimo_ja_existe

app = Flask(__name__)
CORS(app)

def parse_data(data_str):
    for fmt in ('%d/%m/%Y', '%d-%m-%Y'):
        try:
            return datetime.strptime(data_str, fmt)
        except ValueError:
            continue
    raise ValueError("Formato de data inválido. Use DD/MM/AAAA ou DD-MM-AAAA.")

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

    if not all([ra, codigo, retirada_str, entrega_str]):
        return jsonify({"erro": "Todos os campos são obrigatórios."}), 400

    try:
        # Verificação de duplicidade
        if emprestimo_ja_existe(int(ra), int(codigo)):
            return jsonify({"erro": "Este empréstimo já existe para este aluno e livro."}), 400

        data_retirada = datetime.strptime(retirada_str, "%d/%m/%Y")
        data_entrega = datetime.strptime(entrega_str, "%d/%m/%Y")

        if data_retirada > data_entrega:
            return jsonify({'erro': 'A data de retirada não pode ser maior que a data de entrega.'}), 400

        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute(
            "INSERT INTO Emprestimos (ra, codigo_livro, data_retirada, data_entrega) VALUES (?, ?, ?, ?)",
            (ra, codigo, data_retirada, data_entrega)
        )
        conexao.commit()
        return jsonify({"mensagem": "Empréstimo registrado com sucesso"}), 200

    except Exception as e:
        if "UQ_RA_LIVRO" in str(e):
            return jsonify({"erro": "Empréstimo já cadastrado para esse aluno e livro."}), 400
        return jsonify({"erro": "Erro ao registrar o empréstimo", "detalhes": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)