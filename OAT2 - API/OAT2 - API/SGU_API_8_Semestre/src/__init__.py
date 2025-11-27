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
db = SQLAlchemy(app)
migrate = Migrate(app, db)
ma = Marshmallow(app)
api = Api(app)

# importa os models (para o migrate funcionar)
from .models import usuario_model, tarefa_model


#TODO: Apontar os modelos (tabelas)
#      Apontar as Views

from .views import usuario_view, tarefa_view


