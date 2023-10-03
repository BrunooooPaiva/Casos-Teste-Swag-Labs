import pytest
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.home_page import HomePage
from pages.login_page import LoginPage


@pytest.mark.usefixtures("setup_teardown")
class TestCT05:
    def test_ct05_compra_dois_produtos(self):
        login_page = LoginPage()
        home_page = HomePage()
        cart_page = CartPage()
        checkout_page = CheckoutPage()


        # Fazendo Login
        login_page.fazer_login("standard_user", "secret_sauce")
        home_page.verificar_login_com_sucesso()

        # Adicionando produto ao carrinho de compras
        home_page.adicionar_ao_carrinho('Sauce Labs Bolt T-Shirt')


        # Visitando carrinho de compras e verificando se a mochila foi adicionada
        cart_page.verificando_carrinho_de_compras('Sauce Labs Bolt T-Shirt')

        # Voltando para a página de produtos
        cart_page.clicando_no_botao_de_continuar_compras()

        # Adicionando Bike ao carrinho de compras
        home_page.adicionar_ao_carrinho('Sauce Labs Bike Light')

        # Verificadno se os dois itens foram adicionado ao carrinho de compras corretamente
        cart_page.verificando_carrinho_de_compras('Sauce Labs Bolt T-Shirt')
        cart_page.verificando_carrinho_de_compras('Sauce Labs Bike Light')

        # Clicando no botão checkout
        cart_page.clicando_botão_de_checkout()

        # Verificando se está na tela de checkout e inserção de dados
        checkout_page.verificando_tela_de_checkout()
        checkout_page.inserindo_dados("Bruno", "Souza", "75114812")


        # Verificando os produtos para pagamento
        checkout_page.verificando_carrinho_de_compras('Sauce Labs Bolt T-Shirt')
        checkout_page.verificando_carrinho_de_compras('Sauce Labs Bike Light')
        checkout_page.finish_compra()

        # Verificando se está na tela final após o pagamento
        checkout_page.tela_obrigado_pelo_pagamento()



