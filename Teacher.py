from tkinter import *
import tkinter.messagebox
import TeacherBackend
class Teacher:

    def __init__(self,root):
        self.root =root
        self.root.title("SR IT SOLUTION")
        self.root.geometry("1350x750+0+0")
        self.root.config(bg="cadet blue")

        StdID = StringVar()
        Firstname = StringVar()
        Mobile = StringVar()
        DoB = StringVar()
        Catagory = StringVar()
        
        Coursefree = StringVar()
        Paid = StringVar()
        Total_Due = StringVar()
        
# FUNCTIONS
        def iExit():
            iExit = tkinter.messagebox.askyesno("SR Student Management System", "Confirm if you want to exit")
            if iExit > 0:
                root.destroy()
        '''        return
        def clearData():
            #ClearData = tkinter.messagebox.askokcancel("SR Student Management System", "Clear the Data")
            response = tkinter.messagebox.askokcancel("SR Student Management System", "OK or Cancel?")
            if response == "OK":
                def clearData():   
                    self.txtStdID.delete(0, END)
                    self.txtfna.delete(0, END)
                    self.txtSna.delete(0, END)
                    self.txtDoB.delete(0, END)
                    self.txtCatagory.delete(0, END)
                    self.txtCoursefree.delete(0, END)
                    self.txtPaid.delete(0, END)
                    self.txtTotal_Due.delete(0, END)
                   
        '''    
        def clearData():   
            self.txtStdID.delete(0, END)
            self.txtfna.delete(0, END)
            self.txtSna.delete(0, END)
            self.txtDoB.delete(0, END)
            self.txtCatagory.delete(0, END)
            self.txtCoursefree.delete(0, END)
            self.txtPaid.delete(0, END)
            self.txtTotal_Due.delete(0, END)
            
        
            clearData = tkinter.messagebox("SR Student Management System", "Clear the Data")
        
        
            
        def addData():
            if(len(StdID.get())!=0):
                TeacherBackend.addStdRec(StdID.get(), Firstname.get(), Mobile.get() , DoB.get() ,Catagory.get(), Coursefree.get(), Paid.get(), Total_Due.get())
                studentlist.delete(0, END)
                studentlist.insert(END, (StdID.get(), Firstname.get(), Mobile.get(), DoB.get(), Catagory.get(), Coursefree.get(), Paid.get(), Mobile.get()))

        def DisplayData():
            studentlist.delete(0,END)
            for row in TeacherBackend.viewData():
                studentlist.insert(END, row, str(""))

        def StudentRec(event):
            global sd
            searchStd= studentlist.curselection()[0]
            sd = studentlist.get(searchStd)

            self.txtStdID.delete(0, END)
            self.txtStdID.insert(END, sd[1])
            self.txtfna.delete(0, END)
            self.txtfna.insert(END, sd[2])
            self.txtSna.delete(0, END)
            self.txtSna.insert(END, sd[3])
            self.txtDoB.delete(0, END)
            self.txtDoB.insert(END, sd[4])
            self.txtCatagory.delete(0, END)
            self.txtCatagory.insert(END, sd[5])
            self.txtCoursefree.delete(0, END)
            self.txtCoursefree.insert(END, sd[6])
            self.txtPaid.delete(0, END)
            self.txtPaid.insert(END, sd[7])
            self.txtTotal_Due.delete(0, END)
            self.txtTotal_Due.insert(END, sd[8])
            
        """
        def DeleteData():
            response = tkinter.messagebox.askokcancel("SR Student Management System", "Delete Data?")
            if response == "OK":
                def clearData():   
                    if(len(StdID.get())!=0):
                        TeacherBackend.deleteRec(sd[0])
                        clearData()
                        DisplayData()
        """         
        def DeleteData():
            if(len(StdID.get())!=0):
                TeacherBackend.deleteRec(sd[0])
                clearData()
                DisplayData()
        
        def searchDatabase():
            studentlist.delete(0,END)
            for row in TeacherBackend.searchData(StdID.get(), Firstname.get(), Mobile.get() , DoB.get() ,Catagory.get(), Coursefree.get(), Paid.get(), Total_Due.get()):
                studentlist.insert(END, row, str(""))

        def update():
            if (len(StdID.get()) != 0):
                TeacherBackend.deleteRec(sd[0])
            if (len(StdID.get()) != 0):
                TeacherBackend.addStdRec(StdID.get(), Firstname.get(), Mobile.get(), DoB.get(), Catagory.get(), Coursefree.get(),Paid.get(), Total_Due.get())
                studentlist.delete(0, END)
                studentlist.insert(END, (StdID.get(), Firstname.get(), Mobile.get(), DoB.get(), Catagory.get(), Coursefree.get(), Paid.get(), Total_Due.get()))
            ########
            tkinter.messagebox.update("update", "Successfully Uploaded!")
