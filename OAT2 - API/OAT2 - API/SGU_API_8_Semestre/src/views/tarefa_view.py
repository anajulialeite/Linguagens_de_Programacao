from flask_restful import Resource
from marshmallow import ValidationError
from flask import request, jsonify, make_response
from src.schemas import tarefa_schema
from src.models.tarefa_model import TarefaModel
from src.services import tarefa_service, usuario_service
from src import api


class TarefaList(Resource):
    def get(self):
        tarefas = tarefa_service.listar_tarefa()
        if not tarefas:
            return make_response(jsonify({"message": "Nenhuma tarefa encontrada"}), 404)

        schema = tarefa_schema.TarefaSchema(many=True)
        return make_response(jsonify(schema.dump(tarefas)), 200)

    def post(self):
        schema = tarefa_schema.TarefaSchema()
        try:
            dados = schema.load(request.json)
        except ValidationError as err:
            return make_response(jsonify(err.messages), 400)

        # valida o usuario_id
        if not usuario_service.listar_usuario_id(dados['usuario_id']):
            return make_response(jsonify({"message": "Usuário não encontrado"}), 404)

        nova_tarefa = TarefaModel(
            titulo=dados['titulo'],
            descricao=dados['descricao'],
            usuario_id=dados['usuario_id']
        )

        resultado = tarefa_service.cadastrar_tarefa(nova_tarefa)
        return make_response(jsonify(schema.dump(resultado)), 201)


api.add_resource(TarefaList, '/tarefa')


class TarefaResource(Resource):
    def get(self, id_tarefa):
        tarefa = tarefa_service.listar_tarefa_id(id_tarefa)
        if tarefa:
            schema = tarefa_schema.TarefaSchema()
            return make_response(jsonify(schema.dump(tarefa)), 200)

        return make_response(jsonify({"message": "Tarefa não encontrada"}), 404)

    def put(self, id_tarefa):
        schema = tarefa_schema.TarefaSchema()
        try:
            dados = schema.load(request.json)
        except ValidationError as err:
            return make_response(jsonify(err.messages), 400)

        # valida o usuário_id na edição
        if not usuario_service.listar_usuario_id(dados['usuario_id']):
            return make_response(jsonify({"message": "Usuário não encontrado"}), 404)

        tarefa_editada = tarefa_service.editar_tarefa(id_tarefa, dados)
        if tarefa_editada:
            return make_response(jsonify(schema.dump(tarefa_editada)), 200)

        return make_response(jsonify({"message": "Tarefa não encontrada"}), 404)

    def delete(self, id_tarefa):
        if tarefa_service.excluir_tarefa(id_tarefa):
            return make_response(jsonify({"message": "Tarefa excluída com sucesso"}), 200)

        return make_response(jsonify({"message": "Tarefa não encontrada"}), 404)


api.add_resource(TarefaResource, '/tarefa/<int:id_tarefa>')
