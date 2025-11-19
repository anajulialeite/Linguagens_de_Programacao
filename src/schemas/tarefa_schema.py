from src import ma
from src.models.tarefa_model import TarefaModel

class TarefaSchema(ma.SQLAlchemySchema):
    class Meta:
        model = TarefaModel
        load_instance = True

    id = ma.auto_field()
    titulo = ma.auto_field()
    descricao = ma.auto_field()
    status = ma.auto_field()