#Frames
        MainFrame = Frame(self.root, bg="cadet blue")
        MainFrame.grid()
        TitFrame = Frame(MainFrame, bd=2, padx=54,pady=8, bg="Ghost White", relief=RIDGE)
        TitFrame.pack(side=TOP)
        self.lblTit = Label(TitFrame ,font=('times new roman',48,'bold'),text="SR Student Management System",bg="Ghost White")
        self.lblTit.grid()
        ButtonFrame =Frame(MainFrame,bd=2,width=1350,height=70,padx=19,pady=10,bg="Ghost White",relief =RIDGE)
        ButtonFrame.pack(side=BOTTOM)
        DataFrame = Frame(MainFrame, bd=1, width=1300, height=400, padx=20, pady=20, relief=RIDGE,bg="cadet blue")
        DataFrame.pack(side=BOTTOM)
        DataFrameLEFT = LabelFrame(DataFrame, bd=1, width=1000, height=600, padx=20,relief=RIDGE,bg="Ghost White", font=('times new roman',26,'bold'),text="  Teacher Info\n")
        DataFrameLEFT.pack(side=LEFT)
        DataFrameRIGHT = LabelFrame(DataFrame, bd=1, width=450, height=300, padx=31, pady=3, relief=RIDGE,bg="Ghost White",font=('times new roman',20,'bold'),text="          Display Teacher Info\n")
        DataFrameRIGHT.pack(side=RIGHT)
#Entries
        self.lblStdID = Label(DataFrameLEFT, font=('times new roman', 20, 'bold'), text="Teacher ID:",padx=2,pady=2,bg="Ghost White")
        self.lblStdID.grid(row=0,column=0,sticky=W)
        self.txtStdID = Entry(DataFrameLEFT, font=('times new roman', 20, 'bold'), textvariable=StdID, width=39)
        self.txtStdID.grid(row=0, column=1)

        self.lblfna = Label(DataFrameLEFT, font=('times new roman', 20, 'bold'), text="Teachername:", padx=2, pady=2,bg="Ghost White")
        self.lblfna.grid(row=1, column=0, sticky=W)
        self.txtfna = Entry(DataFrameLEFT, font=('times new roman', 20, 'bold'), textvariable=Firstname, width=39)
        self.txtfna.grid(row=1, column=1)

        self.lblDoB = Label(DataFrameLEFT, font=('times new roman', 20, 'bold'), text="Email:", padx=2, pady=2,bg="Ghost White")
        self.lblDoB.grid(row=2, column=0, sticky=W)
        self.txtDoB = Entry(DataFrameLEFT, font=('times new roman', 20, 'bold'), textvariable=DoB, width=39)
        self.txtDoB.grid(row=2, column=1)

        self.lblCatagory = Label(DataFrameLEFT, font=('times new roman', 20, 'bold'), text="Catagory:", padx=2, pady=2,bg="Ghost White")
        self.lblCatagory.grid(row=3, column=0, sticky=W)
        self.txtCatagory = Entry(DataFrameLEFT, font=('times new roman', 20, 'bold'), textvariable=Catagory, width=39)
        self.txtCatagory.grid(row=3, column=1)

        self.lblCoursefree = Label(DataFrameLEFT, font=('times new roman', 20, 'bold'), text="MonthSalary:", padx=2, pady=2,bg="Ghost White")
        self.lblCoursefree.grid(row=4, column=0, sticky=W)
        self.txtCoursefree = Entry(DataFrameLEFT, font=('times new roman', 20, 'bold'), textvariable=Coursefree, width=39)
        self.txtCoursefree.grid(row=4, column=1)

        self.lblSna = Label(DataFrameLEFT, font=('times new roman', 20, 'bold'), text="Income Tax :", padx=2, pady=2,bg="Ghost White")
        self.lblSna.grid(row=5, column=0, sticky=W)
        self.txtSna = Entry(DataFrameLEFT, font=('times new roman', 20, 'bold'), textvariable= Mobile, width=39)
        self.txtSna.grid(row=5, column=1)

        self.lblPaid = Label(DataFrameLEFT, font=('times new roman', 20, 'bold'), text="Salary Paid:", padx=2, pady=2,bg="Ghost White")
        self.lblPaid.grid(row=6, column=0, sticky=W)
        self.txtPaid = Entry(DataFrameLEFT, font=('times new roman', 20, 'bold'), textvariable=Paid, width=39)
        self.txtPaid.grid(row=6, column=1)

        self.lblTotal_Due = Label(DataFrameLEFT, font=('times new roman', 20, 'bold'), text="Salary Due:", padx=2, pady=2,bg="Ghost White")
        self.lblTotal_Due.grid(row=7, column=0, sticky=W)
        self.txtTotal_Due = Entry(DataFrameLEFT, font=('times new roman', 20, 'bold'), textvariable= Total_Due, width=39)
        self.txtTotal_Due.grid(row=7, column=1)
        
