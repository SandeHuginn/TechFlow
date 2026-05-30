from Techflow import Sistema, Usuario, Tarefa

 # ---------------- TESTE CADASTRO DE USUARIO ----------------
def test_cadastro_usuario(monkeypatch):

    sistema = Sistema()

    entradas = iter([
        "João",
        "joao",
        "123",
        "2"
    ])

    monkeypatch.setattr(
        "builtins.input",
        lambda _: next(entradas)
    )

    sistema.cadastrar_usuario()

    assert len(sistema.usuarios) == 1
    assert sistema.usuarios[0].username == "joao"
    assert sistema.usuarios[0].tipo == "local"

    # ---------------- TESTE LOGIN VALIDO ----------------
def test_login_valido(monkeypatch):

    sistema = Sistema()

    sistema.usuarios.append(
        Usuario(
            "joao",
            "123",
            "João",
            "local"
        )
    )

    entradas = iter([
        "joao",
        "123"
    ])

    monkeypatch.setattr(
        "builtins.input",
        lambda _: next(entradas)
    )

    resultado = sistema.login()

    assert resultado is True

    # ---------------- TESTE LOGIN INVÁLIDO ----------------
def test_login_invalido(monkeypatch):

    sistema = Sistema()

    entradas = iter([
        "teste",
        "999"
    ])

    monkeypatch.setattr(
        "builtins.input",
        lambda _: next(entradas)
    )

    resultado = sistema.login()

    assert resultado is False

    # ---------------- TESTE CRIAÇÂO DE TAREFA----------------
def test_criar_tarefa(monkeypatch):

    sistema = Sistema()

    sistema.usuario_logado = Usuario(
        "joao",
        "123",
        "João",
        "local"
    )

    entradas = iter([
        "Bug Login",
        "Corrigir autenticação",
        "Alta"
    ])

    monkeypatch.setattr(
        "builtins.input",
        lambda _: next(entradas)
    )

    sistema.criar_tarefa()

    assert len(sistema.tarefas) == 1
    assert sistema.tarefas[0].titulo == "Bug Login"

    # ---------------- TESTE PERMISSÂO DE EXCLUSÂO----------------

def test_local_nao_pode_excluir(monkeypatch):

    sistema = Sistema()

    sistema.usuario_logado = Usuario(
        "joao",
        "123",
        "João",
        "local"
    )

    sistema.excluir_tarefa()

    assert len(sistema.tarefas) == 0

    # ---------------- TESTE ADMINISTRADOR----------------
def test_admin_pode_excluir(monkeypatch):

    sistema = Sistema()

    sistema.usuario_logado = Usuario(
        "admin",
        "123",
        "Administrador",
        "admin"
    )

    sistema.tarefas.append(
        Tarefa(
            1,
            "Teste",
            "Descrição",
            "Alta"
        )
    )

    entradas = iter([
        "1"
    ])

    monkeypatch.setattr(
        "builtins.input",
        lambda _: next(entradas)
    )

    sistema.excluir_tarefa()

    assert len(sistema.tarefas) == 0

    # ---------------- TESTE RELATORIO DE DESEMPENHO/GERAL----------------
def test_relatorio_desempenho(capsys):

    sistema = Sistema()

    sistema.usuario_logado = Usuario(
        "admin",
        "123",
        "Administrador",
        "admin"
    )

    tarefa1 = Tarefa(
        1,
        "Bug Login",
        "Corrigir autenticação",
        "Alta"
    )
    tarefa1.status = "Concluído"

    tarefa2 = Tarefa(
        2,
        "Dashboard",
        "Criar dashboard",
        "Crítica"
    )
    tarefa2.status = "Em Andamento"

    sistema.tarefas.append(tarefa1)
    sistema.tarefas.append(tarefa2)

    sistema.relatorio_desempenho()

    saida = capsys.readouterr().out

    assert "Total de tarefas: 2" in saida
    assert "Tarefas concluídas: 1" in saida
    assert "Tarefas em andamento: 1" in saida
    assert "Tarefas críticas: 1" in saida

    # ---------------- TESTE RELATORIO POR USUARIO----------------
def test_relatorio_usuarios(capsys):

    sistema = Sistema()

    admin = Usuario(
        "admin",
        "123",
        "Administrador",
        "admin"
    )

    joao = Usuario(
        "joao",
        "123",
        "João",
        "local"
    )

    maria = Usuario(
        "maria",
        "123",
        "Maria",
        "local"
    )

    sistema.usuario_logado = admin

    sistema.usuarios.append(admin)
    sistema.usuarios.append(joao)
    sistema.usuarios.append(maria)

    tarefa1 = Tarefa(1, "Tarefa 1", "Descrição", "Alta")
    tarefa1.responsavel = "joao"
    tarefa1.status = "Concluído"

    tarefa2 = Tarefa(2, "Tarefa 2", "Descrição", "Alta")
    tarefa2.responsavel = "joao"
    tarefa2.status = "Backlog"

    tarefa3 = Tarefa(3, "Tarefa 3", "Descrição", "Alta")
    tarefa3.responsavel = "maria"
    tarefa3.status = "Concluído"

    sistema.tarefas.extend([
        tarefa1,
        tarefa2,
        tarefa3
    ])

    sistema.relatorio_usuarios()

    saida = capsys.readouterr().out

    assert "João" in saida
    assert "Maria" in saida

    assert "Total de tarefas: 2" in saida
    assert "Concluídas: 1" in saida

    # ---------------- TESTE RELATORIO VISIBILIDADE----------------
def test_local_nao_pode_ver_relatorio(capsys):

    sistema = Sistema()

    sistema.usuario_logado = Usuario(
        "joao",
        "123",
        "João",
        "local"
    )

    sistema.relatorio_desempenho()

    saida = capsys.readouterr().out

    assert "Acesso negado!" in saida