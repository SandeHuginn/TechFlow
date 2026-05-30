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