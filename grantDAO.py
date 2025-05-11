import mysql.connector
import dbconfig as cfg
class grantDAO:
    connection=""
    cursor =''
    host=       ''
    user=       ''
    password=   ''
    database=   ''

#config file
    def __init__(self):
        self.host=       cfg.mysql['host']
        self.user=       cfg.mysql['user']
        self.password=   cfg.mysql['password']
        self.database=   cfg.mysql['database']

    def getcursor(self): 
        self.connection = mysql.connector.connect(
            host=       self.host,
            user=       self.user,
            password=   self.password,
            database=   self.database,
        )
        self.cursor = self.connection.cursor()
        return self.cursor

    def closeAll(self):
        self.connection.close()
        self.cursor.close()
         
    def getAll(self):
        cursor = self.getcursor()
        sql="select * from funding"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        #print(results)
        for result in results:
            #print(result)
            returnArray.append(self.convertToDictionary(result))
        
        self.closeAll()
        return returnArray

    def findByID(self, id):
        cursor = self.getcursor()
        sql="select * from funding where id = %s"
        values = (id,)

        cursor.execute(sql, values)
        result = cursor.fetchone()
        returnvalue = self.convertToDictionary(result)
        self.closeAll()
        return returnvalue

    def create(self, grant):
        cursor = self.getcursor()
        sql="insert into funding (title, author, institution, amount) values (%s,%s,%s,%s,%s)"
        values = (grant.get("title"), grant.get("author"), grant.get("institution"), grant.get("programme"), grant.get("amount"))
        cursor.execute(sql, values)

        self.connection.commit()
        newid = cursor.lastrowid
        grant["id"] = newid
        self.closeAll()
        return grant


    def update(self, id, grant):
        cursor = self.getcursor()
        sql="update funding set title= %s,author=%s, institution=%s, programme=%s, amount=%s  where id = %s"
        
        values = (grant.get("title"), grant.get("author"), grant.get("institution"), grant.get("programme"), grant.get("amount"),id)
        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()
        
    def delete(self, id):
        cursor = self.getcursor()
        sql="delete from funding where id = %s"
        values = (id,)

        cursor.execute(sql, values)

        self.connection.commit()
        self.closeAll()
        
        print("delete done")

    def convertToDictionary(self, resultLine):
        attkeys=['id','title','author', 'institution', "programme", "amount"]
        book = {}
        currentkey = 0
        for attrib in resultLine:
            book[attkeys[currentkey]] = attrib
            currentkey = currentkey + 1 
        return book

        
grantDAO = grantDAO()