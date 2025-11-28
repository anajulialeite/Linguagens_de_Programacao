from flask_restful import Resource
from marshmallow import ValidationError
from flask import request, jsonify, make_response
from src.schemas import usuario_schema
from src.models.usuario_model import UsuarioModel
from src.services import usuario_service


class UsuarioList(Resource):
    def get(self):
        usuarios = usuario_service.listar_usuario()
        if not usuarios:
            return make_response(jsonify({"message": "Nenhum usuário encontrado"}), 404)

        schema = usuario_schema.UsuarioSchema(many=True)
        return make_response(jsonify(schema.dump(usuarios)), 200)

    def post(self):
        schema = usuario_schema.UsuarioSchema()
        try:
            dados = schema.load(request.json)
        except ValidationError as err:
            return make_response(jsonify(err.messages), 400)

        # impede emails duplicados
        if usuario_service.listar_usuario_email(dados['email']):
            return make_response(jsonify({"message": "Email já cadastrado"}), 400)

        novo_usuario = UsuarioModel(
            nome=dados['nome'],
            email=dados['email'],
            senha=dados['senha']
        )
        novo_usuario.gen_senha(dados['senha'])

        resultado = usuario_service.cadastrar_usuario(novo_usuario)
        return make_response(jsonify(schema.dump(resultado)), 201)


class UsuarioResource(Resource):
    def get(self, id_usuario):
        usuario = usuario_service.listar_usuario_id(id_usuario)
        if usuario:
            schema = usuario_schema.UsuarioSchema()
            return make_response(jsonify(schema.dump(usuario)), 200)

        return make_response(jsonify({"message": "Usuário não encontrado"}), 404)

    def put(self, id_usuario):
        schema = usuario_schema.UsuarioSchema()
        try:
            dados = schema.load(request.json)
        except ValidationError as err:
            return make_response(jsonify(err.messages), 400)

        usuario_editado = usuario_service.editar_usuario(id_usuario, dados)
        if usuario_editado:
            return make_response(jsonify(schema.dump(usuario_editado)), 200)

        return make_response(jsonify({"message": "Usuário não encontrado"}), 404)

    def delete(self, id_usuario):
        if usuario_service.excluir_usuario(id_usuario):
            return make_response(jsonify({"message": "Usuário excluído com sucesso"}), 200)

        return make_response(jsonify({"message": "Usuário não encontrado"}), 404)
