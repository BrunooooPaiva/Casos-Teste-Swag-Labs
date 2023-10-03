import time
import conftest
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self):
        self.driver = conftest.driver
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.invalid_login = (By.XPATH, "//*[@class='error-message-container error']")
        self.message_error_login = (By.XPATH, "//h3[@data-test='error']")
        self.login_button = (By.ID, "login-button")


    def fazer_login(self, usuario, senha):

        self.escrever(self.username_field, usuario)
        self.escrever(self.password_field, senha)
        self.clicar(self.login_button)
        time.sleep(2)


    def verificar_mensagem_erro_login_existe(self):
        self.verificar_se_elemento_existe(self.invalid_login)

    def verificar_texto_mensagem_erro_login(self, texto_esperado):
        texto_encontrado = self.pegar_texto_elemento(self.message_error_login)
        assert texto_encontrado == texto_esperado, f"O texto retornado foi: '{texto_encontrado}', mas era esperado o texto '{texto_esperado}'"
