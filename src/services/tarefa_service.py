from src.models.tarefa_model import TarefaModel
from src import db

# Função para cadastrar uma nova tarefa
def cadastrar_tarefa(tarefa):
    nova_tarefa = TarefaModel(
        titulo=tarefa.titulo,
        descricao=tarefa.descricao,
        concluida=tarefa.concluida
    )
    db.session.add(nova_tarefa)
    db.session.commit()
    return nova_tarefa


# Função para listar todas as tarefas
def listar_tarefas_service():
    return TarefaModel.query.all()


# Função para atualizar uma tarefa existente
def atualizar_tarefa_service(tarefa, tarefa_nova):
    tarefa.titulo = tarefa_nova.titulo
    tarefa.descricao = tarefa_nova.descricao
    tarefa.concluida = tarefa_nova.concluida
    db.session.commit()
    return tarefa


# Função para remover uma tarefa
def remover_tarefa_service(tarefa):
    db.session.delete(tarefa)
    db.session.commit()
