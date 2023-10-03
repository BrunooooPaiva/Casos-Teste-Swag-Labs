import pytest
from pages.login_page import LoginPage


@pytest.mark.usefixtures("setup_teardown")
class TestCT02:
    def test_ct_02_login_invalido(self):

        # Instancia os objetos a serem usados no teste
        login_page = LoginPage()
    
        # Faz login
        usuario = ""
        senha = ""
        login_page.fazer_login(usuario, senha)

        # Mensagens diferentes de acordo com sua condição (espaço em branco, usuário em branco, senha em branco ou usuário + senha errados)
        if (len(usuario) >= 1 and len(senha) >= 1):
            mensagem_erro_esperada = "Epic sadface: Username and password do not match any user in this service"
            return mensagem_erro_esperada
        elif ((len(usuario) == 0 and len(senha) >= 1) or len(usuario) == 0 and len(senha) == 0):
            mensagem_erro_esperada = "Epic sadface: Username is required"
            return mensagem_erro_esperada
        else:
            mensagem_erro_esperada = "Epic sadface: Password is required"

        # Verifica se o login não foi realizado e a mensagem de erro aparece
        login_page.verificar_mensagem_erro_login_existe()
        login_page.verificar_texto_mensagem_erro_login(mensagem_erro_esperada)

