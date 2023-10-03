import pytest
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.home_page import HomePage
from pages.login_page import LoginPage



@pytest.mark.usefixtures("setup_teardown")
class TestCT04:
    def test_ct04_compra_1_produto(self):
        login_page = LoginPage()
        home_page = HomePage()
        cart_page = CartPage()
        checkout_page = CheckoutPage()


        login_page.fazer_login("standard_user", "secret_sauce")
        home_page.verificar_login_com_sucesso()

        # Adicionando Mochila ao carrinho de compras
        home_page.adicionar_ao_carrinho('Sauce Labs Bolt T-Shirt')


        # Visitando carrinho de compras e verificando se a mochila foi adicionada
        cart_page.verificando_carrinho_de_compras('Sauce Labs Bolt T-Shirt')

        # Clicando no botão checkout
        cart_page.clicando_botão_de_checkout()

        # Verificando se está na tela de checkout e inserção de dados
        checkout_page.verificando_tela_de_checkout()
        checkout_page.inserindo_dados("Bruno", "Souza", "75114812")

        # Verificando os produtos para pagamento
        checkout_page.verificando_carrinho_de_compras('Sauce Labs Bolt T-Shirt')
        checkout_page.finish_compra()

        # Verificando se está na tela final após o pagamento
        checkout_page.tela_obrigado_pelo_pagamento()

