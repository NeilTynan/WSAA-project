import pandas as pd
import mysql.connector
import dbconfig as cfg


df = pd.read_csv("opendata.csv", encoding='ISO-8859-1')
df['year'] = pd.to_datetime(df['Start Date'], format='%d/%m/%Y').dt.year

df = df[['Proposal Title', 'Lead Applicant', 'year', 'Research Body', 'Programme Name', ' Current Total Commitment ']]
df.columns = ['title', 'author', 'year', 'institution', 'programme', 'amount']
df = df.where(pd.notnull(df), None)

conn = mysql.connector.connect(
    host=cfg.mysql['host'],
    user=cfg.mysql['user'],
    password=cfg.mysql['password'],
    database=cfg.mysql['database']
)

cursor = conn.cursor()

for index, row in df.iterrows():
    sql = "insert into researcher (title, author, year, institution, programme, amount) values (%s, %s, %s, %s, %s, %s)"
    values = (row['title'], row['author'], row['year'], row['institution'], row['programme'], row['amount']) 
    cursor.execute(sql, values)

self.commit()
cursor.close()
self.close()