#Scroll bar and list box
        scrollbar= Scrollbar(DataFrameRIGHT)
        scrollbar.grid(row=0,column=1,sticky='ns')

        studentlist = Listbox(DataFrameRIGHT, width=41, height=16, font=('times new roman', 12, 'bold'),yscrollcommand=scrollbar.set)
        studentlist.bind('<<ListboxSelect>>',StudentRec)
        studentlist.grid(row=0, column=0, padx=8)
        scrollbar.config(command=studentlist.yview)
#buttons
        self.btnAddData = Button(ButtonFrame, text="Add New", font=('times new roman', 20, 'bold'), height=1, width=10, bd=4, command=addData)
        self.btnAddData.grid(row=0, column =0)

        self.btnDisplayData = Button(ButtonFrame, text="Display", font=('times new roman', 20, 'bold'), height=1, width=10, bd=4, command=DisplayData)
        self.btnDisplayData.grid(row=0, column=1)

        self.btnClearData = Button(ButtonFrame, text="Clear", font=('times new roman', 20, 'bold'), height=1, width=10, bd=4,command=clearData)
        self.btnClearData.grid(row=0, column=2)

        self.btnDeleteData = Button(ButtonFrame, text="Delete", font=('times new roman', 20, 'bold'), height=1, width=10, bd=4,command=DeleteData)
        self.btnDeleteData.grid(row=0, column=3)

        self.btnSearchData = Button(ButtonFrame, text="Search", font=('times new roman', 20, 'bold'), height=1, width=10, bd=4,command=searchDatabase)
        self.btnSearchData.grid(row=0, column=4)

        self.btnUpdateData = Button(ButtonFrame, text="Update", font=('times new roman', 20, 'bold'), height=1, width=10, bd=4,command=update)
        self.btnUpdateData.grid(row=0, column=5)

        self.btnExit = Button(ButtonFrame, text="Exit", font=('times new roman', 20, 'bold'), height=1, width=10, bd=4, command=iExit)
        self.btnExit.grid(row=0, column=6)
        
        self.btnStudent = Button(ButtonFrame, text="Student", font=('times new roman', 20, 'bold'), height=1, width=10, bd=4)
        self.btnStudent.grid(row=1, column=2)
        
        self.btnTeacher = Button(ButtonFrame, text="Teacher", font=('times new roman', 20, 'bold'), height=1, width=10, bd=4)
        self.btnTeacher.grid(row=1, column=3)
        
        self.btnLogout = Button(ButtonFrame, text="Logout", font=('times new roman', 20, 'bold'), height=1, width=10, bd=4)
        self.btnLogout.grid(row=1, column=4)

if __name__=='__main__':
    root = Tk()
    application = Teacher(root)
    root.mainloop()
