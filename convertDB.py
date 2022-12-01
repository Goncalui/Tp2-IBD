import io
import sqlite3
import pandas as pd

f = io.open('consult.db', 'w', encoding='utf-8')
f.close()

conn = sqlite3.connect('consult.db')
cursor = conn.cursor()

f = io.open('BancoDeDados.sql', 'r', encoding='utf-8')
sql = f.read()
print(sql)
cursor.executescript(sql)