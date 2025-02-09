# from selenium.webdriver.chrome.webdriver import WebDriver as ChromeWebDriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.chrome.options import Options as ChromeOptions
# from webdriver_manager.chrome import ChromeDriverManager as ChromeDriverManager
from undetected_chromedriver.options import ChromeOptions
import undetected_chromedriver as uc

from traceback import format_exc
from pathlib import Path
import logging

class Driver():
    """Classe responsavel pro gerenciar driver selenium que o robo irá utilizar!
    """
    
    def __init__(self):
        self.__extension_path = Path(Path(__file__).parent.parent, "extension")
        self.__user_data_dir = Path(Path(__file__).parent.parent, "sessoes_chrome")

    # def get_chrome_driver(self) -> ChromeWebDriver:
    #     try:
    #         self.__service = ChromeService(executable_path=ChromeDriverManager().install())

    #         self.__options = ChromeOptions()
    #         self.__options.add_extension(f"{self.__extension_path}")

    #         self.__driver = ChromeWebDriver(options=self.__options, service=self.__service)

    #         self.__driver.maximize_window()

    #         return self.__driver
        
    #     except:
    #         logging.critical(format_exc())
    #         raise ConnectionError("Erro ao abrir navegador!")
        
    def get_undetected_chrome_driver(self) -> uc.Chrome:
        try:
            self.__undetected_chrome_options = ChromeOptions()
            self.__undetected_chrome_options.add_argument(f"--user-data-dir={self.__user_data_dir}")
            self.__undetected_chrome_options.add_argument(f'--load-extension={self.__extension_path}')
            self.__undetected_chrome_options.add_argument("--disable-popup-blocking")

            self.__driver = uc.Chrome(options=self.__undetected_chrome_options)

            self.__driver.maximize_window()

            return self.__driver

        except Exception:
            logging.critical(format_exc())
            ConnectionError("Erro inesperado ao abrir undetected chrome driver")
