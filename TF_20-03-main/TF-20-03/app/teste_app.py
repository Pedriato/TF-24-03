import pytest
from flask import Flask
from unittest.mock import patch, MagicMock
from models import get_db_connection

import sys
sys.path.insert(0, 'C:\\Users\\Administrador\\Desktop\\TF_20-03-main\\TF-20-03\\app')
from models import models



@pytest.fixture
def client():
    models.config['TESTING'] = True
    with models.test_client() as client:
        yield client

@patch('app.get_db_connection')
def test_listar_alunos(mock_get_db_connection, client):
    # Simulando o banco de dados
    mock_conn = MagicMock()
    mock_cursor = mock_conn.cursor.return_value
    mock_cursor.fetchall.return_value = [
        (1, 'João Silva', 'Rua A', 'Cidade X', 'Estado Y', '12345-678', 'Brasil', '123456789'),
        (2, 'Maria Oliveira', 'Rua B', 'Cidade Y', 'Estado Z', '87654-321', 'Brasil', '987654321')
    ]
    mock_get_db_connection.return_value = mock_conn

    response = client.get('/alunos')
    assert response.status_code == 200
    assert response.json == [
        [1, 'João Silva', 'Rua A', 'Cidade X', 'Estado Y', '12345-678', 'Brasil', '123456789'],
        [2, 'Maria Oliveira', 'Rua B', 'Cidade Y', 'Estado Z', '87654-321', 'Brasil', '987654321']
    ]

@patch('app.get_db_connection')
def test_cadastrar_aluno(mock_get_db_connection, client):
    mock_conn = MagicMock()
    mock_cursor = mock_conn.cursor.return_value
    mock_get_db_connection.return_value = mock_conn

    novo_aluno = {
        'aluno_id': 3,
        'nome': 'Carlos Ferreira',
        'endereco': 'Rua C',
        'cidade': 'Cidade Z',
        'estado': 'Estado W',
        'cep': '12312-312',
        'pais': 'Brasil',
        'telefone': '111222333'
    }

    response = client.post('/alunos', json=novo_aluno)
    assert response.status_code == 201
    assert response.json == {'message': 'Aluno cadastrado com sucesso!'}

    mock_cursor.execute.assert_called_once_with(
        'INSERT INTO alunos (aluno_id, nome, endereco, cidade, estado, cep, pais, telefone) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)',
        (3, 'Carlos Ferreira', 'Rua C', 'Cidade Z', 'Estado W', '12312-312', 'Brasil', '111222333')
    )

@patch('app.get_db_connection')
def test_atualizar_aluno(mock_get_db_connection, client):
    mock_conn = MagicMock()
    mock_cursor = mock_conn.cursor.return_value
    mock_get_db_connection.return_value = mock_conn

    dados_atualizados = {
        'nome': 'Carlos Atualizado',
        'endereco': 'Rua D',
        'cidade': 'Cidade W',
        'estado': 'Estado Q',
        'cep': '12312-123',
        'pais': 'Brasil',
        'telefone': '999888777'
    }

    response = client.put('/alunos/3', json=dados_atualizados)
    assert response.status_code == 200
    assert response.json == {'message': 'Aluno atualizado com sucesso!'}

    mock_cursor.execute.assert_called_once_with(
        'UPDATE alunos SET nome = %s, endereco = %s, cidade = %s, estado = %s, cep = %s, pais = %s, telefone = %s WHERE aluno_id = %s',
        ('Carlos Atualizado', 'Rua D', 'Cidade W', 'Estado Q', '12312-123', 'Brasil', '999888777', '3')
    )

@patch('app.get_db_connection')
def test_excluir_aluno(mock_get_db_connection, client):
    mock_conn = MagicMock()
    mock_cursor = mock_conn.cursor.return_value
    mock_get_db_connection.return_value = mock_conn

    response = client.delete('/alunos/3')
    assert response.status_code == 200
    assert response.json == {'message': 'Aluno excluído com sucesso!'}

    mock_cursor.execute.assert_called_once_with('DELETE FROM alunos WHERE aluno_id = %s', ('3',))

