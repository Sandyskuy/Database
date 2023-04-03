#!/usr/bin/env python
# coding: utf-8

# In[1]:


import mysql.connector

dataBase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = ""
)

cursorObject = dataBase.cursor()
cursorObject.execute("CREATE DATABASE D3_TI_2023")


# In[3]:


import mysql.connector

dataBase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "D3_TI_2023"
)

cursorObject = dataBase.cursor()
studentRecord = """CREATE TABLE mahasiswa (
                    NIM VARCHAR(10) PRIMARY KEY NOT NULL,
                    NAMA VARCHAR(30) NOT NULL,
                    ALAMAT VARCHAR(255) NOT NULL,
                    MATA_KULIAH VARCHAR(50) NOT NULL
                    )"""
cursorObject.execute(studentRecord)


# In[4]:


import mysql.connector

dataBase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "D3_TI_2023"
)

cursorObject = dataBase.cursor()
studentRecord = """CREATE TABLE dosen (
                    NIP VARCHAR(20) PRIMARY KEY NOT NULL,
                    NAMA_DOSEN VARCHAR(50) NOT NULL,
                    MATA_KULIAH VARCHAR(50) NOT NULL
                    )"""
cursorObject.execute(studentRecord)


# In[5]:


import mysql.connector

dataBase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "D3_TI_2023"
)

cursorObject = dataBase.cursor()
studentRecord = """CREATE TABLE mata_kuliah (
                    KODE_MATKUL VARCHAR(10) PRIMARY KEY NOT NULL,
                    NAMA VARCHAR(50) NOT NULL,
                    WAKTU DATE NOT NULL,
                    RUANGAN VARCHAR(10) NOT NULL
                    )"""
cursorObject.execute(studentRecord)


# In[7]:


import mysql.connector

dataBase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "D3_TI_2023"
)

cursorObject = dataBase.cursor()
sql = "INSERT INTO mahasiswa(NIM, NAMA, ALAMAT, MATA_KULIAH)VALUES(%s, %s, %s, %s)"
val = [("V3922051", "Budi", "Surabaya", "Wireless"), 
       ("V3922050", "Siti", "Bandung", "Statistika"),
       ("V3922049", "Aisyah", "Jember", "Mikrokontroler"),
       ("V3922048", "Ario", "Surabaya", "Web"),
       ("V3922047", "wudi", "Madiun", "Wireless")
      ]

cursorObject.executemany(sql, val)
dataBase.commit()


# In[8]:


import mysql.connector

dataBase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "D3_TI_2023"
)

cursorObject = dataBase.cursor()
query = "SELECT * FROM mahasiswa"
cursorObject.execute(query)

myresult = cursorObject.fetchall()

for x in myresult:
    print(x)
    
dataBase.close()


# In[12]:


import mysql.connector

dataBase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "D3_TI_2023"
)

cursorObject = dataBase.cursor()
sql = "INSERT INTO dosen(NIP, NAMA_DOSEN, MATA_KULIAH)VALUES(%s, %s, %s)"
val = [("1999757865", "Alika", "Wireless"), 
       ("1847489433", "Wahyu", "Statistika"),
       ("1987637993", "Tirta", "Mikrokontroler"),
       ("1987637389", "Coki", "Web"),
       ("1876368389", "Windah", "Wireless")
      ]

cursorObject.executemany(sql, val)
dataBase.commit()


# In[13]:


import mysql.connector

dataBase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "D3_TI_2023"
)

cursorObject = dataBase.cursor()
query = "SELECT * FROM dosen"
cursorObject.execute(query)

myresult = cursorObject.fetchall()

for x in myresult:
    print(x)
    
dataBase.close()


# In[14]:


import mysql.connector

dataBase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "D3_TI_2023"
)

cursorObject = dataBase.cursor()
sql = "INSERT INTO mata_kuliah(KODE_MATKUL, NAMA, WAKTU, RUANGAN)VALUES(%s, %s, %s, %s)"
val = [("87343", "Wireless", "2023-05-19", "Lab-1"), 
       ("83478", "Mikrokontroler", "2023-05-15", "Lab-3"),
       ("87344", "Statistika", "2023-05-19", "Lab-2"),
       ("87340", "Web", "2023-05-16", "Lab-1"),
       ("87334", "Basis Data", "2023-05-15", "Lab-3")
      ]

cursorObject.executemany(sql, val)
dataBase.commit()


# In[15]:


import mysql.connector

dataBase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "D3_TI_2023"
)

cursorObject = dataBase.cursor()
query = "SELECT * FROM mata_kuliah"
cursorObject.execute(query)

myresult = cursorObject.fetchall()

for x in myresult:
    print(x)
    
dataBase.close()


# In[ ]:




