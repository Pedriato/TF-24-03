from flask import Flask, request, jsonify
from models import get_db_connection  # Importa a conexão ao banco

app = Flask(__name__)

@app.route('/alunos', methods=['GET'])
def listar_alunos():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM alunos')
    alunos = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(alunos)

@app.route('/alunos', methods=['POST'])
def cadastrar_aluno():
    novo_aluno = request.json
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        'INSERT INTO alunos (aluno_id, nome, endereco, cidade, estado, cep, pais, telefone) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)',
        (novo_aluno['aluno_id'], novo_aluno['nome'], novo_aluno['endereco'], novo_aluno['cidade'], novo_aluno['estado'], novo_aluno['cep'], novo_aluno['pais'], novo_aluno['telefone'])
    )
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({'message': 'Aluno cadastrado com sucesso!'}), 201

@app.route('/alunos/<aluno_id>', methods=['PUT'])
def atualizar_aluno(aluno_id):
    dados_atualizados = request.json
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        'UPDATE alunos SET nome = %s, endereco = %s, cidade = %s, estado = %s, cep = %s, pais = %s, telefone = %s WHERE aluno_id = %s',
        (dados_atualizados['nome'], dados_atualizados['endereco'], dados_atualizados['cidade'], dados_atualizados['estado'],
         dados_atualizados['cep'], dados_atualizados['pais'], dados_atualizados['telefone'], aluno_id)
    )
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({'message': 'Aluno atualizado com sucesso!'})

@app.route('/alunos/<aluno_id>', methods=['DELETE'])
def excluir_aluno(aluno_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('DELETE FROM alunos WHERE aluno_id = %s', (aluno_id,))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({'message': 'Aluno excluído com sucesso!'})

def test_placeholder():
    assert 1 == 1


if __name__ == '__main__':
    app.run(debug=True)
