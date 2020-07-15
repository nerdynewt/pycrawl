#!/bin/env python3

import mysql.connector


mydb = mysql.connector.connect(
        host = "localhost",
        user = "vishnu",
        password = "CrapWeasel",
        database = "search_index"
        )

mycursor = mydb.cursor()

def add(url, title, content):
    if not url or not title or not content:
        return False
    sql = "INSERT INTO search_index (url, title, content) VALUES (%s, %s, %s)"
    val = (url, title, content)
    mycursor.execute(sql, val)
    mydb.commit()
    return True
