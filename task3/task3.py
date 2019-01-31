import os.path
import sys
import requests
import sqlite3
from bs4 import BeautifulSoup

HTMLFILE = "marybrown.html"
STATUS_CODE = 200


def init():
    body = ""
    if not os.path.exists(HTMLFILE):
        resp = requests.get("https://www.marrybrown.com/restaurants-by-listing/?states=selangor")
        if not resp.status_code == STATUS_CODE:
            print("Expected to get 200 for status code and not {}".format(resp.status_code))
            # exit the program
            sys.exit(1)

        # create a file for storing the html code.
        file = open(HTMLFILE, "w")
        file.write(resp.text)
        file.close()
    else:
        file = open(HTMLFILE, "r")
        body = file.read()
        file.close()

    conn = sqlite3.connect("MarybrownRestoran.db")
    c = conn.cursor()
    c.execute("DROP TABLE restorans")
    c.execute("""CREATE TABLE IF NOT EXISTS restorans (
        restoranID INTEGER PRIMARY KEY AUTOINCREMENT, 
        restoranName TEXT, restoranPhone TEXT, restoranAddress TEXT)""")

    soup = BeautifulSoup(body, "html.parser")
    restorans = soup.find_all("div", class_="restaurant_listing")

    for restoran in restorans:
        restoran_name = restoran.find("strong", class_="content_title").get_text()
        restoran_phone = restoran.find("img", title="Contact Us")
        r_phone = "-"
        if restoran_phone:
            r_phone = restoran_phone.get_text().strip()
            restoran_phone.decompose()
        restoran_address = restoran.find("p").get_text()
        c.execute("""INSERT INTO restorans (restoranName, 
        restoranPhone, restoranAddress) VALUES (?,?,?)""", 
        (restoran_name, r_phone, restoran_address))
    else:
        print("Successfully inserted restoran records.")
        conn.commit()
        conn.close()
        

if __name__ == "__main__":
    init()