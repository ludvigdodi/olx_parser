import requests
from bs4 import BeautifulSoup
from time import sleep
import sqlite3


header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0",
}

DB_NAME = 'catalog.db'
main_url = input("Insert the page link: ")
number_of_pages = int(input("Enter number of pages: "))
data = []


# GET PAGE
def get_html(url):
    r = requests.get(main_url, headers=header)
    return r


# GET DATA FROM PAGE
def get_content(html):
    soup = BeautifulSoup(html.text, 'html.parser')
    items = soup.find_all('div', class_="css-1sw7q4x")

    for item in items:
        link = item.find('a')
        title = item.find('h6')
        price = item.find('p')
        adress = item.find('p', class_="css-veheph")
        if link != None:
            data.append([link.get('href'), title.get_text(),
                        price.get_text(), adress.get_text()])
        print(data)
    return data


# DB
def adding_db(data):
    # CREATE TABLE AND LIST
    with sqlite3.connect(DB_NAME) as sqlite_conn:
        sql_request = """CREATE TABLE IF NOT EXISTS catalog (
            link TEXT,
            title TEXT NOT NULL,
            price INT,
            adress TEXT
            );"""
        sqlite_conn.execute(sql_request)
        sqlite_conn.commit()

    # ADD DATA TO LIST
        for i in data:
            sqlite_conn.execute("INSERT INTO catalog VALUES(?,?,?,?)",
                                (f"https://www.olx.ua{i[0]}", i[1], i[2], i[3]))
        sqlite_conn.commit()


# START PROGRAM
if __name__ == '__main__':
    for p in range(1, number_of_pages + 1):
        print(f"Parsing - {p} page")
        html = get_html(f"{main_url}/?page={p}")
        cont = get_content(html)
        sleep(2)

    adding_db(data)
