from src import db

class TarefaModel(db.Model):
    __tablename__ = 'tarefa'

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.String(255))
    status = db.Column(db.String(50), nullable=False, default='Pendente')

    def __init__(self, titulo, descricao, status='Pendente'):
        self.titulo = titulo
        self.descricao = descricao
        self.status = status
