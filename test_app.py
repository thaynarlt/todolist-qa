"""
Testes Unitários - To-Do List (Gerenciador de Tarefas)
Utiliza pytest para validar as operações CRUD.

Cada teste cobre uma regra de negócio específica,
incluindo cenários de sucesso (Happy Path) e falha (Sad Path).
"""

import pytest
from app import GerenciadorTarefas


@pytest.fixture
def gerenciador():
    """Retorna uma instância nova do GerenciadorTarefas."""
    return GerenciadorTarefas()


# ---- CREATE (Sucesso) ----
def test_adicionar_tarefa_com_titulo_e_descricao(gerenciador):
    """Deve criar uma tarefa com título, descrição e status pendente."""
    tarefa = gerenciador.adicionar_tarefa("Comprar leite", "No mercado central")

    assert tarefa.id == 1
    assert tarefa.titulo == "Comprar leite"
    assert tarefa.descricao == "No mercado central"
    assert tarefa.concluida is False


# ---- CREATE (Falha) ----
def test_adicionar_tarefa_com_titulo_vazio_levanta_erro(gerenciador):
    """Não deve permitir criar tarefa com título vazio — deve lançar ValueError."""
    with pytest.raises(ValueError, match="título da tarefa não pode ser vazio"):
        gerenciador.adicionar_tarefa("")


# ---- READ (Sucesso) ----
def test_buscar_tarefa_existente(gerenciador):
    """Deve retornar a tarefa correta ao buscar por um ID existente."""
    gerenciador.adicionar_tarefa("Tarefa 1", "Descrição 1")
    tarefa = gerenciador.buscar_tarefa(1)

    assert tarefa.titulo == "Tarefa 1"
    assert tarefa.descricao == "Descrição 1"


# ---- UPDATE (Sucesso) ----
def test_atualizar_titulo_da_tarefa(gerenciador):
    """Deve alterar apenas o título, mantendo os demais campos."""
    gerenciador.adicionar_tarefa("Tarefa 1", "Descrição 1")
    tarefa = gerenciador.atualizar_tarefa(1, titulo="Novo Título")

    assert tarefa.titulo == "Novo Título"
    assert tarefa.descricao == "Descrição 1"
    assert tarefa.concluida is False


# ---- DELETE (Sucesso) ----
def test_remover_tarefa_existente(gerenciador):
    """Deve remover a tarefa e ela não deve mais existir na lista."""
    gerenciador.adicionar_tarefa("Tarefa 1")
    tarefa_removida = gerenciador.remover_tarefa(1)

    assert tarefa_removida.titulo == "Tarefa 1"
    assert gerenciador.listar_tarefas() == []
