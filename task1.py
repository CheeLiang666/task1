import json
import requests
import sqlite3

headersData = {
    "remote_address":"110.74.177.173:443",
    "content_type":"application/json",
    "cookie":"_gcl_au=1.1.1721302690.1546506033; 7ca746ce7fe0def195d70be50aabba8038c6394f89e0cc553e3028ede520a45e=ab89c3df3b7e20a080754d5745133c0bf8de40225f6f68e9d876b41f4e39c621; _ga=GA1.3.1655757456.1546506033; _gac_UA-50820363-1=1.1546506034.EAIaIQobChMIjrLZ9J_R3wIV0A0rCh3s-A23EAAYASAAEgJed_D_BwE; _gac_UA-50820363-6=1.1546506034.EAIaIQobChMIjrLZ9J_R3wIV0A0rCh3s-A23EAAYASAAEgJed_D_BwE; AMP_TOKEN=%24NOT_FOUND; _gid=GA1.3.561490073.1548722253; _fbp=fb.2.1548722252769.254046646; _gat_UA-50820363-1=1; _gat_UA-50820363-6=1"
}

r = requests.get("https://kfc.com.my/api/v2/store?1548723564791", headers = headersData)
stores = json.loads(r.text)
print(len(stores))

#create sqlite database and store information
#open a connection to the sqlite database file database
conn = sqlite3.connect("kfcstore.db")
c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS stores (storeID INTEGER PRIMARY KEY,
            latitude REAL, longitude REAL, storeName TEXT)""")
for x in range(len(stores)):
    c.execute("INSERT OR IGNORE INTO stores VALUES (?,?,?,?)",
    (stores[x]["id"], stores[x]["latitude"], stores[x]["longitude"], stores[x]["name"]))

print("Successfully insert into database")
#commit the changes and close the database
conn.commit()
conn.close()