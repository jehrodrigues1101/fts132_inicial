import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


# Classes e Definições
class TestConsultarmantis():
    def setup_method(self, method):
        self.driver = webdriver.Chrome('C:/Users/jessi/PycharmProjects/fts132_inicial3\drivers/navegadores/chrome/96/chromedriver.exe')
        self.driver.implicitly_wait (30) # robo espera ate 30 segundos pelos elementos
        self.driver.maximize_window() # maximizar a janela do navegador
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_consultarmantis(self):
        self.driver.get("https://iterasys.com.br/plataforma/home/index.php?action=initial")
        self.driver.set_window_size(1616, 876)
        self.driver.find_element(By.ID, "searchtext").click()
        self.driver.find_element(By.ID, "searchtext").send_keys("mantis")
        self.driver.find_element(By.ID, "btn_form_search").click()
        self.driver.find_element(By.CSS_SELECTOR, ".comprar").click()
        assert self.driver.find_element(By.CSS_SELECTOR, ".item-title").text == "Mantis"
        assert self.driver.find_element(By.CSS_SELECTOR, ".new-price").text == "R$ 59,99"
