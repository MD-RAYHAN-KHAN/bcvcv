import sqlite3
def studentData():
    con=sqlite3.connect("learnTOSR.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS student(id INTEGER PRIMARY KEY,StdID int, Name text,Mobile text,Age text, Coursefree int,waiver int, Paid int,Total_Due int,course_free int)")
    con.commit()
    con.close()

def addStdRec(StdID, Name,Mobile ,Catagory, Coursefree,waiver, Paid, Total_Due,course_free):
    con = sqlite3.connect("learnTOSR.db")
    cur = con.cursor()
    cur.execute("INSERT INTO student VALUES (NULL,?,?,?,?,?,?,?,?,?) ", (StdID, Name,Mobile,Catagory, Coursefree ,waiver,Paid,Total_Due,course_free))
    con.commit()
    con.close()
    
def viewData():
    con = sqlite3.connect("learnTOSR.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM student")
    rows = cur.fetchall()
    con.close()
    return rows
    
def deleteRec(id):
    con = sqlite3.connect("learnTOSR.db")
    cur = con.cursor()
    cur.execute("DELETE FROM student WHERE id=?",(id,))
    con.commit()
    con.close()
    
def searchData(StdID="", Name="", Mobile="", Catagory="", Coursefree="",waiver="", Paid="", Total_Due="",course_free=""):
    con = sqlite3.connect("learnTOSR.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM student WHERE StdID=? OR Name=? OR waiver=? OR Mobile=? OR Catagory=? OR Coursefree=? OR Paid=? OR Total_Due=? OR course_free=?",(StdID, Name,Mobile,Catagory
                                                                                                                                               , Coursefree,waiver,Paid,Total_Due,course_free))
    rows = cur.fetchall()
    con.close()
    return rows
    
def dataUpdate(id,StdID="", Name="",Mobile="", Catagory="", Coursefree="",waiver="", Paid="", Total_Due="",course_free=""):
    con = sqlite3.connect("learnTOSR.db")
    cur = con.cursor()
    cur.execute("UPDATE student SET StdID=?, Name=?, Mobile=?,Catagory=?,Paid=?Total_Due=?, course_free=?,WHERE id=?,", (StdID, Name,Mobile, Catagory, Coursefree,waiver, Paid, Total_Due,course_free, id))
    con.commit()
    con.close()



studentData()
