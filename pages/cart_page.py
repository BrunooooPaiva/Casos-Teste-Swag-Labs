from pages.base_page import BasePage
import conftest
from selenium.webdriver.common.by import By
from pages.home_page import HomePage


class CartPage (BasePage):
    def __init__(self):
        self.driver = conftest.driver
        self.home_page = HomePage()
        self.cart = (By.XPATH, "//a[@class='shopping_cart_link']")
        self.item_inventario = (By.XPATH, "//*[@class='inventory_item_name' and text()='{}']")
        self.continue_shopping = (By.XPATH, "//button[@id='continue-shopping']")
        self.checkout = (By.XPATH, "//button[@id='checkout']")

    
    def verificando_carrinho_de_compras(self, nome):
        self.clicar(self.cart)
        item = (self.item_inventario[0], self.item_inventario[1].format(nome))
        self.verificar_se_elemento_existe(item)

    def clicando_no_botao_de_continuar_compras(self):
        self.clicar(self.continue_shopping)

    def clicando_botão_de_checkout(self):
        self.clicar(self.checkout)