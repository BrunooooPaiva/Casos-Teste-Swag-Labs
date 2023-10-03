import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.cart_page import CartPage

@pytest.mark.usefixtures("setup_teardown")
class TestCT03:
    def test_ct03_adicionar_produtos_carrinho(self):
        login_page = LoginPage()
        home_page = HomePage()
        cart_page = CartPage()

        login_page.fazer_login("standard_user", "secret_sauce")
        home_page.verificar_login_com_sucesso()


        # Adicionando Mochila ao carrinho de compras
        home_page.adicionar_ao_carrinho('Sauce Labs Backpack')

        # Visitando carrinho de compras e verificando se a mochila foi adicionada
        cart_page.verificando_carrinho_de_compras('Sauce Labs Backpack')
        cart_page.clicando_no_botao_de_continuar_compras()

        # Adicionando Bike ao carrinho de compras
        home_page.adicionar_ao_carrinho('Sauce Labs Fleece Jacket')

        # Verificadno se os dois itens foram adicionado ao carrinho de compras corretamente
        cart_page.verificando_carrinho_de_compras('Sauce Labs Fleece Jacket')

