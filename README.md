English | [Brazilian Portuguese](.github/README_pt-br.md)

# Minecraft Marketplace Web Scraping
![Version Badge](https://img.shields.io/badge/version-beta--1.0-orange)
![Python Version Badge](https://img.shields.io/badge/python-3.8.6-blue)

This project aims to collect information from the [Minecraft Marketplace](https://www.minecraft.net/en-us/catalog) catalog page by category and save it in a `json` file separately. 

> #### Copyright
>
> All information collected is public, no information favors or harms any content creator on the Marketplace. 
>
> All information collected **is not** of its own authorship and belongs to *Mojang AB*. 

## Prerequisites

  * Install [Git](https://git-scm.com).
  * Install [Python](https://www.python.org/downloads/) and a package installer for Python; Recommended: [pip](https://pypi.org/project/pip/).
  * Install [geckodriver](https://github.com/mozilla/geckodriver/releases).
  * (Optional) Install an IDE; Recommended:  [vscode](https://code.visualstudio.com).

After installing Python and pip, enter the project directory and perform the installation of the dependencies using the command: 

```shell
λ pip install -r requirements.txt
```

## Generated JSON structure
```json
[
  {
    "uuid": str,
    "title": str,
    "creator": str,
    "price": str | int,
    "url": str,
    "keyart": str
  }
]
```
The price can be either `string` or `int` because there are items on the Marketplace for free, which are displayed at the price of **FREE**. 

### Contact

Leonardo Luiz Gava - [@llgava](https://twitter.com/llgava "Leonardo Luiz Gava • Twitter") - <llgavamt@gmail.com>
