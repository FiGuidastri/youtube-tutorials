from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = r'C:\Users\filipe.guidastri\Projetos\youtube-tutorials\tech-with-tim\python-selenium-tutorials\chromedriver.exe'
service = Service(PATH)

driver = webdriver.Chrome(service=service)
driver.get('https://www.viarondon.com.br/')

try:
    # Aguarda até que a tabela esteja presente na página
    tabela = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "vr-tabela__inner"))
    )

    # Encontra todas as linhas da tabela
    linhas = tabela.find_elements(By.TAG_NAME, "tr")

    # Extrai o texto de cada célula em cada linha
    conteudo_tabela = []
    for linha in linhas:
        celulas = linha.find_elements(By.TAG_NAME, "td")
        linha_texto = [celula.text for celula in celulas]
        conteudo_tabela.append(linha_texto)

    # Exibe o conteúdo extraído
    for linha in conteudo_tabela:
        print(linha)

except Exception as e:
    print("Erro ao localizar a tabela ou extrair dados:", e)
finally:
    driver.quit()
