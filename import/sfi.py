import pandas as pd
import mysql.connector


df = pd.read_csv("opendata.csv", encoding='ISO-8859-1')
df['year'] = pd.to_datetime(df['Start Date'], format='%d/%m/%Y').dt.year

df = df[['Proposal Title', 'Lead Applicant', 'year', 'Research Body', 'Programme Name', ' Current Total Commitment ']]
df.columns = ['title', 'author', 'year', 'institution', 'programme', 'amount']


conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="wsaa"
)

cursor = conn.cursor()

for index, row in df.iterrows():
    sql = "insert into researcher (title, author, year, institution, programme, amount) values (%s, %s, %s, %s, %s, %s)"
    values = (row['title'], row['author'], row['year'], row['institution'], row['programme'], row['amount']) 
    cursor.execute(sql, values)

conn.commit()
cursor.close()
conn.close()