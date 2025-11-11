# 🧠 Projeto de Extração e Automação de Dados - Lenarge Scraping Table

## 📋 Descrição Geral
Este projeto tem como objetivo **automatizar o processo de extração, manipulação, tratamento e armazenamento de dados** provenientes da aplicação **Lenarge**, utilizando **Selenium** apenas como ferramenta de **acesso e download automático** da tabela disponibilizada diretamente pelo próprio app.

> ⚙️ **Importante:**  
> O processo de **extração da tabela já existe nativamente dentro do aplicativo Lenarge**.  
> O papel do Selenium neste projeto **não é extrair linha a linha** da interface, mas sim **automatizar o acesso, navegação e download** da tabela em seu formato padrão atual, garantindo consistência e periodicidade.

Este projeto se diferencia do repositório **`web_scraping_v2`**, onde o Selenium é usado de forma mais profunda — lá ele **navega, coleta e reconstrói dados linha a linha** devido à ausência de uma função de exportação complexa no aplicativo.  
Aqui, o foco é **otimizar o processo já existente** e integrá-lo a fluxos automatizados de manipulação e armazenamento.

A estrutura foi desenvolvida para permitir **reutilização modular**, de forma que os dados extraídos possam ser utilizados em **relatórios automáticos**, **subextrações específicas** e **integrações com outros sistemas administrativos**.

------------------------------------------------------------------------

## 🚀 Funcionalidades Principais

### 1. Acesso e Download Automatizado (Web Scraping Simplificado)
- O Selenium é utilizado **somente para login, navegação e download automático** da tabela disponibilizada pelo app Lenarge.  
- O download segue um padrão de nome (`programacao--YYYY-MM-DD...`) e é salvo automaticamente na pasta de downloads.  
- O script identifica o arquivo mais recente e o move para o diretório de processamento.  
- Este fluxo garante **extrações padronizadas e reprodutíveis**, sem depender de ações manuais.

### 2. Manipulação de Pastas e Arquivos
- Função `manipulacao_path()` com estrutura iterativa e validações robustas.  
- Verificação das variáveis de ambiente (`PATH_DOWNLOAD`, `PATH_DATA`).  
- Criação de diretórios ausentes e tratamento de erros padronizado.  
- Movimentação segura do arquivo mais recente, renomeando conforme timestamp.  
- Garantia de que apenas o último arquivo modificado é considerado válido.

### 3. Tratamento e Padronização dos Dados
- Padronização de nomes de colunas e normalização de formatos.  
- Conversões seguras de tipo (string → numérico, datetime).  
- Eliminação de duplicatas e inconsistências.  
- Enriquecimento com colunas de metadados (ex: data de extração, fonte, id único).  
- Estrutura final ideal para inserção em bancos relacionais (MySQL).

### 4. Integração com Banco de Dados MySQL
- Conexão via `mysql.connector` ou `SQLAlchemy`.  
- Criação automática de tabelas (DDL dinâmica).  
- Inserção incremental, evitando sobrescrever históricos.  
- Logs detalhados de execução e falhas.  
- Compatível com execuções locais e remotas (via script ou automação agendada).

### 5. Reutilização e Modularidade
Este projeto serve como **base de dados oficial** para:
- Relatórios e dashboards gerenciais;
- Subextrações específicas (clientes, transportadoras, notas, etc.);
- Integrações com pipelines de automação financeira e operacional;
- Scripts complementares que utilizam os dados baixados e tratados.

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


