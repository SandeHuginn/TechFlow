    # ---------------- CLASSES ----------------
class Usuario:
    def __init__(self, username, senha, nome):
        self.username = username
        self.senha = senha
        self.nome = nome


class Tarefa:
    def __init__(self, id, titulo, descricao, prioridade):
        self.id = id
        self.titulo = titulo
        self.descricao = descricao
        self.prioridade = prioridade
        self.status = "Backlog"
        self.responsavel = None

    def exibir(self):
        print(f"\nID: {self.id}")
        print(f"Título: {self.titulo}")
        print(f"Descrição: {self.descricao}")
        print(f"Prioridade: {self.prioridade}")
        print(f"Status: {self.status}")
        print(f"Responsável: {self.responsavel}")


class Sistema:
    def __init__(self):
        self.usuarios = []
        self.tarefas = []
        self.usuario_logado = None
        self.proximo_id = 1
