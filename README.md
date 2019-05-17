# **Tasks during Internship**

## Table of Contents
  - [Read this first](#read-this-first)
  - [Task 1](#task-1)
    - [Explanation for task 1](#explanation-for-task-1)
    - [Code snippets for task 1](#code-snippets-for-task-1)
      - [Import library](#import-library)
      - [Adding HTTP header](#adding-http-header)
      - [Decoding JSON data to a Python object](#decoding-json-data-to-a-python-object)
      - [Create SQLite Database for storing data](#create-sqlite-database-for-storing-data)
    - [References for task 1](#references-for-task-1)
  - [Task 2](#task-2)
    - [Explanation for task 2](#explanation-for-task-2)
    - [Code snippets for task 2](#code-snippets-for-task-2)
      - [Import library](#import-library-1)
      - [POST request](#post-request)
      - [Set encoding](#set-encoding)
      - [Decoding JSON data to a Python object](#decoding-json-data-to-a-python-object-1)
      - [Create SQLite Database for storing data](#create-sqlite-database-for-storing-data-1)
    - [References for task 2](#references-for-task-2)

## Read this first
* This is the repository for storing the tasks that have been done during the internship period.
* This repository contains necessary explanation for each of the completed task.
* References that assist in doing each of the task was documented properly in below.
* All the codes were compiled and run using [Visual Studio Code](https://code.visualstudio.com/).
* The operating system involved in doing the tasks is **Ubuntu** operating system.

## Task 1
## Explanation for task 1
Task 1 is to download the *[KFC stores json data](https://kfc.com.my/api/v2/store?1548824841143)* from [KFC website](https://kfc.com.my/find-a-kfc). The *[KFC stores json data](https://kfc.com.my/api/v2/store?1548824841143)* was then been processed for storing into the **SQLite** database.

## Code snippets for task 1
First of all, in order to download, process, and storing the *[KFC stores json data](https://kfc.com.my/api/v2/store?1548824841143)*, three library need to be imported which are *requests*, *json*, and *sqlite3*.

### Import library
Importing the *requests*, *json*, and *sqlite3* library.
```python
import requests
import json
import sqlite3
```

### Adding HTTP header
For task 1, we need to add the HTTP header to a request by passing in a **dict** to the **headers** parameter.

In this case, **headersData** will pass to the **headers** parameter. The **cookie** is the important key in getting the *[KFC stores json data](https://kfc.com.my/api/v2/store?1548824841143)*.
```python
headersData = {
    "remote_address":"110.74.177.173:443",
    "content_type":"application/json",
    "cookie":"_gcl_au=1.1.1721302690.1546506033; 7ca746ce7fe0def195d70be50aabba8038c6394f89e0cc553e3028ede520a45e=ab89c3df3b7e20a080754d5745133c0bf8de40225f6f68e9d876b41f4e39c621; _ga=GA1.3.1655757456.1546506033; _gac_UA-50820363-1=1.1546506034.EAIaIQobChMIjrLZ9J_R3wIV0A0rCh3s-A23EAAYASAAEgJed_D_BwE; _gac_UA-50820363-6=1.1546506034.EAIaIQobChMIjrLZ9J_R3wIV0A0rCh3s-A23EAAYASAAEgJed_D_BwE; AMP_TOKEN=%24NOT_FOUND; _gid=GA1.3.561490073.1548722253; _fbp=fb.2.1548722252769.254046646; _gat_UA-50820363-1=1; _gat_UA-50820363-6=1"
}
```
After that, the **headersData** is passed to the **headers** parameter in a request as shown in below.
```python
r = requests.get("https://kfc.com.my/api/v2/store?1548723564791", headers = headersData)
```
Now, we have a Response object called r. We can get all the information we need from this object. The reason why using *request.get()* method is because it is a **GET** request.

### Decoding JSON data to a Python object
The code below will deserialize a **str** instance containing a JSON document to a Python object.
```python
stores = json.loads(r.text)
```

### Create SQLite Database for storing data
For storing data into **SQLite** database, we need to create a **SQLite** database and open a connection to the **SQLite** database.
```python
conn = sqlite3.connect("kfcstore.db")
c = conn.cursor()
```

After that, create the table **stores** for storing the *KFC stores* information.
The **CREATE TABLE** statement is executed by calling the **execute()** method of the **Cursor** object.
```python
c.execute("""CREATE TABLE IF NOT EXISTS stores (storeID INTEGER PRIMARY KEY,
            latitude REAL, longitude REAL, storeName TEXT)""")
```

Then, loop through each store record for getting and inserting the stores information to **SQLite** database. The **INSERT** statement is executed by calling the **execute()** method of the **Cursor** object.
```python
for x in range(len(stores)):
    c.execute("INSERT OR IGNORE INTO stores VALUES (?,?,?,?)",
    (stores[x]["id"], stores[x]["latitude"], stores[x]["longitude"], stores[x]["name"]))
```

## References for task 1
There are few useful references that help in accomplish the task 1:
* The [first reference](http://docs.python-requests.org/en/master/user/quickstart/) help in understanding what is *requests* and how to make a request.
* The [second reference](https://docs.python.org/2/library/json.html) is the documentation of the **Python Standard Library** for internet data handling which describe the basic usage of the **json** modules.

## Task 2
## Explanation for task 2
Task 2 is to download the *McDonald's stores json data* from [McDonald's website](https://www.mcdonalds.com.my/locate-us). The *McDonald's stores json data* was then been processed for storing into the **SQLite** database.

## Code snippets for task 2
First of all, in order to download, process, and storing the *McDonald's stores json data*, three library need to be imported which are *requests*, *json*, and *sqlite3*.

### Import library
Importing the *requests*, *json*, and *sqlite3* library.
```python
import requests
import json
import sqlite3
```

### POST request
Because it is a **POST** request, we need to send some form-encoded data to the request by passing a **dictionary** to the **data** argument. The dictionary of data will automatically be form-encoded when the request is made.
```python
payload = {
    "ajax":1,
    "action":"get_nearby_stores",
    "lat":4.210484,
    "lng":101.97576600000002
}
r = requests.post("https://www.mcdonalds.com.my/storefinder/index.php", data=payload)
```
The **payload** contains the important keys and values that are needed for getting the JSON data.

### Set encoding
The code below set the encoding of the content to be **'utf-8-sig'**. This is important because without setting the encoding to be **'utf-8-sig'** will raise an error when accessing **r.text**.
```python
r.encoding = 'utf-8-sig'
```
After setting the encoding, Requests will use the new value of **r.encoding** whenever the **r.text** is called.

### Decoding JSON data to a Python object
The code below will deserialize a **str** instance containing a JSON document to a Python object.
```python
stores = json.loads(r.text)
```

### Create SQLite Database for storing data
For storing data into **SQLite** database, we need to create a **SQLite** database and open a connection to the **SQLite** database.
```python
conn = sqlite3.connect("mcdstore.db")
c = conn.cursor()
```

After that, create the table **stores** for storing the *McDonald's stores* information. The **CREATE TABLE** statement is executed by calling the **execute()** method of the **Cursor** object.
```python
c.execute("""CREATE TABLE IF NOT EXISTS stores (storeName TEXT, address TEXT, telephone TEXT,
            email TEXT, fax TEXT, latitude REAL, longitude REAL, category TEXT)""")
```

Then, loop through each store record for getting and inserting the stores information to **SQLite** database. The **INSERT** statement is executed by calling the **execute()** method of the **Cursor** object.
```python
for s in stores["stores"]:
    list = []
    for cat in s["cat"]:
        list.append(cat["cat_name"])
    #Serialize obj to a formatted string
    l = json.dumps(list)
    #print(l)
    c.execute("INSERT OR IGNORE INTO stores VALUES (?,?,?,?,?,?,?,?)",
    (s["name"], s["address"], s["telephone"], s["email"], s["fax"], s["lat"], s["lng"], l))
```

## References for task 2
There are few useful references that help in accomplish the task 1:
* The [first reference](http://docs.python-requests.org/en/master/user/quickstart/) help in understanding what is *requests* and how to make a request.
* The [second reference](https://docs.python.org/2/library/json.html) is the documentation of the **Python Standard Library** for internet data handling which describe the basic usage of the **json** modules.
* https://examples.javacodegeeks.com/enterprise-java/selenium/selenium-ide-commands-example/
