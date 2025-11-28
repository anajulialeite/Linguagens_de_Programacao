from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate

db = SQLAlchemy()
ma = Marshmallow()
migrate = Migrate()
api = Api()

def create_app():
    app = Flask(__name__)
    app.config.from_object('connection')

    # Inicializar extensões
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)
    api.init_app(app)

    # Importar models
    with app.app_context():
        from src.models.usuario_model import UsuarioModel
        from src.models.tarefa_model import TarefaModel

        # Importar rotas SOMENTE AQUI
        from src.views.usuario_view import UsuarioList, UsuarioResource
        from src.views.tarefa_view import TarefaList, TarefaResource

        # Registrar as rotas
        api.add_resource(UsuarioList, "/usuario")
        api.add_resource(UsuarioResource, "/usuario/<int:id_usuario>")
        api.add_resource(TarefaList, "/tarefa")
        api.add_resource(TarefaResource, "/tarefa/<int:id_tarefa>")

    return app
