#Python 2.7.0
#William Skagerstrom, Teodor Karlgren

from Tkinter import Tk, Text, TOP, BOTH, X, N, LEFT
from Tkinter import *
from ttk import Frame, Label, Entry
from ttk import *
import main


class doctorForm(Frame):

    def __init__(self, parent, conn, doctorTeam):
        Frame.__init__(self, parent)

        self.parent = parent
        self.doctorTeam = doctorTeam
        self.conn = conn
        self.initUI()


    def quit(self):
        self.parent.destroy()

    def logPatient(self):
        values = self.getInfo()
        main.logPatient(self.conn, values)

    def initUI(self):

        self.parent.title("Doctor Form")
        self.parent.geometry("700x700+300+300")
        self.pack(fill=BOTH, expand=True)

        #print(self.doctorTeam)


        formInfo = (main.top(self.conn, self.doctorTeam))[0]
        cname = formInfo[0]
        cpnum = formInfo[1]
        cgender = formInfo[2]
        cage = formInfo[3]
        carrival = formInfo[5]
        cissue = formInfo[6]
        cprio =  formInfo[7]
        cteamid = formInfo[8]





        entry = Entry(self)
        quitButton = Button(self, text ="Exit", command=self.quit)
        quitButton.pack(side=BOTTOM, pady = 10)

        queueButton = Button(self,text="Checkout", command=self.logPatient)
        queueButton.pack(side=BOTTOM, pady = 20)


        frame1 = Frame(self)
        frame1.pack(fill=X)

        lbl1 = Label(frame1, text="Name", width=8)
        lbl1.pack(side=LEFT, padx=5, pady=5)

        self.entry1 = Entry(frame1)
        self.entry1.pack(fill=X, padx=5, expand=True)
        self.entry1.insert(INSERT, cname)


        pNumber = Frame(self)
        pNumber.pack(fill=X)
        pNumberLabel = Label(pNumber, text= "Person ID", width=8 )
        pNumberLabel.pack(side=LEFT, padx=5, pady=5)

        self.pNumberEntry = Entry(pNumber)
        self.pNumberEntry.pack(fill=X, padx=5, expand=True)
        self.pNumberEntry.insert(INSERT, cpnum)



        timeFrame = Frame(self)
        timeFrame.pack(fill=X)

        timeLabel = Label(timeFrame, text="TOA", width=8)
        timeLabel.pack(side=LEFT, padx=5, pady=5)

        self.timeEntry = Entry(timeFrame)
        self.timeEntry.pack(fill=X, padx=5, expand=True)
        self.timeEntry.insert(INSERT, carrival)


        teamFrame = Frame(self)
        teamFrame.pack(fill=X)
        teamLabel = Label(teamFrame, text="Handled by team:", width=15)
        teamLabel.pack(side=LEFT, padx=5, pady=5)

        self.teamEntry = Entry(teamFrame)
        self.teamEntry.pack(fill=X, padx=5, expand=True)
        self.teamEntry.insert(INSERT, cteamid)

        frame2 = Frame(self)
        frame2.pack(fill=X)

        lbl2 = Label(frame2, text="Age", width=8)
        lbl2.pack(side=LEFT, padx=5, pady=5)

        self.entry2 = Entry(frame2)
        self.entry2.pack(fill=X, padx=5, expand=True)
        self.entry2.insert(INSERT, cage)


        gender = Frame(self)
        gender.pack(fill=X)
        genderLabel = Label(gender, text="Gender", width=8)
        genderLabel.pack(side=LEFT, padx=0, pady= 0)

        self.genderChoice = StringVar()

        self.gender = Radiobutton(gender, text="Male", variable=self.genderChoice, value = 'M').pack(side=LEFT, padx = 0, pady=0)
        self.gender = Radiobutton(gender, text="Female", variable=self.genderChoice, value = 'F').pack(side=LEFT, padx = 0, pady=0)
        self.genderChoice.set(cgender)





        frame3 = Frame(self)
        frame3.pack(fill=X)


        lbl3 = Label(frame3, text="Priority", width=8)
        lbl3.pack(side=LEFT, padx=5, pady=0)

        self.entry3 = Entry(frame3)
        self.entry3.pack(side=LEFT , padx=5, pady=5)
        self.entry3.insert(INSERT, cprio)



        frame4 = Frame(self)
        frame4.pack(fill=X)

        lbl5 = Label(frame4, text="Treatments", width = 8)
        lbl5.pack(side=LEFT, padx = 5, pady = 5)

        treatments = ["Proc1","Proc2","Proc3","Proc4", "Proc5","Proc6","Proc7","Proc8","Proc9","Proc10"]


        self.treatment1=BooleanVar()
        self.treatment2=BooleanVar()
        self.treatment3=BooleanVar()
        self.treatment4=BooleanVar()
        self.treatment5=BooleanVar()
        self.treatment6=BooleanVar()
        self.treatment7=BooleanVar()
        self.treatment8=BooleanVar()
        self.treatment9=BooleanVar()
        self.treatment10=BooleanVar()

        self.entry4 = Checkbutton(frame4, text=treatments[0], variable=self.treatment1).pack(side=LEFT, padx = 0, pady=0, expand=True)
        self.entry4 = Checkbutton(frame4, text=treatments[1], variable=self.treatment2).pack(side=LEFT, padx = 0, pady=0, expand=True)
        self.entry4 = Checkbutton(frame4, text=treatments[2], variable=self.treatment3).pack(side=LEFT, padx = 0, pady=0, expand=True)
        self.entry4 = Checkbutton(frame4, text=treatments[3], variable=self.treatment4).pack(side=LEFT, padx = 0, pady=0, expand=True)
        self.entry4 = Checkbutton(frame4, text=treatments[4], variable=self.treatment5).pack(side=LEFT, padx = 0, pady=0, expand=True)
        self.entry4 = Checkbutton(frame4, text=treatments[5], variable=self.treatment6).pack(side=LEFT, padx = 0, pady=0, expand=True)
        self.entry4 = Checkbutton(frame4, text=treatments[6], variable=self.treatment7).pack(side=LEFT, padx = 0, pady=0, expand=True)
        self.entry4 = Checkbutton(frame4, text=treatments[7], variable=self.treatment8).pack(side=LEFT, padx = 0, pady=0, expand=True)
        self.entry4 = Checkbutton(frame4, text=treatments[8], variable=self.treatment9).pack(side=LEFT, padx = 0, pady=0, expand=True)
        self.entry4 = Checkbutton(frame4, text=treatments[9], variable=self.treatment10).pack(side=LEFT, padx = 0, pady=0, expand=True)



        frame5 = Frame(self)
        frame5.pack(fill=X)

        lbl5 = Label(frame5, text="Drugs", width = 8)
        lbl5.pack(side=LEFT, padx = 5, pady = 5)

        drugs = ["Drug1","Drug2","Drug3","Drug4", "Drug5","Drug6","Drug7","Drug8","Drug9","Drug10"]


        self.drug1=BooleanVar()
        self.drug2=BooleanVar()
        self.drug3=BooleanVar()
        self.drug4=BooleanVar()
        self.drug5=BooleanVar()
        self.drug6=BooleanVar()
        self.drug7=BooleanVar()
        self.drug8=BooleanVar()
        self.drug9=BooleanVar()
        self.drug10=BooleanVar()

        self.entry4 = Checkbutton(frame5, text=drugs[0], variable=self.drug1).pack(side=LEFT, padx = 0, pady=0, expand=True)
        self.entry4 = Checkbutton(frame5, text=drugs[1], variable=self.drug2).pack(side=LEFT, padx = 0, pady=0, expand=True)
        self.entry4 = Checkbutton(frame5, text=drugs[2], variable=self.drug3).pack(side=LEFT, padx = 0, pady=0, expand=True)
        self.entry4 = Checkbutton(frame5, text=drugs[3], variable=self.drug4).pack(side=LEFT, padx = 0, pady=0, expand=True)
        self.entry4 = Checkbutton(frame5, text=drugs[4], variable=self.drug5).pack(side=LEFT, padx = 0, pady=0, expand=True)
        self.entry4 = Checkbutton(frame5, text=drugs[5], variable=self.drug6).pack(side=LEFT, padx = 0, pady=0, expand=True)
        self.entry4 = Checkbutton(frame5, text=drugs[6], variable=self.drug7).pack(side=LEFT, padx = 0, pady=0, expand=True)
        self.entry4 = Checkbutton(frame5, text=drugs[7], variable=self.drug8).pack(side=LEFT, padx = 0, pady=0, expand=True)
        self.entry4 = Checkbutton(frame5, text=drugs[8], variable=self.drug9).pack(side=LEFT, padx = 0, pady=0, expand=True)
        self.entry4 = Checkbutton(frame5, text=drugs[9], variable=self.drug10).pack(side=LEFT, padx = 0, pady=0, expand=True)





        frame6 = Frame(self)
        frame6.pack(fill=X)

        lbl6 = Label(frame6, text=" ", width = 8)
        lbl6.pack(side=LEFT, padx = 5, pady = 5)



        self.where=BooleanVar()


        self.entry6 = Radiobutton(frame6, text="Send home", variable=self.where, value=0).pack(side=LEFT, padx = 0, pady=0)
        self.entry6 = Radiobutton(frame6, text="Send for further treatment", variable=self.where, value=1).pack(side=LEFT, padx = 0, pady=0)





    def getInfo(self):
        #name, pnum, gender, age, prio, timearrival, senthome, treamtents, drugs
        return([self.entry1.get(),self.pNumberEntry.get(),self.genderChoice.get(), self.entry2.get(),int(self.entry3.get()),str(self.timeEntry.get()), self.where.get(), self.getTreatments(), self.getDrugs()])

    def onScale(self,val):
        v = int(float(val))
        self.var.set(v)

    def getDrugs(self): #How to get checkbox values?
        Symptoms = []
        i = 1
        for drug in (self.drug1,self.drug2,self.drug3,self.drug4,self.drug5,self.drug6,self.drug7,self.drug8,self.drug9,self.drug10):
            if drug.get():
                Symptoms.append(i)
            i=i+1

        return(Symptoms)

    def getTreatments(self): #How to get checkbox values?
        Symptoms = []
        i = 1
        for treatment in (self.treatment1,self.treatment2,self.treatment3,self.treatment4,self.treatment5,self.treatment6,self.treatment7,self.treatment8,self.treatment9,self.treatment10):
            if treatment.get():
                Symptoms.append(i)
            i=i+1

        return(Symptoms)

'''

def main():

    conn = psycopg2.connect("dbname=hospital user=postgres")
    root = Tk()
    root.geometry("700x300+300+300")
    app = doctorForm(root,conn)
    root.mainloop()


if __name__ == '__main__':
    main()
'''
