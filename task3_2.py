import os.path
import sys
import requests
import sqlite3
from bs4 import BeautifulSoup

STATUS_CODE = 200


def init():
    states = ["johor", "kedah", "kelantan", "kuala-lumpur", "melaka", "negeri-sembilan", 
    "pahang", "penang", "perak", "perlis", "putrajaya", "sabah", "sarawak", "selangor", 
    "brunei", "myanmar", "singapore", "thailand"]
    
    conn = sqlite3.connect("MarybrownRestaurants.db")
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS restaurants")
    c.execute("""CREATE TABLE IF NOT EXISTS restaurants (
    restoranID INTEGER PRIMARY KEY AUTOINCREMENT, 
    restoranName TEXT, restoranState TEXT, restoranAddress TEXT, restoranPhone TEXT)""")

    for state in states:
        body = ""
        if not os.path.exists("./task3_2/" + state + ".html"):
            payload = {"states": state}
            resp = requests.get("https://www.marrybrown.com/restaurants-by-listing/", 
            params=payload)

            if not resp.status_code == STATUS_CODE:
                print("Expected to get 200 for status code and not {}".format(resp.status_code))
                sys.exit(1)
            
            file = open("./task3_2/" + state + ".html", "w")
            file.write(resp.text)
            file.close()
        else:
            file = open("./task3_2/" + state + ".html", "r")
            body = file.read()
            file.close()

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
                c.execute("""INSERT INTO restaurants (restoranName, 
                restoranState, restoranAddress, restoranPhone) VALUES (?,?,?,?)""", 
                (restoran_name, state, restoran_address, r_phone))

    conn.commit()
    conn.close()
    

if __name__ == "__main__":
    init()