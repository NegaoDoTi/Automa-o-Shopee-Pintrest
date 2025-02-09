from robot.pages.login import LoginPage
from robot.pages.products import ProductPage
from utils.config_driver import Driver
from config.config import email, password
import logging

class Robot:

    def start(self):

        self.driver = Driver().get_undetected_chrome_driver()

        self.login = LoginPage(self.driver)
        self.products_page = ProductPage(self.driver)

        login_process = self.login.login(email, password)
        if login_process["error"] == True:
            if login_process['type'] == "Aplicação finalizada!":
                print("Encerrando Robô!")
                self.driver.quit()
                quit()
            
            logging.critical(f'{login_process["type"]}, {login_process["data"]}')
            quit()

        count_pagination = 3

        while True:
            
            products = self.products_page.get_cards_div()
            if products["error"] == True:
                logging.critical(f'{process["type"]}, {process["data"]}')
                quit()

            if products["error"] == False:
                div_products = products["products"]

            process = self.products_page.process(div_products, count_pagination)
            if process["error"] == True:
                logging.critical(f'{process["type"]}, {process["data"]}')
                quit()
            
            if process["error"] == False:
                count_pagination = process["pagination"]
        
