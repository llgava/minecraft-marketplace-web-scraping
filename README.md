English | [Brazilian Portuguese](.github/README_pt-br.md)

# Minecraft Marketplace Web Scraping
![Version Badge](https://img.shields.io/badge/Version-beta--1.0.2-orange?style=flat-square)
![Python Version Badge](https://img.shields.io/badge/3.8.6-blue?style=flat-square&logo=python&logoColor=white)

This project aims to collect information from the [Minecraft Marketplace](https://www.minecraft.net/en-us/catalog) catalog page by category and save it in a `json` file separately.

> ##### Copyright
>
> All information collected is public, no information favors or harms any content creator on the Marketplace.
>
> All information collected **is not** of its own authorship and belongs to *Mojang AB*.

## Prerequisites

  * Install [Git](https://git-scm.com).
  * Install [Python](https://www.python.org/downloads/) and a package installer for Python; Recommended: [pip](https://pypi.org/project/pip/).
  * Install [geckodriver](https://github.com/mozilla/geckodriver/releases).
  * (Optional) Install an IDE; Recommended:  [vscode](https://code.visualstudio.com).

## Instaling dependencies

After installing Python and pip, enter the project directory create a new Virtual Enviroment and activate:

```shell
λ python -m venv .env
λ source .env/bin/activate
```

After create and activate the Virtual Enviroment, install all dependencies with pip.

```shell
λ pip install -r requirements.txt
```

## Configuring Enviroment Variables (section in development)

Now you will need to configure the enviroments variables, on the root of project you can found the file `.env.template`, rename to `.env` and set all the needed variables:

* **API_URL** - under development...
* **BEARER_TOKEN** - under development...

## Running the program

```shell
λ clear && python main.py
```

## Generated JSON structure
You can also see a example at `data/example.json`.

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

### Contact

Leonardo Luiz Gava - [@llgava](https://twitter.com/llgava "Leonardo Luiz Gava • Twitter") - <llgavamt@gmail.com>
