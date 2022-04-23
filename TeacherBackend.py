
import sqlite3
def TeacherData():
    con=sqlite3.connect("teacher.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS teacher(id INTEGER PRIMARY KEY,StdID text, Firstname text, Mobile text, DoB text,Age text, Coursefree text,Paid text,Total_Due int)")
    con.commit()
    con.close()

def addStdRec(StdID, Firstname, Mobile , DoB ,Catagory, Coursefree, Paid, Total_Due):
    con = sqlite3.connect("teacher.db")
    cur = con.cursor()
    cur.execute("INSERT INTO teacher VALUES (NULL,?,?,?,?,?,?,?,?) ", (StdID, Firstname,Mobile,DoB,Catagory, Coursefree ,Paid,Total_Due))
    con.commit()
    con.close()
    
def viewData():
    con = sqlite3.connect("teacher.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM teacher")
    rows = cur.fetchall()
    con.close()
    return rows
    
def deleteRec(id):
    con = sqlite3.connect("teacher.db")
    cur = con.cursor()
    cur.execute("DELETE FROM teacher WHERE id=?",(id,))
    con.commit()
    con.close()
    
def searchData(StdID="", Firstname="", Mobile="",DoB="", Catagory="", Coursefree="", Paid="", Total_Due=""):
    con = sqlite3.connect("teacher.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM teacher WHERE StdID=? OR Firstname=? OR Mobile=? OR DoB=? OR Catagory=? OR Coursefree=? OR Paid=? OR Total_Due=?",(StdID, Firstname,Mobile,DoB,Catagory
                                                                                                                                               , Coursefree,Paid,Total_Due))
    rows = cur.fetchall()
    con.close()
    return rows
    
def dataUpdate(id,StdID="", Firstname="", Mobile="",DoB="", Catagory="", Coursefree="", Paid="", Total_Due=""):
    con = sqlite3.connect("teacher.db")
    cur = con.cursor()
    cur.execute("UPDATE teacher SET StdID=?, Firstname=?, DoB=?,Catagory=?,Paid=?Total_Due=?,WHERE id=?", (StdID, Firstname, Mobile, DoB, Catagory, Coursefree, Paid, Total_Due, id))
    con.commit()
    con.close()

TeacherData()
