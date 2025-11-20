from flask import Flask, request
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from dotenv import load_dotenv
import os

load_dotenv()

<<<<<<< HEAD
app = Flask(__name__)
app.config.from_object('connection')
<<<<<<<< HEAD:OAT2 - API/SGU_API_8_Semestre/SGU_API_8_Semestre/src/__init__.py
========
<<<<<<< HEAD
=======

>>>>>>> meu-trabalho
>>>>>>>> c382b46ab4dc7ab4e1eca4224a6248dd848121b5:src/__init__.py
=======
# instanciando o Flask e a Api
app = Flask(__name__)
app.config.from_object('connection')
>>>>>>> c382b46ab4dc7ab4e1eca4224a6248dd848121b5
db = SQLAlchemy(app)
migrate = Migrate(app, db)
ma = Marshmallow(app)
api = Api(app)

<<<<<<< HEAD
<<<<<<<< HEAD:OAT2 - API/SGU_API_8_Semestre/SGU_API_8_Semestre/src/__init__.py
#TODO: Apontar os modelos (tabelas)
#      Apontar as Views

from src.models.usuario_model import UsuarioModel
========
# importa os models (para o migrate funcionar)
from src.models.usuario_model import UsuarioModel
from src.models.tarefa_model import TarefaModel

<<<<<<< HEAD

#TODO: Apontar os modelos (tabelas)
#      Apontar as Views

from .models.usuario_model import UsuarioModel
>>>>>>>> c382b46ab4dc7ab4e1eca4224a6248dd848121b5:src/__init__.py

from .views import usuario_view
=======
# importa as views (elas mesmas registram as rotas)
from src.views import usuario_view, tarefa_view
>>>>>>> meu-trabalho
=======
#TODO: Apontar os modelos (tabelas)
#      Apontar as Views

<<<<<<< HEAD:src/__init__.py
from .models.usuario_model import UsuarioModel
=======
from src.models.usuario_model import UsuarioModel
>>>>>>> 4a09d256fc91400db154801acacb4571852dcc75:OAT2 - API/SGU_API_8_Semestre/SGU_API_8_Semestre/src/__init__.py

from .views import usuario_view
>>>>>>> c382b46ab4dc7ab4e1eca4224a6248dd848121b5
