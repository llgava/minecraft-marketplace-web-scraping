[English](../README.md) | Brazilian Portuguese

# Minecraft Marketplace Web Scraping
![Version Badge](https://img.shields.io/badge/version-beta--1.0-orange)
![Python Version Badge](https://img.shields.io/badge/python-3.8.6-blue)

Este projeto tem como intuito fazer a coleta de informações da página de catálogo da [Minecraft Marketplace](https://www.minecraft.net/en-us/catalog) por categoria e salvar em um arquivo `json` separadamente.

> #### Copyright
>
> Todas as informações coletadas são públicas, nenhuma informação favorece ou prejudica qualquer criador de conteúdo da Marketplace.
>
> Todas as informações coletadas **nao** são de autoria própria e pertecem a *Mojang AB*.

## Pré-requisitos

  * Instalar [Git](https://git-scm.com).
  * Instalar [Python](https://www.python.org/downloads/) e um instalador de pacotes para o Python; Recomendado: [pip](https://pypi.org/project/pip/).
  * Instalar [geckodriver](https://github.com/mozilla/geckodriver/releases).
  * (Opcional) Instalar uma IDE; Recomendado: [vscode](https://code.visualstudio.com).

Após fazer a instalação do Python e pip, entre no diretório do projeto e execute a instalação das dependências através do comando:

```shell
λ pip install -r requirements.txt
```

## Estrutura de JSON gerado

```json
[
  {
    "uuid": "str",
    "title": "str",
    "creator": "str",
    "price": "str | int",
    "url": "str",
    "keyart": "str"
  }
]
```

O preço pode ser tanto do tipo `string` quando `int` por motivo de existirem itens na Marketplace de graça, que são exibidos com o preço de **FREE**.

### Contato

Leonardo Luiz Gava - [@llgava](https://twitter.com/llgava "Leonardo Luiz Gava • Twitter") - <llgavamt@gmail.com>
