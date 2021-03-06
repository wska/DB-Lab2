#Python 2.7.0
#William Skagerstrom, Teodor Karlgren

from Tkinter import Tk, Text, TOP, BOTH, X, N, LEFT
from Tkinter import *
from ttk import Frame, Label, Entry
from ttk import *
from doctorForm import *
from main import *


class queuePicker(Frame):

    def __init__(self, parent,conn):
        Frame.__init__(self, parent)
        self.parent = parent
        self.queuePickerForm()
        self.conn = conn



    def queuePickerForm(self):
        self.parent.title("Queue Picker")
        self.pack(fill=BOTH)
        self.parent.geometry("300x300+300+300")



        menuEntry = Entry(self)
        menuQuitButton = Button(self, text ="Exit", command=self.quit)
        menuQuitButton.pack(side=BOTTOM, pady = 5)


        nurseQueueButton1 = Button(self,text="Queue 1", command=self.open_Doctor1)
        nurseQueueButton1.pack(side=BOTTOM, pady = 5)

        nurseQueueButton2 = Button(self,text="Queue 2", command=self.open_Doctor2)
        nurseQueueButton2.pack(side=BOTTOM, pady = 5)

        nurseQueueButton3 = Button(self,text="Queue 3", command=self.open_Doctor3)
        nurseQueueButton3.pack(side=BOTTOM, pady = 5)

        nurseQueueButton4 = Button(self,text="Queue 4", command=self.open_Doctor4)
        nurseQueueButton4.pack(side=BOTTOM, pady = 5)

        nurseQueueButton5 = Button(self,text="Queue 5", command=self.open_Doctor5)
        nurseQueueButton5.pack(side=BOTTOM, pady = 5)

    def quit(self):
        self.parent.destroy()


    def open_Doctor1(self):
        #getQueue(conn, tId)
        self.doctorTeam = 1
        self.newWindow = Toplevel(self.parent)
        self.app = doctorForm(self.newWindow,self.conn, self.doctorTeam)

    def open_Doctor2(self):
        #getQueue(conn, tId)
        self.doctorTeam = 2
        self.newWindow = Toplevel(self.parent)
        self.app = doctorForm(self.newWindow,self.conn,  self.doctorTeam)


    def open_Doctor3(self):
        #getQueue(conn, tId)
        self.doctorTeam = 3
        self.newWindow = Toplevel(self.parent)
        self.app = doctorForm(self.newWindow,self.conn,  self.doctorTeam)

    def open_Doctor4(self):
        #getQueue(conn, tId)
        self.doctorTeam = 4
        self.newWindow = Toplevel(self.parent)
        self.app = doctorForm(self.newWindow, self.conn, self.doctorTeam)

    def open_Doctor5(self):
        #getQueue(conn, tId)
        self.doctorTeam = 5
        self.newWindow = Toplevel(self.parent)
        self.app = doctorForm(self.newWindow,self.conn,  self.doctorTeam)




