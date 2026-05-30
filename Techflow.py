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

    # ---------------- LOGIN ----------------

    def cadastrar_usuario(self):
        nome = input("Nome: ")
        username = input("Usuário: ")
        senha = input("Senha: ")

        usuario = Usuario(username, senha, nome)
        self.usuarios.append(usuario)

        print("Usuário cadastrado!")

    def login(self):
        username = input("Usuário: ")
        senha = input("Senha: ")

        for usuario in self.usuarios:
            if usuario.username == username and usuario.senha == senha:
                self.usuario_logado = usuario
                print(f"Bem-vindo {usuario.nome}")
                return

        print("Usuário ou senha inválidos.")


    # ---------------- CREATE ----------------

    def criar_tarefa(self):
        titulo = input("Título: ")
        descricao = input("Descrição: ")
        prioridade = input("Prioridade (Baixa/Média/Alta/Crítica): ")

        tarefa = Tarefa(
            self.proximo_id,
            titulo,
            descricao,
            prioridade
        )

        self.tarefas.append(tarefa)
        self.proximo_id += 1

        print("Tarefa criada!")

    # ---------------- READ ----------------

    def listar_tarefas(self):
        if not self.tarefas:
            print("Nenhuma tarefa cadastrada.")
            return

        for tarefa in self.tarefas:
            tarefa.exibir()

    # ---------------- UPDATE ----------------

    def editar_tarefa(self):
        id_tarefa = int(input("ID da tarefa: "))

        for tarefa in self.tarefas:
            if tarefa.id == id_tarefa:

                tarefa.titulo = input("Novo título: ")
                tarefa.descricao = input("Nova descrição: ")
                tarefa.prioridade = input("Nova prioridade: ")
                tarefa.status = input(
                    "Novo status (Backlog/A Fazer/Em Andamento/Em Revisão/Concluído): "
                )

                print("Tarefa atualizada!")
                return

        print("Tarefa não encontrada.")

    # ---------------- DELETE ----------------

    def excluir_tarefa(self):
        id_tarefa = int(input("ID da tarefa: "))

        for tarefa in self.tarefas:
            if tarefa.id == id_tarefa:
                self.tarefas.remove(tarefa)
                print("Tarefa removida!")
                return

        print("Tarefa não encontrada.")

            # ---------------- MENU ----------------

    def menu(self):
        while True:

            print("\n===== SISTEMA ÁGIL =====")
            print("1 - Cadastrar usuário")
            print("2 - Login")
            print("3 - Criar tarefa")
            print("4 - Listar tarefas")
            print("5 - Editar tarefa")
            print("6 - Excluir tarefa")
            print("0 - Sair")

            opcao = input("Escolha: ")

            if opcao == "1":
                self.cadastrar_usuario()

            elif opcao == "2":
                self.login()

            elif opcao == "3":
                if self.usuario_logado:
                    self.criar_tarefa()
                else:
                    print("Faça login primeiro!")

            elif opcao == "4":
                self.listar_tarefas()

            elif opcao == "5":
                if self.usuario_logado:
                    self.editar_tarefa()
                else:
                    print("Faça login primeiro!")

            elif opcao == "6":
                if self.usuario_logado:
                    self.excluir_tarefa()
                else:
                    print("Faça login primeiro!")

            elif opcao == "0":
                print("Encerrando...")
                break

            else:
                print("Opção inválida!")


sistema = Sistema()

# Usuário padrão
sistema.usuarios.append(
    Usuario("admin", "123", "Administrador")
)

sistema.menu()