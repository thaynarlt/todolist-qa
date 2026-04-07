"""
To-Do List - TO DO LIST
Lógica de negócio com operações CRUD completas.
"""


class Tarefa:
    """Representa uma tarefa individual do To-Do List."""

    def __init__(self, id: int, titulo: str, descricao: str = ""):
        self.id = id
        self.titulo = titulo
        self.descricao = descricao
        self.concluida = False

    def to_dict(self) -> dict:
        """Retorna a tarefa como dicionário."""
        return {
            "id": self.id,
            "titulo": self.titulo,
            "descricao": self.descricao,
            "concluida": self.concluida,
        }


class GerenciadorTarefas:
    """Gerencia a lista de tarefas com operações CRUD."""

    def __init__(self):
        self._tarefas: dict[int, Tarefa] = {}
        self._proximo_id: int = 1

    # ------------------------------------------------------------------ #
    #  CREATE
    # ------------------------------------------------------------------ #
    def adicionar_tarefa(self, titulo: str, descricao: str = "") -> Tarefa:
        """Adiciona uma nova tarefa à lista.

        Args:
            titulo: Título da tarefa (obrigatório, não pode ser vazio).
            descricao: Descrição opcional da tarefa.

        Returns:
            A tarefa criada.

        Raises:
            ValueError: Se o título for vazio ou apenas espaços em branco.
        """
        if not titulo or not titulo.strip():
            raise ValueError("O título da tarefa não pode ser vazio.")

        tarefa = Tarefa(id=self._proximo_id, titulo=titulo.strip(), descricao=descricao.strip())
        self._tarefas[tarefa.id] = tarefa
        self._proximo_id += 1
        return tarefa

    # ------------------------------------------------------------------ #
    #  READ
    # ------------------------------------------------------------------ #
    def buscar_tarefa(self, tarefa_id: int) -> Tarefa:
        """Busca uma tarefa pelo seu ID.

        Args:
            tarefa_id: ID da tarefa a ser buscada.

        Returns:
            A tarefa encontrada.

        Raises:
            KeyError: Se a tarefa não for encontrada.
        """
        if tarefa_id not in self._tarefas:
            raise KeyError(f"Tarefa com ID {tarefa_id} não encontrada.")
        return self._tarefas[tarefa_id]

    def listar_tarefas(self) -> list[Tarefa]:
        """Retorna todas as tarefas cadastradas.

        Returns:
            Lista com todas as tarefas (pode ser vazia).
        """
        return list(self._tarefas.values())

    # ------------------------------------------------------------------ #
    #  UPDATE
    # ------------------------------------------------------------------ #
    def atualizar_tarefa(
        self,
        tarefa_id: int,
        titulo: str | None = None,
        descricao: str | None = None,
        concluida: bool | None = None,
    ) -> Tarefa:
        """Atualiza os dados de uma tarefa existente.

        Apenas os campos informados (não-None) serão alterados.

        Args:
            tarefa_id: ID da tarefa a ser atualizada.
            titulo: Novo título (opcional).
            descricao: Nova descrição (opcional).
            concluida: Novo status de conclusão (opcional).

        Returns:
            A tarefa atualizada.

        Raises:
            KeyError: Se a tarefa não for encontrada.
            ValueError: Se o novo título for vazio.
        """
        tarefa = self.buscar_tarefa(tarefa_id)

        if titulo is not None:
            if not titulo or not titulo.strip():
                raise ValueError("O título da tarefa não pode ser vazio.")
            tarefa.titulo = titulo.strip()

        if descricao is not None:
            tarefa.descricao = descricao.strip()

        if concluida is not None:
            tarefa.concluida = concluida

        return tarefa

    def marcar_concluida(self, tarefa_id: int) -> Tarefa:
        """Atalho para marcar uma tarefa como concluída.

        Args:
            tarefa_id: ID da tarefa.

        Returns:
            A tarefa atualizada.
        """
        return self.atualizar_tarefa(tarefa_id, concluida=True)

    # ------------------------------------------------------------------ #
    #  DELETE
    # ------------------------------------------------------------------ #
    def remover_tarefa(self, tarefa_id: int) -> Tarefa:
        """Remove uma tarefa da lista.

        Args:
            tarefa_id: ID da tarefa a ser removida.

        Returns:
            A tarefa removida.

        Raises:
            KeyError: Se a tarefa não for encontrada.
        """
        tarefa = self.buscar_tarefa(tarefa_id)
        del self._tarefas[tarefa_id]
        return tarefa


# ------------------------------------------------------------------ #
#  Execução interativa (opcional)
# ------------------------------------------------------------------ #
if __name__ == "__main__":
    gerenciador = GerenciadorTarefas()

    # Exemplo de uso
    t1 = gerenciador.adicionar_tarefa("Estudar Python", "Revisar classes e métodos")
    t2 = gerenciador.adicionar_tarefa("Fazer exercícios", "Lista de pytest")

    print("=== Todas as tarefas ===")
    for t in gerenciador.listar_tarefas():
        print(t.to_dict())

    gerenciador.marcar_concluida(t1.id)
    print(f"\nTarefa '{t1.titulo}' concluída: {t1.concluida}")

    gerenciador.atualizar_tarefa(t2.id, titulo="Fazer exercícios de pytest")
    print(f"Tarefa atualizada: {t2.to_dict()}")

    gerenciador.remover_tarefa(t1.id)
    print(f"\nApós remover '{t1.titulo}':")
    for t in gerenciador.listar_tarefas():
        print(t.to_dict())
