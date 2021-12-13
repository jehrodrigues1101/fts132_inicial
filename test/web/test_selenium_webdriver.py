# 1 importar bibliotecas
import os
from datetime import datetime

import pytest
# Classes
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By

caminho_print = 'C:/Users/jessi/PycharmProjects/fts132_inicial3/prints/' \
                + datetime.now().strftime('%Y-%m-%d %H-%M-%S') + '/'


class Test_selenium_webdriver:

    def before_all(self):

    # Criar pasta para guardar prints
        os.mkdir(caminho_print)

    # Definição de inicio- Executa antes do teste
    def setup_method(self):
        # Declarar o Objeto do Selenium e instanciar como navegador desejado
        self.driver = webdriver.Chrome(
            'C:/Users/jessi/PycharmProjects/fts132_inicial3/drivers/navegadores/chrome/96/chromedriver.exe')
        self.driver.implicitly_wait(30)  # O selenium vai esperar ate 30 segundos pelos elementos
        self.driver.maximize_window()  # Maximizar a Janela do navegador

        # Definição de Fim - Executa depois do teste

    def teardown_method(self):
        # Destruir o objeto do Selenium
        self.driver.quit()

    # Definição do teste
    @pytest.mark.parametrize('id, termo, curso, preco', [
        ('1', 'mantis', 'Mantis', 'R$ 59,99'),
        ('2', 'ctfl', 'Preparatório CTFL', 'R$ 199,00'),
    ])
    def testar_comprar_curso_click_na_lupa(self, id, termo, curso, preco):
        self.driver.get('https://www.iterasys.com.br')  # Selenium abra a url indicado
        self.driver.get_screenshot_as_file(f'{caminho_print}teste {id} - passo 1 - home.png')
        # Selenium clica no elemento
        self.driver.find_element(By.ID, 'searchtext').click()
        # O selenium apaga o conteudo da caixa de pesquisa
        self.driver.find_element(By.ID, 'searchtext').clear()
        # O selenium escreve mantis na caixa de pesquisa
        self.driver.find_element(By.ID, 'searchtext').send_keys(termo)
        self.driver.get_screenshot_as_file(f'{caminho_print}teste {id} - passo 2 - pesquisa pelo nome.png')
        # selenium clica no botão da lupa
        self.driver.find_element(By.ID, 'btn_form_search').click()
        # Selenium cliaca em matricule-se
        self.driver.find_element(By.CSS_SELECTOR, 'span.comprar').click()
        # O selenium valida o nome do curso no carrinho de compras
        assert self.driver.find_element(By.CSS_SELECTOR, 'span.item-title').text == curso
        assert self.driver.find_element(By.CSS_SELECTOR, 'span.new-price').text == preco

    def testar_comprar_curso_mantis_com_enter(self):
        self.driver.get('https://www.iterasys.com.br')  # Selenium abra a url indicado
        # Selenium clica no elemento
        self.driver.find_element(By.ID, 'searchtext').click()
        # O selenium apaga o conteudo da caixa de pesquisa
        self.driver.find_element(By.ID, 'searchtext').clear()
        # O selenium escreve mantis na caixa de pesquisa
        self.driver.find_element(By.ID, 'searchtext').send_keys('mantis')
        # selenium clica no botão pressiona enter
        self.driver.find_element(By.ID, 'btn_form_search').send_keys(keys.ENTER)
        # Selenium cliaca em matricule-se
        self.driver.find_element(By.CSS_SELECTOR, 'span.comprar').click()
        # O selenium valida o nome do curso no carrinho de compras
        assert self.driver.find_element(By.CSS_SELECTOR, 'span.item-title').text == 'Mantis'
        assert self.driver.find_element(By.CSS_SELECTOR, 'span.new-price').text == 'R$ 59,99'
