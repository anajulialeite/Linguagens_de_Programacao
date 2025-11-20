from flask_restful import Resource
from flask import Blueprint, request, jsonify, make_response
from marshmallow import ValidationError

from src.schemas.tarefa_schema import TarefaSchema
from src.entities import tarefa_entity
from src.services.tarefa_service import (
    cadastrar_tarefa,
    listar_tarefas_service,
    atualizar_tarefa_service,
    remover_tarefa_service
)
from src import api

# Instância do Blueprint
tarefa_bp = Blueprint('tarefa_bp', __name__, url_prefix='/tarefas')

# Instâncias dos Schemas
tarefa_schema = TarefaSchema()
tarefas_schema = TarefaSchema(many=True)

@tarefa_bp.route('/tarefa', methods=['POST'])
def criar_tarefa():
    data = request.get_json()
    nova_tarefa = cadastrar_tarefa(data)
    return tarefa_schema.jsonify(nova_tarefa), 201

@tarefa_bp.route('/tarefa', methods=['GET'])
def listar_tarefas():
    tarefas = listar_tarefas_service()
    return tarefas_schema.jsonify(tarefas), 200

@tarefa_bp.route('/tarefa/<int:id>', methods=['PUT'])
def atualizar_tarefa(id):
    data = request.get_json()
    tarefa_atualizada = atualizar_tarefa_service(id, data)
    return tarefa_schema.jsonify(tarefa_atualizada), 200

@tarefa_bp.route('/tarefa/<int:id>', methods=['DELETE'])
def remover_tarefa(id):
    remover_tarefa_service(id)
    return jsonify({"mensagem": "Tarefa removida com sucesso"}), 200
