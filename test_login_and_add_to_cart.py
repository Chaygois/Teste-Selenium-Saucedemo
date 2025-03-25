from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configuração do driver
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)

try:
    print("🔹 Acessando a página...")
    driver.get("https://www.saucedemo.com/v1/")
    driver.maximize_window()
    
    # Login
    print("🔹 Realizando login...")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    
    # Aguardar a lista de produtos carregar
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "inventory_list"))
    )
    print("✅ Login realizado com sucesso!")

    # Adicionar um item ao carrinho
    print("🔹 Adicionando item ao carrinho...")
    add_to_cart_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'ADD TO CART')]"))
    )
    add_to_cart_button.click()

    # Acessar o carrinho
    print("🔹 Acessando o carrinho...")
    cart_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))
    )
    cart_link.click()

    # Verificar se o item foi adicionado ao carrinho
    item = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "inventory_item_name"))
    )

    assert item.is_displayed(), "❌ ERRO: O item não foi adicionado ao carrinho!"
    print("✅ Teste passou: O item foi adicionado com sucesso!")

    # Clicar em Checkout
    print("🔹 Iniciando Checkout...")
    checkout_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "checkout_button"))
    )
    checkout_button.click()

    # Preencher informações de checkout
    print("🔹 Preenchendo informações de checkout...")
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "first-name"))
    ).send_keys("QA")

    driver.find_element(By.ID, "last-name").send_keys("Tester")
    driver.find_element(By.ID, "postal-code").send_keys("12345")

    # Clicar em continuar
    print("🔹 Continuando checkout...")
    driver.find_element(By.CLASS_NAME, "cart_button").click()

    # Confirmar a página de checkout
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))
    )
    print("✅ Página de resumo do pedido carregada com sucesso!")

    # Finalizar compra
    print("🔹 Finalizando compra...")
    finish_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "cart_button"))
    )
    finish_button.click()

    # Verificar mensagem de sucesso
    print("🔹 Verificando mensagem de sucesso...")
    success_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "complete-header"))
    )

    assert "THANK YOU FOR YOUR ORDER" in success_message.text, "❌ ERRO: Pedido não foi finalizado corretamente!"
    print("✅ Teste passou: Pedido finalizado com sucesso!")

finally:
    print("🔹 Fechando o navegador...")
    driver.quit()
