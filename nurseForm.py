#Python 2.7.0
#William Skagerstrom, Teodor Karlgren

from Tkinter import Tk, Text, TOP, BOTH, X, N, LEFT
from Tkinter import *
import tkMessageBox
from ttk import Frame, Label, Entry
from ttk import *
from doctorForm import *
from queuePicker import *
import main


class nurseForm(Frame):

    def __init__(self, parent, conn):
        Frame.__init__(self, parent)
        self.conn = conn
        self.parent = parent
        self.nurseForm()

    def quit(self):
        self.parent.destroy()

    def new_window(self):
        self.newWindow = Toplevel(self.parent)
        self.getInfo()
        self.app = nurseQueueSelect(self.newWindow, self.patientInfo)
    '''
    def Box(self):
        choices = ['Queue 1','Queue 2','Queue 3','Queue 4','Queue 5']
        variable = StringVar(self)
        variable.set('Queue 1')

        w = OptionMenu(self, variable, *choices)
        w.pack();
    '''

    def addQueueToDatabase(self):
        pass

    def nurseForm(self):

        self.parent.title("Nurse Form")
        self.parent.geometry("700x300+300+300")
        self.pack(fill=BOTH, expand=True)


        entry = Entry(self)
        quitButton = Button(self, text ="Exit", command=self.quit)
        quitButton.pack(side=BOTTOM, pady = 10)

        patientInfo = self.getInfo
        queueButton = Button(self,text="Add to queue", command=self.new_window)
        queueButton.pack(side=BOTTOM, pady = 20)


        frame1 = Frame(self)
        frame1.pack(fill=X)

        lbl1 = Label(frame1, text="Name", width=8)
        lbl1.pack(side=LEFT, padx=5, pady=5)

        self.entry1 = Entry(frame1)
        self.entry1.pack(fill=X, padx=5, expand=True)

        pNumber = Frame(self)
        pNumber.pack(fill=X)
        pNumberLabel = Label(pNumber, text= "Person ID", width=8 )
        pNumberLabel.pack(side=LEFT, padx=5, pady=5)

        self.pNumberEntry = Entry(pNumber)
        self.pNumberEntry.pack(fill=X, padx=5, expand=True)

        frame2 = Frame(self)
        frame2.pack(fill=X)

        lbl2 = Label(frame2, text="Age", width=8)
        lbl2.pack(side=LEFT, padx=5, pady=5)

        self.entry2 = Entry(frame2)
        self.entry2.pack(fill=X, padx=5, expand=True)

        gender = Frame(self)
        gender.pack(fill=X)
        genderLabel = Label(gender, text="Gender", width=8)
        genderLabel.pack(side=LEFT, padx=0, pady= 0)

        self.genderChoice = StringVar()

        self.gender = Radiobutton(gender, text="Male", variable=self.genderChoice, value = 'M').pack(side=LEFT, padx = 0, pady=0)
        self.gender = Radiobutton(gender, text="Female", variable=self.genderChoice, value = 'F').pack(side=LEFT, padx = 0, pady=0)


        frame3 = Frame(self)
        frame3.pack(fill=BOTH)

        self.var = IntVar()
        lbl3 = Label(frame3, text="Priority", width=8)
        lbl3.pack(side=LEFT, padx=5, pady=0)
        lbl3n = Label(frame3, textvariable=self.var)
        lbl3n.pack(side=LEFT, padx=0)

        self.entry3 = Scale(frame3, from_=1, to=5, command=self.onScale, orient=HORIZONTAL)
        self.entry3.pack(side=LEFT , padx=5, pady=5)

        frame4 = Frame(self)
        frame4.pack(fill=X)

        lbl4 = Label(frame4, text="Symptoms", width = 8)
        lbl4.pack(side=LEFT, padx = 5, pady = 5)

        issue = ["Test1","Test2","Test3","Test4", "Test5","Test6","Test7","Test8","Test9","Test10"]

        self.issue1=BooleanVar()
        self.issue2=BooleanVar()
        self.issue3=BooleanVar()
        self.issue4=BooleanVar()
        self.issue5=BooleanVar()
        self.issue6=BooleanVar()
        self.issue7=BooleanVar()
        self.issue8=BooleanVar()
        self.issue9=BooleanVar()
        self.issue10=BooleanVar()

        self.entry4 = Checkbutton(frame4, text=issue[0], variable=self.issue1).pack(side=LEFT, padx = 0, pady=0, expand=True)
        self.entry4 = Checkbutton(frame4, text=issue[1], variable=self.issue2).pack(side=LEFT, padx = 0, pady=0, expand=True)
        self.entry4 = Checkbutton(frame4, text=issue[2], variable=self.issue3).pack(side=LEFT, padx = 0, pady=0, expand=True)
        self.entry4 = Checkbutton(frame4, text=issue[3], variable=self.issue4).pack(side=LEFT, padx = 0, pady=0, expand=True)
        self.entry4 = Checkbutton(frame4, text=issue[4], variable=self.issue5).pack(side=LEFT, padx = 0, pady=0, expand=True)
        self.entry4 = Checkbutton(frame4, text=issue[5], variable=self.issue6).pack(side=LEFT, padx = 0, pady=0, expand=True)
        self.entry4 = Checkbutton(frame4, text=issue[6], variable=self.issue7).pack(side=LEFT, padx = 0, pady=0, expand=True)
        self.entry4 = Checkbutton(frame4, text=issue[7], variable=self.issue8).pack(side=LEFT, padx = 0, pady=0, expand=True)
        self.entry4 = Checkbutton(frame4, text=issue[8], variable=self.issue9).pack(side=LEFT, padx = 0, pady=0, expand=True)
        self.entry4 = Checkbutton(frame4, text=issue[9], variable=self.issue10).pack(side=LEFT, padx = 0, pady=0, expand=True)




    def getInfo(self):

        teams = main.addPatient(self.conn, [self.entry1.get(),self.pNumberEntry.get(),self.entry2.get() , int(self.entry3.get()), self.genderChoice.get()], self.getSymptoms()[0])

    def onScale(self,val):
        v = int(float(val))
        self.var.set(v)

    def getSymptoms(self): #How to get checkbox values?
        Symptoms = []
        i = 1
        for issue in (self.issue1,self.issue2,self.issue3,self.issue4,self.issue5,self.issue6,self.issue7,self.issue8,self.issue9,self.issue10):
            if issue.get():
                Symptoms.append(i)
            i=i+1

        return(Symptoms)


'''
def main():

    root = Tk()
    root.geometry("700x300+300+300")
    app = nurseForm(root)
    root.mainloop()


if __name__ == '__main__':
    main()
'''
