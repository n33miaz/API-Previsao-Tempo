# API Previsao Tempo
 openweathermap.org
# Previsão do Tempo com Flask e Python

Este projeto é uma aplicação web simples que consulta a previsão do tempo para uma cidade especificada pelo usuário, utilizando a API do OpenWeatherMap. A interface é construída com **Flask** e **HTML**, e o projeto é desenvolvido em **Python**.

## Requisitos

- Python 3.7 ou superior
- Conta e chave de API do [OpenWeatherMap](https://openweathermap.org/api)

## Como Usar

### 1. Clonar o Repositório

Certifique-se de que você está na pasta onde deseja clonar o projeto, e então execute:

```bash
$ git clone https://github.com/seu-usuario/seu-repositorio.git
$ cd seu-repositorio
```

### 2. Instalar Dependências

Certifique-se de que o `pip` está atualizado:

```bash
$ python -m pip install --upgrade pip
```

Em seguida, instale os pacotes necessários:

```bash
$ pip install requests
$ pip install flask
```

### 3. Configurar a Chave da API

- Abra o arquivo `app.py`.
- Substitua o valor da variável `API_Key` pela sua chave pessoal obtida no [OpenWeatherMap](https://openweathermap.org/appid).

```python
API_Key = "SUA_CHAVE_API"
```

### 4. Estrutura de Diretórios

Certifique-se de que os arquivos estão organizados da seguinte forma:

```
sua_pasta/
├── app.py
└── pagina/
    └── index.html
```

### 5. Executar a Aplicação

No terminal, dentro da pasta do projeto, execute:

```bash
$ python app.py
```

### 6. Acessar a Aplicação

Abra o navegador e vá para:

```
http://127.0.0.1:5000
```

### 7. Utilizando a Aplicação

1. No campo de busca, digite o nome de uma cidade.
2. Clique em "Buscar" para visualizar a previsão do tempo.
