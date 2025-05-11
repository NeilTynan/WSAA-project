import pandas as pd
import mysql.connector


df = pd.read_csv("opendata.csv", encoding='ISO-8859-1')


df = df[['Proposal Title', 'Lead Applicant', 'Research Body', 'Programme Name', ' Current Total Commitment ']]
df.columns = ['title', 'author', 'institution', 'programme', 'amount']


conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="wsaa"
)

cursor = conn.cursor()

for index, row in df.iterrows():
    sql = "INSERT INTO funding (title, author, institution, programme, amount) VALUES (%s, %s, %s, %s, %s)"
    values = (row['title'], row['author'], row['institution'], row['programme'], row['amount']) 
    cursor.execute(sql, values)

conn.commit()
cursor.close()
conn.close()