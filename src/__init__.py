from flask import Flask, request
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.config.from_object('connection')
<<<<<<< HEAD
=======

>>>>>>> meu-trabalho
db = SQLAlchemy(app)
migrate = Migrate(app, db)
ma = Marshmallow(app)
api = Api(app)

# importa os models (para o migrate funcionar)
from src.models.usuario_model import UsuarioModel
from src.models.tarefa_model import TarefaModel

<<<<<<< HEAD

#TODO: Apontar os modelos (tabelas)
#      Apontar as Views

from .models.usuario_model import UsuarioModel

from .views import usuario_view
=======
# importa as views (elas mesmas registram as rotas)
from src.views import usuario_view, tarefa_view
>>>>>>> meu-trabalho