class nurseQueueSelect(Frame):
    def __init__(self, parent, patientInfo, teams, conn):
        Frame.__init__(self, parent)
        self.parent = parent
        self.teams = teams
        self.patientInfo = patientInfo
        self.conn = conn
        self.nurseQueueSelectForm()



    def nurseQueueSelectForm(self):
        self.parent.title("Queue Selection")
        self.pack(fill=BOTH)
        self.parent.geometry("300x300+300+300")



        menuEntry = Entry(self)
        menuQuitButton = Button(self, text ="Exit", command=self.quit)
        menuQuitButton.pack(side=BOTTOM, pady = 5)

        #queues = getInfo()
        issueDict = getSpec(self.conn)
        queueChosen = 0
        openedButtons = []
        '''
        for i in queues:
            if i in issueDict[1] and i not in openedButtons:
                open_NurseQueue1

            elif i in issueDict[2] and i not in openedButtons:
                open_NurseQueue2

            elif i in issueDict[3] and i not in openedButtons:
                open_NurseQueue3

            elif i in issueDict[4] and i not in openedButtons:
                open_NurseQueue4

            elif i in issueDict[5] and i not in openedButtons:
                open_NurseQueue5
        '''
        print(self.teams)
        for i in self.teams:
            if i == 1:
                #print("open 1")
                self.open_NurseQueue1()
            elif i == 2:
                #print("open 2")
                self.open_NurseQueue2()
            elif i == 3:
                #print("open 3")
                self.open_NurseQueue3()
            elif i == 4:
                #print("open 4")

                self.open_NurseQueue4()
            elif i == 5:
                #print("open 5")
                self.open_NurseQueue5()






    def quit(self):
        self.parent.destroy()


    def open_NurseQueue1(self):
        nurseQueueButton1 = Button(self,text="Queue 1", command=self.sendToDatabase1)
        nurseQueueButton1.pack(side=BOTTOM, pady = 5)


        listBox1 = Listbox(self, width = 200)
        queue1 = getQueue(self.conn, 1)

        for i in range(0, len(queue1)):
            ins1 = str(queue1[i][1]) + ", " + str(queue1[i][0]) + ", Issue:" + str(queue1[i][3]) + ", Priority:" + str(queue1[i][2])
            listBox1.insert(i, ins1)

        listBox1.pack(side=BOTTOM, pady = 2)


    def open_NurseQueue2(self):
        nurseQueueButton2 = Button(self,text="Queue 2", command=self.sendToDatabase2)
        nurseQueueButton2.pack(side=BOTTOM, pady = 5)

        listBox2 = Listbox(self, width = 100)
        queue2 = getQueue(self.conn, 2)

        for i in range(0, len(queue2)):
            ins2 = str(queue2[i][1]) + ", " + str(queue2[i][0]) + ", Issue:" + str(queue2[i][3]) + ", Priority:" + str(queue2[i][2])
            listBox2.insert(i, ins2)

        listBox2.pack(side=BOTTOM, pady = 2)


    def open_NurseQueue3(self):
        print(self.patientInfo)
        nurseQueueButton3 = Button(self,text="Queue 3", command=self.sendToDatabase3)
        nurseQueueButton3.pack(side=BOTTOM, pady = 5)

        listBox3 = Listbox(self, width = 100)
        queue3 = getQueue(self.conn, 3)

        for i in range(0, len(queue3)):
            ins3 = str(queue3[i][1]) + ", " + str(queue3[i][0]) + ", Issue:" + str(queue3[i][3]) + ", Priority:" + str(queue3[i][2])
            listBox3.insert(i, ins3)

        listBox3.pack(side=BOTTOM, pady = 2)



    def open_NurseQueue4(self):
        nurseQueueButton4 = Button(self,text="Queue 4", command=self.sendToDatabase4)
        nurseQueueButton4.pack(side=BOTTOM, pady = 5)

        listBox4 = Listbox(self, width = 100)
        queue4 = getQueue(self.conn, 4)

        for i in range(0, len(queue4)):
            ins4 = str(queue4[i][1]) + ", " + str(queue4[i][0]) + ", Issue:" + str(queue4[i][3]) + ", Priority:" + str(queue4[i][2])
            listBox4.insert(i, ins4)

        listBox4.pack(side=BOTTOM, pady = 2)

    def open_NurseQueue5(self):
        nurseQueueButton5 = Button(self,text="Queue 5", command=self.sendToDatabase5)
        nurseQueueButton5.pack(side=BOTTOM, pady = 5)

        listBox5 = Listbox(self, width = 100)
        queue5 = getQueue(self.conn, 5)

        for i in range(0, len(queue5)):
            ins5 = str(queue5[i][1]) + ", " + str(queue5[i][0]) + ", Issue:" + str(queue5[i][3]) + ", Priority:" + str(queue5[i][2])
            listBox5.insert(i, ins5)

        listBox5.pack(side=BOTTOM, pady = 2)


    def quit(self):
        self.conn.rollback()
        self.parent.destroy()



    def sendToDatabase1(self):
        values = [str(self.patientInfo[0][1]), self.patientInfo[1], self.patientInfo[0][3],1 ]
        addToQueue(self.conn, values)

    def sendToDatabase2(self):
        values = [str(self.patientInfo[0][1]), self.patientInfo[1], self.patientInfo[0][3],2]
        addToQueue(self.conn, values)
    def sendToDatabase3(self):
        values = [str(self.patientInfo[0][1]), self.patientInfo[1], self.patientInfo[0][3],3 ]
        addToQueue(self.conn, values)

    def sendToDatabase4(self):
        values = [str(self.patientInfo[0][1]), self.patientInfo[1], self.patientInfo[0][3],4 ]
        addToQueue(self.conn, values)

    def sendToDatabase5(self):
        values = [str(self.patientInfo[0][1]), self.patientInfo[1], self.patientInfo[0][3],5 ]
        addToQueue(self.conn, values)











'''
def main():

    root = Tk()
    root.geometry("700x300+300+300")
    app = queuePicker(root)
    root.mainloop()


if __name__ == '__main__':
    main()
'''
