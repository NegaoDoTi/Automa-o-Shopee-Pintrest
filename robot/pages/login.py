from selenium.webdriver.common.by import By
from utils.waits import Waits
from traceback import format_exc
from time import sleep

class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.waits:Waits = Waits(self.driver)

    def login(self, email:str, password:str) -> dict[bool, str]:
        try:
            self.driver.get("https://affiliate.shopee.com.br/offer/product_offer")

            # inserir_button = self.waits.wait_clickable({"css_selector" : 'a[class="home-btn"]'})
            # inserir_button.click()

            try:
                cookies = self.waits.wait_clickable({"css_selector" : 'div:nth-of-type(4) button:nth-child(2)'})
                cookies.click()
            except:
                return {"error" : False, "type" : "", "data" : ""}

            input_email = self.waits.wait_visibility({"css_selector" : 'input[name="loginKey"]'})
            input_email.send_keys(email)

            input_password = self.waits.wait_visibility({"css_selector" : 'input[name="password"]'})
            input_password.send_keys(password)

            form = self.waits.wait_visibility({"css_selector" : "form"})
            
            buttons = form.find_elements(By.CSS_SELECTOR, "button")

            button_submit = buttons[1]

            sleep(2)

            button_submit.click()

            print("Efetue o login no site da shopee e no site do pinterest pela extensão Save to Pinterest!")
            print("Apos concluir os Logins porfavor digite 'continue' para continuar o Robo ou 'sair' para finalizar o Robô")

            comando = str(input("Digite o comando: ")).strip().lower()
            if comando != "continue":
                return {"error" : True, "type" : "Aplicação finalizada!", "data" : "Aplicação finalizada!" }
            
            try:
                div_produtos = self.waits.wait_visibility({"css_selector" : 'div[class="product-offer-list"]'})
            except Exception:
                return {"error" : True, "type" : "Erro, parece que o login não foi efetuado com sucesso!", "data" : f"{format_exc()}"}

            return {"error" : False, "type" : "", "data" : ""}

        except Exception:
            return {"error" : True, "type" : "Erro inesperado ao efetuar login na shopee", "data" : f"{format_exc()}"}