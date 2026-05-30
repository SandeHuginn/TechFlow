from Techflow import Sistema

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