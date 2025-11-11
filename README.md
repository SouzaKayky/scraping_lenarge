# 🧠 Projeto de Extração e Automação de Dados - Lenarge Scraping Table

## 📋 Descrição Geral

Este projeto tem como objetivo automatizar **a extração, manipulação,
tratamento e armazenamento de dados** provenientes da aplicação
**Lenarge**, utilizando **Selenium para web scraping**, manipulação de
arquivos locais e integração com **MySQL** para persistência de dados.

A estrutura foi desenvolvida para permitir **reutilização modular**, de
forma que os dados extraídos possam ser utilizados em **relatórios
automáticos**, **subextrações específicas** e **integrações com outros
sistemas administrativos**.

------------------------------------------------------------------------

## 🚀 Funcionalidades Principais

### 1. Extração de Dados (Web Scraping)

-   Extração de tabelas do app Lenarge utilizando **Selenium
    WebDriver**.
-   Localização dinâmica de elementos com **XPath otimizados**.
-   Scroll automatizado e iteração em carrosséis e tabelas dinâmicas.
-   Armazenamento temporário em arquivos `.xlsx` ou `.csv` gerados
    automaticamente.

### 2. Manipulação de Pastas e Arquivos

-   Função `manipulacao_path()` com lógica iterativa e validada.
-   Verificação das variáveis de ambiente (`PATH_DOWNLOAD`, `PATH_DATA`)
    com tratamento de erro profissional.
-   Identificação automática do arquivo mais recente baseado no padrão
    de nomeação.
-   Movimentação segura do arquivo mais recente para o diretório de
    destino.
-   Geração de nomes padronizados e limpos com `safe_filename()`.

### 3. Tratamento e Padronização dos Dados

-   Normalização de colunas com nomes consistentes e legíveis.
-   Conversão de tipos (string → int, float, datetime) para
    compatibilidade SQL.
-   Remoção de duplicatas e registros inconsistentes.
-   Enriquecimento com colunas derivadas (ex: data de extração, fonte,
    identificadores únicos).
-   Transformação em formato tabular ideal para uso em bancos
    relacionais.

### 4. Integração com Banco de Dados MySQL

-   Conexão via `mysql.connector` ou `SQLAlchemy`.
-   Criação automática de tabelas se não existirem.
-   Inserção incremental (append) de novos dados sem sobrescrever
    históricos.
-   Logs de execução e falhas de conexão.
-   Scripts configuráveis para rodar localmente ou em servidores
    remotos.

### 5. Reutilização e Modularidade

-   O projeto foi estruturado para permitir uso em **outros scripts e
    automações**, como:
    -   Geração de relatórios diários ou semanais;
    -   Subextrações de dados específicas (clientes, transportadoras,
        notas, etc);
    -   Dashboards e integrações com Power BI ou Google Data Studio.

------------------------------------------------------------------------

## ⚙️ Estrutura Recomendada de Pastas

    ScrapingTable/
    │
    ├── src/
    │   ├── main.py                # Execução principal da extração
    │   ├── utils/
    │   │   ├── scraping.py        # Funções Selenium e XPaths
    │   │   ├── look_path.py       # Manipulação de diretórios e arquivos
    │   │   ├── data_clean.py      # Tratamento e normalização dos dados
    │   │   └── db_mysql.py        # Integração e inserção no MySQL
    │   │
    │   └── config/
    │       └── .env               # Variáveis de ambiente (PATH_DOWNLOAD, PATH_DATA, DB_CREDENTIALS)
    │
    ├── data/
    │   ├── raw/                   # Dados brutos extraídos
    │   └── processed/             # Dados tratados e prontos para carga
    │
    └── README.md

------------------------------------------------------------------------

## 🛠️ Tecnologias Utilizadas

  Categoria                 Ferramenta
  ------------------------- -------------------------------
  Web Scraping              Selenium, XPath, ChromeDriver
  Manipulação de Arquivos   pathlib, shutil
  Tratamento de Dados       pandas, datetime
  Banco de Dados            MySQL, SQLAlchemy
  Automação                 Python 3.11+
  Ambiente                  `.env`, dotenv

------------------------------------------------------------------------

## 🧩 Fluxo de Execução

1.  **Extração:** Selenium acessa o app Lenarge, localiza e exporta a
    tabela desejada.\
2.  **Manipulação:** O arquivo mais recente é identificado e movido para
    o diretório `data/processed`.\
3.  **Tratamento:** Os dados são normalizados, limpos e convertidos para
    um formato padrão.\
4.  **Persistência:** Inserção no banco de dados MySQL com checagem de
    duplicatas.\
5.  **Reuso:** O dataset consolidado é utilizado em relatórios,
    automações e análises.

------------------------------------------------------------------------

## 🧰 Configuração do Ambiente

1.  **Instale as dependências**

    ``` bash
    pip install -r requirements.txt
    ```

2.  **Configure o arquivo `.env`**

    ``` env
    PATH_DOWNLOAD=C:\Users\user\Downloads
    PATH_DATA=C:\Users\user\Documents\data_processed
    MYSQL_USER=root
    MYSQL_PASSWORD=senha
    MYSQL_DB=lenarge_data
    MYSQL_HOST=localhost
    ```

3.  **Execute o script principal**

    ``` bash
    python src/main.py
    ```

------------------------------------------------------------------------

## 🧠 Futuras Expansões

-   Adição de logs detalhados (logging + monitoramento).
-   Agendamento automático com Airflow ou cron jobs.
-   Deploy em nuvem (Google Cloud ou AWS) com execução remota.
-   Integração com dashboards analíticos.

------------------------------------------------------------------------

## 🧾 Licença

Este projeto é de uso interno e educativo.\
Desenvolvido com foco em automação e integração de dados
administrativos e profissionais.


