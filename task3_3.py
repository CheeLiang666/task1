import os.path
import sys
import requests
import sqlite3
from bs4 import BeautifulSoup

STATUS_CODE = 200


def download_information(state="selangor"):
    payload = {"states": state}
    resp = requests.get("https://www.marrybrown.com/restaurants-by-listing/", params=payload)
    if not resp.status_code == STATUS_CODE:
        print("Expected to get 200 for status code and not {}".format(resp.status_code))
        sys.exit(1)
    
    return resp.text


def write_file(f_path, contents):
    f = open(f_path, "w")
    f.write(contents)
    f.close()


def read_file(f_path):
    f = open(f_path, "r")
    body = f.read()
    f.close()
    return body


def init():
    conn = sqlite3.connect("Marybrown.db")
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS restaurants")
    c.execute("""CREATE TABLE IF NOT EXISTS restaurants (
    restaurantID INTEGER PRIMARY KEY, 
    restaurantName TEXT, restaurantState TEXT, restaurantAddress TEXT, restaurantPhone TEXT)""")

    # Get the absolute path
    absolute_path = os.path.abspath(".")
    task3_path = os.path.join(absolute_path, "task3_3")
    STATES_FILE = "states.html"
    f_path = os.path.join(task3_path, STATES_FILE)
    
    if not os.path.exists(f_path):
        data = download_information()
        write_file(f_path, data)
    
    body = read_file(f_path)
    soup = BeautifulSoup(body, "html.parser")
    selection_list = soup.find("select", id="states")
    # Get the state title and remove it.
    state_title = selection_list.find("option", value="0")
    state_title.decompose()
    # Get all the available states in the selection list.
    states = selection_list.find_all("option")
    
    for state in states:
        state_name = state["value"]
        s_path = os.path.join(task3_path, state_name + ".html")
        if not os.path.exists(s_path):
            state_data = download_information(state_name)
            write_file(s_path, state_data)
        
        state_content = read_file(s_path)
        state_soup = BeautifulSoup(state_content, "html.parser")
        state_restaurants = state_soup.find_all("div", class_="restaurant_listing")
        for s_restaurant in state_restaurants:
            s_restaurant_name = s_restaurant.find("strong", class_="content_title").get_text()
            s_restaurant_phone = s_restaurant.find("img", title="Contact Us")
            s_phone = "-"
            if s_restaurant_phone is not None:
                s_phone = s_restaurant_phone.get_text().strip()
                s_restaurant_phone.decompose()
            s_restaurant_address = s_restaurant.find("p").get_text()
            c.execute("""INSERT INTO restaurants (restaurantName, restaurantState, 
            restaurantAddress, restaurantPhone) VALUES (?,?,?,?)""",
            (s_restaurant_name, state_name, s_restaurant_address, s_phone))
    
    conn.commit()
    conn.close()
    

if __name__ == "__main__":
    init()