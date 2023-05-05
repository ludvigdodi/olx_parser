# OLX parser

Parsing ads from olx.ua

As requests to the parser, you need to submit a link to a category or search results.
Data is written to SQLite database - "catalog.db" file


### Collection Supported:

- Title
- Address
- Price and currency
- Link to announcement


## For work:

1. Clone/download archive from Github - make a clone of the project or download it as a zip archive unzip it to your computer

```sh
git@github.com:ludvigdodi/olx_parser.git
```

2. In folder with patrser open terminal and install dependencies
```sh
pip install pipenv

pipenv install
```
3. In the terminal, enter the command 
```sh
python main.py
```
4. Paste the previously copied link to the catalog / category of goods from the site
```sh
example: https://www.olx.ua/d/uk/elektronika/telefony-i-aksesuary/
```
5.  Enter the number of pages to parse
```sh
example: 10
```
6. Wait for the program to do the work


