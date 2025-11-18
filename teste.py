from selenium import webdriver
import time

# Inicia o navegador
navegador = webdriver.Chrome()

# Maximiza a janela
navegador.maximize_window()

# Abre o site
navegador.get("https://sp.senai.br/unidade/lencoispaulista/")

# ---- abre os botões menu ----
lista_links = navegador.find_elements("css selector", ".nav-link.menu-link.dropdown-toggle")
for link in lista_links:
    if "Cursos" in link.text:
        link.click()
        break

time.sleep(5)

lista_links = navegador.find_elements("css selector", ".nav-link.menu-link.dropdown-toggle")
for link in lista_links:
    if "Processo Seletivo" in link.text:
        link.click()
        break

time.sleep(5)

lista_links = navegador.find_elements("css selector", ".nav-link.menu-link.dropdown-toggle")
for link in lista_links:
    if "O SENAI" in link.text:
        link.click()
        break

time.sleep(5)

lista_links = navegador.find_elements("css selector", ".nav-link.menu-link.dropdown-toggle")
for link in lista_links:
    if "Para a sua empresa" in link.text:
        link.click()
        break

time.sleep(5)

lista_links = navegador.find_elements("css selector",".nav-link.menu-link.dropdown-toggle")
for link in lista_links:
    if "Transparência" in link.text:
        link.click()
        break

time.sleep(5)

# --- Acessa todos os botões ---

lista_links = navegador.find_elements("css selector", ".nav-link.nav-link-escola")
for link in lista_links:
    if "Informações aos Alunos" in link.text:
        link.click()
        break

time.sleep(5)

lista_links = navegador.find_elements("css selector", ".nav-link.nav-link-escola")
for link in lista_links:
    if "Atendimento a Empresas" in link.text:
        link.click()
        break

time.sleep(5)

lista_links = navegador.find_elements("css selector", ".nav-link.nav-link-escola")
for link in lista_links:
    if "Horário de Atendimento" in link.text:
        link.click()
        break   

time.sleep(5)