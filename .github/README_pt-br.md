[English](../README.md) | Brazilian Portuguese

# Minecraft Marketplace Web Scraping
![Version Badge](https://img.shields.io/badge/Version-beta--1.0.2-orange?style=flat-square)
![Python Version Badge](https://img.shields.io/badge/3.8.6-blue?style=flat-square&logo=python&logoColor=white)

Este projeto tem como intuito fazer a coleta de informações da página de catálogo da [Minecraft Marketplace](https://www.minecraft.net/en-us/catalog) por categoria e salvar em um arquivo `json` separadamente.

> ##### Copyright
>
> Todas as informações coletadas são públicas, nenhuma informação favorece ou prejudica qualquer criador de conteúdo da Marketplace.
>
> Todas as informações coletadas **nao** são de autoria própria e pertecem a *Mojang AB*.

## Pré-requisitos

  * Instalar [Git](https://git-scm.com).
  * Instalar [Python](https://www.python.org/downloads/) e um instalador de pacotes para o Python; Recomendado: [pip](https://pypi.org/project/pip/).
  * Instalar [geckodriver](https://github.com/mozilla/geckodriver/releases).
  * (Opcional) Instalar uma IDE; Recomendado: [vscode](https://code.visualstudio.com).

## Instalando dependências

Depois de instalar o Python e pip, entre no diretório do projeto, crie um novo Ambiente Virtual e ative-o:

```shell
λ python -m venv .env
λ source .env/bin/activate
```

Depois de criar e ativar o Ambiente Virtual, instale todas as dependências com o pip.

```shell
λ pip install -r requirements.txt
```

## Configurando as Variáveis de Ambient (sessão em desenvolvimento)

Agora, você vai precisar configurar as variáveis de ambiente, na raiz do projeto você pode encontrar o arquivo `.env.template`, renomeie para `.env` e configure todas as variáveis necessárias:

* **API_URL** - em desenvolvimento...
* **BEARER_TOKEN** - em desenvolvimento...

## Rodando o programa

```shell
λ clear && python main.py
```

## Estrutura de JSON gerado
Você também pode ver um exemplo em `data/example.json`.

```json
[
  {
    "uuid": "str",
    "title": "str",
    "description": "str",
    "creator": "str",
    "price": "str",
    "trailer": "str | null",
    "keyart": "str",
    "rating": {
      "average": "float",
      "total": "int"
    },
    "url": "str",
  }
]
```

### Contato

Leonardo Luiz Gava - [@llgava](https://twitter.com/llgava "Leonardo Luiz Gava • Twitter") - <llgavamt@gmail.com>
