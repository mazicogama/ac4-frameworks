from flask import Flask, request, jsonify
import sqlite3
import os

app = Flask(__name__)

@app.route('/dados', methods=['GET'])
def obter_dados():
    conn = sqlite3.connect('banco_de_dados.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tabela_dados")
    dados = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(dados)

@app.route('/dados', methods=['POST'])
def adicionar_dados():
    dados = request.get_json()

    conn = sqlite3.connect('banco_de_dados.db')
    cursor = conn.cursor()

    cursor.execute("INSERT INTO tabela_dados (coluna1, coluna2) VALUES (?, ?)", (dados['coluna1'], dados['coluna2']))
    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({'message': 'Dados adicionados com sucesso'})

if __name__ == '__main__':
    if not os.path.exists('banco_de_dados.db'):
        conn = sqlite3.connect('banco_de_dados.db')
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE tabela_dados (coluna1 TEXT, coluna2 TEXT)")
        cursor.close()
        conn.close()

    app.run()
