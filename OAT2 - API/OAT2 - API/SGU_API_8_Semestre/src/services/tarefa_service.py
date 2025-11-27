# src/services/tarefa_service.py
from src.models.tarefa_model import TarefaModel
from src import db

def cadastrar_tarefa(tarefa):
    nova_tarefa = TarefaModel(
        titulo=tarefa.titulo,
        descricao=getattr(tarefa, 'descricao', None),
        usuario_id=getattr(tarefa, 'usuario_id', None),
        status=getattr(tarefa, 'status', 'Pendente')
    )
    db.session.add(nova_tarefa)
    db.session.commit()
    return nova_tarefa

def listar_tarefa():
    return TarefaModel.query.all()

def listar_tarefa_id(id_tarefa):
    return TarefaModel.query.get(id_tarefa)

def editar_tarefa(id_tarefa, dados):
    tarefa = listar_tarefa_id(id_tarefa)
    if not tarefa:
        return None
    # atualiza apenas os campos permitidos
    tarefa.titulo = dados.get('titulo', tarefa.titulo)
    tarefa.descricao = dados.get('descricao', tarefa.descricao)
    tarefa.status = dados.get('status', tarefa.status)
    # se passou usuario_id, atualiza (você pode validar existência do usuário antes)
    if 'usuario_id' in dados:
        tarefa.usuario_id = dados['usuario_id']
    db.session.commit()
    return tarefa

def excluir_tarefa(id_tarefa):
    tarefa = listar_tarefa_id(id_tarefa)
    if not tarefa:
        return False
    db.session.delete(tarefa)
    db.session.commit()
    return True
