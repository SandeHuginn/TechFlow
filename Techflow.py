    # ---------------- CLASSES ----------------
class Usuario:
    def __init__(self, username, senha, nome, tipo):
        self.username = username
        self.senha = senha
        self.nome = nome
        self.tipo = tipo


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

        print("\nTipos:")
        print("1 - Administrador")
        print("2 - Usuário Local")

        opcao = input("Escolha: ")

        if opcao == "1":
            tipo = "admin"
        else:
            tipo = "local"

        usuario = Usuario(username, senha, nome, tipo)

        
        self.usuarios.append(usuario)

        print("Usuário cadastrado com sucesso!")
        
    def login(self):
        usuario = input("Usuário: ")
        senha = input("Senha: ")


        for u in self.usuarios:
            if u.username == usuario and u.senha == senha:
                self.usuario_logado = u
                print(f"\nBem-vindo, {u.nome}!")
                return True

        print("Usuário ou senha incorretos!")
        return False

    def logout(self):
        self.usuario_logado = None
        print("Logout realizado com sucesso!")

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

        tarefa.responsavel = self.usuario_logado.username

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

        if self.usuario_logado.tipo != "admin":
            print("Acesso negado!")
            return

        id_tarefa = int(input("ID da tarefa: "))

        for tarefa in self.tarefas:
            if tarefa.id == id_tarefa:
                self.tarefas.remove(tarefa)
                print("Tarefa removida!")
                return

        print("Tarefa não encontrada.")

    # ---------------- RELATORIO DESEMPENHO ----------------
    def relatorio_desempenho(self):

        if self.usuario_logado.tipo != "admin":
            print("Acesso negado!")
            return

        total_tarefas = len(self.tarefas)

        concluidas = 0
        andamento = 0
        backlog = 0
        revisao = 0
        criticas = 0

        for tarefa in self.tarefas:

            if tarefa.status == "Concluído":
                concluidas += 1

            elif tarefa.status == "Em Andamento":
                andamento += 1

            elif tarefa.status == "Backlog":
                backlog += 1

            elif tarefa.status == "Em Revisão":
                revisao += 1

            if tarefa.prioridade.lower() == "crítica":
                criticas += 1

        print("\n===== RELATÓRIO DE DESEMPENHO =====")
        print(f"Total de tarefas: {total_tarefas}")
        print(f"Tarefas concluídas: {concluidas}")
        print(f"Tarefas em andamento: {andamento}")
        print(f"Tarefas em revisão: {revisao}")
        print(f"Tarefas no backlog: {backlog}")
        print(f"Tarefas críticas: {criticas}")


    # ---------------- RELATORIO USUARIO ----------------
    def relatorio_usuarios(self):

        if self.usuario_logado.tipo != "admin":
            print("Acesso negado!")
            return

        print("\n===== PRODUTIVIDADE POR USUÁRIO =====")

        for usuario in self.usuarios:

            total = 0
            concluidas = 0

            for tarefa in self.tarefas:

                if tarefa.responsavel == usuario.username:

                    total += 1

                    if tarefa.status == "Concluído":
                        concluidas += 1

            print(f"\nUsuário: {usuario.nome}")
            print(f"Total de tarefas: {total}")
            print(f"Concluídas: {concluidas}")


    # ---------------- MENU LOGIN ----------------

    def menu_login(self):

        while True:

            print("\n===== TECHFLOW =====")
            print("1 - Login")
            print("2 - Cadastrar Usuário")
            print("0 - Sair")

            opcao = input("Escolha: ")

            if opcao == "1":

                if self.login():
                    self.menu_principal()

            elif opcao == "2":
                self.cadastrar_usuario()

            elif opcao == "0":
                print("Sistema encerrado.")
                break

            else:
                print("Opção inválida!")

    # ---------------- MENU PRINCIPAL ----------------

    def menu_principal(self):

        while self.usuario_logado:

            print("\n===== MENU PRINCIPAL =====")
            print(f"Usuário: {self.usuario_logado.nome}")
            print(f"Tipo: {self.usuario_logado.tipo}")

            print("1 - Criar tarefa")
            print("2 - Listar tarefas")
            print("3 - Editar tarefa")

            if self.usuario_logado.tipo == "admin":
                print("4 - Excluir tarefa")
                print("5 - Relatório Geral")
                print("6 - Relatório por Usuário")
                print("7 - Logout")
            else:
                print("4 - Logout")

            opcao = input("Escolha: ")

            # CREATE
            if opcao == "1":
                self.criar_tarefa()

            # READ
            elif opcao == "2":
                self.listar_tarefas()

            # UPDATE
            elif opcao == "3":
                self.editar_tarefa()

            # DELETE (somente admin)
            elif opcao == "4" and self.usuario_logado.tipo == "admin":
                self.excluir_tarefa()

            # RELATORIO GERAL
            elif opcao == "5" and self.usuario_logado.tipo == "admin":
                self.relatorio_desempenho()    

            # RELATORIO USUARIO
            
            elif opcao == "6" and self.usuario_logado.tipo == "admin":
                self.relatorio_usuarios()

             # LOGOUT ADMIN
            elif opcao == "7" and self.usuario_logado.tipo == "admin":
                self.logout()

            # LOGOUT LOCAL
            elif opcao == "4" and self.usuario_logado.tipo == "local":
                self.logout()

            else:
                print("Opção inválida!")


# ---------------- EXECUÇÃO ----------------

if __name__ == "__main__":

    sistema = Sistema()

    # Usuário administrador padrão
    sistema.usuarios.append(
        Usuario(
            "admin",
            "123",
            "Administrador",
            "admin"
        )
    )

    sistema.menu_login()