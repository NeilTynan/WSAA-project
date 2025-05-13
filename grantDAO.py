#libraries
import mysql.connector
import dbconfig as cfg

#grantDAO()
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
    
    def convertToDictionary(self, resultLine):
        attkeys=['id','title','author','year', 'institution', "programme", "amount"]
        book = {}
        currentkey = 0
        for attrib in resultLine:
            book[attkeys[currentkey]] = attrib
            currentkey = currentkey + 1 
        return book

        
grantDAO = grantDAO()

# researcherDAO
class researcherDAO:
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
         
    def getAllResearcher(self):
        cursor = self.getcursor()
        sql="select * from researcher"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        #print(results)
        for result in results:
            #print(result)
            returnArray.append(self.convertToDictionaryResearcher(result))
        
        self.closeAll()
        return returnArray

    def findByIDResearcher(self, id):
        cursor = self.getcursor()
        sql="select * from researcher where id = %s"
        values = (id,)

        cursor.execute(sql, values)
        result = cursor.fetchone()
        returnvalue = self.convertToDictionaryResearcher(result)
        self.closeAll()
        return returnvalue

    def createResearcher(self, researcher):
        cursor = self.getcursor()
        sql="insert into researcher (title, author, year, institution, programme, amount) values (%s,%s,%s,%s,%s,%s)"
        values = (researcher.get("title"), researcher.get("author"), researcher.get("year"), researcher.get("institution"), researcher.get("programme"), researcher.get("amount"))
        cursor.execute(sql, values)

        self.connection.commit()
        newid = cursor.lastrowid
        researcher["id"] = newid
        self.closeAll()
        return researcher


    def updateResearcher(self, id, researcher):
        cursor = self.getcursor()
        sql="update researcher set title= %s, author=%s, year=%s, institution=%s, programme=%s, amount=%s  where id = %s"
        values = (researcher.get("title"), researcher.get("author"), researcher.get("year"), researcher.get("institution"), researcher.get("programme"), researcher.get("amount"),id)
        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()
        
    def deleteResearcher(self, id):
        cursor = self.getcursor()
        sql="delete from researcher where id = %s"
        values = (id,)

        cursor.execute(sql, values)

        self.connection.commit()
        self.closeAll()
        
        print("delete done")

    def convertToDictionaryResearcher(self, resultLine):
        attkeys=['id', 'title', 'author', 'year', 'institution', "programme", "amount"]
        book = {}
        currentkey = 0
        for attrib in resultLine:
            book[attkeys[currentkey]] = attrib
            currentkey = currentkey + 1 
        return book

# Comparison functions

    def compareResearcherAmount(self, id):
        cursor = self.getcursor()

        sql_res = "select amount, year, institution, programme from researcher where id = %s"
        cursor.execute(sql_res, (id,))
        researcher = cursor.fetchone()
        res_amount = researcher[0]
        year = researcher[1]
        institution = researcher[2]
        programme = researcher[3]

        overall_amount = "select avg(amount) from funding"
        cursor.execute(overall_amount)
        avg_funding = cursor.fetchone()
        avg_overall = avg_funding[0]

        overall_year = "select avg(amount) from funding where year = %s"
        cursor.execute(overall_year, (year,))
        year_result = cursor.fetchone()
        year_avg = year_result[0]

        overall_inst = "select avg(amount) from funding where institution = %s"
        cursor.execute(overall_inst, (institution,))
        inst_result = cursor.fetchone()
        inst_avg = inst_result[0]

        overall_prog = "select avg(amount) from funding where programme = %s"
        cursor.execute(overall_prog, (programme,))
        prog_result = cursor.fetchone()
        prog_avg = prog_result[0]

        comparison_overall = "above average" if res_amount > avg_overall else (
            "below average" if res_amount < avg_overall else "equal to average"
        )
        
        comparison_year = "above average" if res_amount > year_avg else (
            "below average" if res_amount < year_avg else "equal to average"
        )

        comparison_institution = "above average" if res_amount > inst_avg else (
            "below average" if res_amount < inst_avg else "equal to average"
        )

        comparison_programme = "above average" if res_amount > prog_avg else (
            "below average" if res_amount < prog_avg else "equal to average"
        )

        self.closeAll()
        
        return {
            'researcher_amount': res_amount,
            'average_grant_amount': avg_overall,
            'year_average': year_avg,
            'institution_average': inst_avg,
            'programme_average': prog_avg,
            'comparison_overall': comparison_overall,
            'comparison_year': comparison_year,
            'comparison_institution': comparison_institution,
            'comparison_programme': comparison_programme
    }


        
researcherDAO = researcherDAO()
