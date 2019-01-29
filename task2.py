import requests
import json
import sqlite3

#Add HTTP headers to a request.
#headersData = {"cookie":"__cfduid=d3983bf8b5b0c5afb2c7d73d6a38ef6771548742687; _ga=GA1.3.1364054270.1548742691; _gid=GA1.3.2113794150.1548742691; _gac_UA-52217625-3=1.1548742691.EAIaIQobChMIjNXdjayS4AIVBI-PCh25JQJsEAAYASAAEgI-svD_BwE; _gat_UA-52217625-3=1; _fbp=fb.2.1548742691281.34208051; XSRF-TOKEN=eyJpdiI6Ik1UaCtcL3JFUnd5RjREdXArMkNwdDhBPT0iLCJ2YWx1ZSI6Imp6aVRBOHpFR0xXVWlsS2lJRkVEdW41cTNaTkhuc2Zwbkl2cjlTREQ0aFNUb0FucGV0UWpXRlJ2cjF0RldObDkiLCJtYWMiOiJhYmEzMmJmMzYxYzgwYTQ1MTllMGZhMjViMzBmOTA3MDZjMzJlNjU0MGY0MGQ5NGY2M2E0NGY3MTc2NmY1YmFkIn0%3D; laravel_session=eyJpdiI6IlwvRXN1VEk0NG1cL2lDVjM0OHRYclZ1Zz09IiwidmFsdWUiOiJOQmZxZWthclFxS1pmeEs0NG91YUh1Y2wyZGVNZzlVNUtqXC9jRGhaZDRmeWl6Z05QeDFtNUt0dmNMMzl0Tmc5SyIsIm1hYyI6IjMyNmVkOTI2Yzg5MWJiZWNjMmE0MTQ3YWNmZTA0YmZhNTg4ZTE0ODc1Y2E0NmQ1MWZhZThmZDhkOWVkNzExZjQifQ%3D%3D"}
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
#print(r.text)

conn = sqlite3.connect("mcdstore.db")
c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS stores (storeName TEXT, address TEXT, telephone TEXT,
            email TEXT, fax TEXT, latitude REAL, longitude REAL, category TEXT)""")

for s in stores["stores"]:
    list = []
    for cat in s["cat"]:
        list.append(cat["cat_name"])
    l = json.dumps(list)
    #print(l)
    c.execute("INSERT OR IGNORE INTO stores VALUES (?,?,?,?,?,?,?,?)",
    (s["name"], s["address"], s["telephone"], s["email"], s["fax"], s["lat"], s["lng"], l))
conn.commit()
conn.close()
#print(len(stores))