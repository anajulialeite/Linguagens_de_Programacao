# src/models/tarefa_model.py
from src import db

class TarefaModel(db.Model):
    __tablename__ = 'tarefa'

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.String(255))
    status = db.Column(db.String(50), nullable=False, default='Pendente')
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)

    def __init__(self, titulo, descricao=None, usuario_id=None, status='Pendente'):
        self.titulo = titulo
        self.descricao = descricao
        self.usuario_id = usuario_id
        self.status = status
