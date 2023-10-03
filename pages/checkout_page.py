from pages.base_page import BasePage
import conftest
from selenium.webdriver.common.by import By

from pages.home_page import HomePage


class CheckoutPage (BasePage):
    def __init__(self):
        self.driver = conftest.driver
        self.home_page = HomePage()
        self.text_checkout = (By.XPATH, "//span[contains(text(), 'Checkout: Your Information')]")
        self.first_name = (By.ID, "first-name")
        self.lasta_name = (By.ID, "last-name")
        self.postal_code = (By.ID, "postal-code")
        self.button_continue = (By.ID, "continue")
        self.finish = (By.ID, "finish")
        self.order = (By.XPATH, "//*[@class='complete-header' and text()='Thank you for your order!']")
        self.item_inventario = (By.XPATH, "//*[@class='inventory_item_name' and text()='{}']")

    
    def verificando_tela_de_checkout(self):
        self.verificar_se_elemento_existe(self.text_checkout)

    
    def inserindo_dados(self, primeiro_nome, ultimo_nome, caixa_postal):
        self.escrever(self.first_name, primeiro_nome)
        self.escrever(self.lasta_name, ultimo_nome)
        self.escrever(self.postal_code, caixa_postal)
        self.clicar(self.button_continue)
        
    
    def verificando_carrinho_de_compras(self, nome):
        item = (self.item_inventario[0], self.item_inventario[1].format(nome))
        self.verificar_se_elemento_existe(item)  

    def finish_compra(self):
        self.clicar(self.finish)

    def tela_obrigado_pelo_pagamento(self):
        self.verificar_se_elemento_existe(self.order)
