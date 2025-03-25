# Teste Automatizado de Fluxo de Compra com Selenium

Este repositório contém um teste automatizado que simula o fluxo de compra em um site de comércio eletrônico, utilizando o Selenium WebDriver com Python. O objetivo principal é verificar a funcionalidade correta do processo de login, adição de itens ao carrinho, checkout e finalização da compra.

## Requisitos

Para executar este teste, você precisará dos seguintes componentes instalados em seu sistema:

* **Python 3.x:** A linguagem de programação utilizada para o script de teste.
* **Selenium:** A biblioteca Python para automatização de navegadores web.
* **WebDriver (ChromeDriver):** O driver específico para o navegador Google Chrome, que permite ao Selenium controlá-lo.

## Instalação

Siga estas etapas para configurar o ambiente de teste:

1.  **Instale o Python 3.x:**
    * Se você ainda não tiver o Python instalado, baixe a versão mais recente do site oficial do Python: [python.org](https://www.python.org/).
2.  **Instale o Selenium:**
    * Abra o terminal ou prompt de comando e execute o seguinte comando para instalar o Selenium usando o gerenciador de pacotes pip:

    ```bash
    pip install selenium
    ```

3.  **Baixe o ChromeDriver:**
    * Baixe o ChromeDriver correspondente à versão do seu navegador Google Chrome no site oficial do ChromeDriver: [chromedriver.chromium.org](https://chromedriver.chromium.org/).
    * Coloque o arquivo `chromedriver.exe` (ou `chromedriver` em sistemas Linux/macOS) no mesmo diretório do script de teste (`test_purchase_flow.py`) ou adicione o caminho do ChromeDriver à variável de ambiente PATH do seu sistema.


## Como Executar o Teste

1.  Certifique-se de que o Python e o ChromeDriver estão configurados corretamente.
2.  Abra o terminal ou prompt de comando e navegue até o diretório do projeto.
3.  Execute o script de teste com o seguinte comando:

    ```bash
    python test_purchase_flow.py
    ```

4.  O script abrirá uma janela do navegador Google Chrome e executará automaticamente as etapas do fluxo de compra.

## Descrição do Teste

O script de teste executa as seguintes ações:

1.  Acessa a página inicial do site de demonstração de comércio eletrônico.
2.  Realiza o login com o usuário "standard_user" e a senha "secret_sauce".
3.  Adiciona um item ao carrinho de compras e verifica se a adição foi bem-sucedida.
4.  Acessa a página do carrinho de compras para validar a presença do item.
5.  Inicia o processo de checkout.
6.  Preenche as informações de checkout (nome, sobrenome e código postal).
7.  Finaliza a compra e verifica se a mensagem de sucesso "THANK YOU FOR YOUR ORDER" é exibida.
8.  Fecha o navegador após a conclusão do teste.

## Resultados Esperados

* O teste deve ser executado sem erros se o fluxo de compra estiver funcionando corretamente.
* Mensagens de sucesso serão exibidas no console para cada etapa do teste.
* Em caso de falha, mensagens de erro detalhadas serão exibidas no console.


