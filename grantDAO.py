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
    
    def convertToDictionary(self, resultLine):
        attkeys=['id','title','author','year', 'institution', "programme", "amount"]
        grant = {}
        currentkey = 0
        for attrib in resultLine:
            grant[attkeys[currentkey]] = attrib
            currentkey = currentkey + 1 
        return grant

        
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
        researcher = {}
        currentkey = 0
        for attrib in resultLine:
            researcher[attkeys[currentkey]] = attrib
            currentkey = currentkey + 1 
        return researcher

# Comparison functions

    def compareResearcherAmount(self, id):
        cursor = self.getcursor()

        sql_res = "select title, author, year, institution, programme, amount from researcher where id = %s"
        cursor.execute(sql_res, (id,))
        researcher = cursor.fetchone()
        title = researcher[0]
        author = researcher[1]
        year = researcher[2]
        institution = researcher[3]
        programme = researcher[4]
        res_amount = researcher[5]

        overall_amount = "select avg(amount) from funding"
        cursor.execute(overall_amount)
        avg_funding = cursor.fetchone()
        avg_overall = avg_funding[0] if avg_funding and avg_funding[0] is not None else 0

        overall_year = "select avg(amount) from funding where year = %s"
        cursor.execute(overall_year, (year,))
        year_result = cursor.fetchone()
        year_avg = year_result[0] if year_result and year_result[0] is not None else 0

        overall_inst = "select avg(amount) from funding where institution = %s"
        cursor.execute(overall_inst, (institution,))
        inst_result = cursor.fetchone()
        inst_avg = inst_result[0] if inst_result and inst_result[0] is not None else 0

        overall_prog = "select avg(amount) from funding where programme = %s"
        cursor.execute(overall_prog, (programme,))
        prog_result = cursor.fetchone()
        prog_avg = prog_result[0] if prog_result and prog_result[0] is not None else 0

        comparison_overall = "larger" if res_amount > avg_overall else (
            "smaller" if res_amount < avg_overall else "equal"
        )
        
        comparison_year = "larger" if res_amount > year_avg else (
            "smaller" if res_amount < year_avg else "equal"
        )

        comparison_institution = "larger" if res_amount > inst_avg else (
            "smaller" if res_amount < inst_avg else "equal"
        )

        comparison_programme = "larger" if res_amount > prog_avg else (
            "smaller" if res_amount < prog_avg else "equal"
        )

        self.closeAll()
        
        return {
            'researcher': researcher,
            'title': title,
            'author': author,
            'year': year,
            'institution': institution,
            'programme': programme,
            'amount': res_amount,
            'researcher_amount': res_amount,
            'average_grant_amount': round(avg_overall, 2),
            'year_average': round(year_avg, 2),
            'institution_average': round(inst_avg, 2),
            'programme_average': round(prog_avg, 2),
            'comparison_overall': comparison_overall,
            'comparison_year': comparison_year,
            'comparison_institution': comparison_institution,
            'comparison_programme': comparison_programme
    }

researcherDAO = researcherDAO()
