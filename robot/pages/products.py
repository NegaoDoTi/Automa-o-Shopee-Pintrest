from traceback import format_exc
from utils.waits import Waits
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webelement import WebElement
import pyautogui
import random
from time import sleep

class ProductPage:

    def __init__(self, driver):
        self.driver:uc.Chrome = driver
        self.waits:Waits = Waits(self.driver)

    def get_cards_div(self) -> dict[bool, str, str, WebElement]:
        try:
            sleep(5)

            div_products = self.waits.wait_visibility({"css_selector" : 'div[class="product-offer-list-wrap"]'})

            return {"error" : False, "type" : "", "data" : "", "products" : div_products}
        except:
            return {"error" : True, "type" : "Erro ao buscar div dos produtos", "data" : f"{format_exc()}"}


    def process(self, web_element:WebElement, count_pagination:int) -> dict[bool, str]:
        try:
            
            div_products = web_element

            products_cards = div_products.find_elements(By.CSS_SELECTOR, 'div[class="product-offer-item"]')
            for product_card in products_cards:
                sleep(random.uniform(3.0, 4.5))

                button_link = product_card.find_element(By.CSS_SELECTOR, "button")
                self.driver.execute_script("arguments[0].click()", button_link)

                sleep(3)

                text_area_link = self.waits.wait_visibility({"css_selector" : 'div[class="ant-modal-body"] textarea'})
                link = text_area_link.text

                sleep(random.uniform(2.0, 3.0))

                self.driver.execute_script(f"window.open('{link}', '_blank')")
                
                sleep(random.uniform(2.0, 2.5))

                self.driver.switch_to.window(self.driver.window_handles[-1])


                sleep(random.uniform(4.0, 5.5))

                while True:
                    section_img = self.waits.wait_visibility({"css_selector" : 'div.container > section > section:first-of-type'})

                    img = section_img.find_elements(By.CSS_SELECTOR, 'img[loading="lazy"]')[random.randrange(3, 5)]

                    self.driver.execute_script("arguments[0].scrollIntoView()", img)

                    self.driver.execute_script("arguments[0].click()", img)
                    
                    try:
                        pyautogui.moveTo(random.randrange(930, 945), random.randrange(650, 655), random.uniform(0.3, 0.8))

                        pyautogui.click()

                        sleep(random.uniform(0.8, 1.2))

                        pyautogui.moveTo(random.randrange(485, 505), random.randrange(370, 400), random.uniform(0.3, 0.8))
                        extension = self.driver.find_element(By.CSS_SELECTOR, "body > span")
                      
                        break
                    except:
                        pyautogui.moveTo(1201, 219)
                        pyautogui.click()
                        pass
                    
                sleep(random.uniform(1.5, 2.0))

                pyautogui.moveTo(307, 164, duration=random.uniform(0.3 , 0.8))

                pyautogui.moveTo(473, 164, duration=random.uniform(0.3 , 0.8))

                pyautogui.click()

                sleep(random.uniform(2.0, 3.0))

                self.driver.close()

                self.driver.switch_to.window(self.driver.window_handles[0])

                sleep(random.uniform(1.5, 2.0))

                close_modal = self.waits.wait_clickable({"css_selector" : 'span[class="ant-modal-close-x"]'})
                self.driver.execute_script("arguments[0].click()", close_modal)

                sleep(random.uniform(3.0, 3.5))

                if product_card == products_cards[-1]:
                    pagination_span = self.waits.wait_clickable({"css_selector" : f'div[class="PaginationNoTotal__wrap"] span:nth-child({count_pagination})'})
                    count_pagination = count_pagination + 1
                    self.driver.execute_script("arguments[0].click()", pagination_span)
                    return {"error" : False, "type" : "", "data" : "", "pagination" : count_pagination}

            return {"error" : False, "type" : "", "data" : ""}

        except Exception:
            return {"error" : True, "type" : "Erro inesperado ao fazer processo de salvar no Pinterest", "data" : f"{format_exc()}" }