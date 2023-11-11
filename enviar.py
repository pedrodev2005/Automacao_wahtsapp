import urllib
import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import os

contatos = pd.read_excel("teste.xlsx")

navegador = webdriver.Chrome()
navegador.get("https://web.whatsapp.com/")

while len(navegador.find_elements(By.ID, "side")) < 1:
    time.sleep(1)

for i, mensagem in enumerate(contatos['Mensagem']):
    pessoa = contatos.loc[i, "Pessoas"]
    numero = contatos.loc[i, "Número"]
    texto = urllib.parse.quote(f"Oi, {pessoa}! {mensagem}")
    link = f"https://web.whatsapp.com/send?phone={numero}&text={texto}"
    navegador.get(link)

    while len(navegador.find_elements(By.ID, "side")) < 1:
        time.sleep(1)
    time.sleep(4)
    caminho_completo = os.path.abspath(f"catalogo.pdf")
    # clica no x
    navegador.find_element(By.XPATH,
                           '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div/div/div/div/span').click()
    # clica no doc
    navegador.find_element(By.XPATH,
                           '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div/div/span/div/ul/div/div[1]/li/div/input').send_keys(caminho_completo)
    time.sleep(2)
    # envia o
    navegador.find_element(By.XPATH,
                           '//*[@id="app"]/div/div/div[3]/div[2]/span/div/span/div/div/div[2]/div/div[2]/div[2]/div/div[1]').click()

    time.sleep(8)
