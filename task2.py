import requests
import json
import sqlite3

#Send form-encoded data
payload = {
    "ajax":1,
    "action":"get_nearby_stores",
    "lat":4.210484,
    "lng":101.97576600000002
}

#Response object r. We can get all the information we need from this object.
r = requests.post("https://www.mcdonalds.com.my/storefinder/index.php", data=payload)
r.encoding = 'utf-8-sig'
stores = json.loads(r.text)
print(r.text)

conn = sqlite3.connect("mcdstore.db")
c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS stores (storeName TEXT, address TEXT, telephone TEXT,
            email TEXT, fax TEXT, latitude REAL, longitude REAL, category TEXT)""")

for s in stores["stores"]:
    list = []
    for cat in s["cat"]:
        list.append(cat["cat_name"])
    #Serialize obj to a formatted string
    l = json.dumps(list)
    #print(l)
    c.execute("INSERT OR IGNORE INTO stores VALUES (?,?,?,?,?,?,?,?)",
    (s["name"], s["address"], s["telephone"], s["email"], s["fax"], s["lat"], s["lng"], l))
conn.commit()
conn.close()
#print(len(stores))