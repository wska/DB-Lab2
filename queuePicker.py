#Python 2.7.0
#William Skagerstrom, Teodor Karlgren

from Tkinter import Tk, Text, TOP, BOTH, X, N, LEFT
from Tkinter import *
from ttk import Frame, Label, Entry
from ttk import *
from doctorForm import *
#from main import *


class queuePicker(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.queuePickerForm()

    def queuePickerForm(self):
        self.parent.title("Queue Picker")
        self.pack(fill=BOTH)


        menuEntry = Entry(self)
        menuQuitButton = Button(self, text ="Cancel", command=self.quit)
        menuQuitButton.pack(side=BOTTOM, pady = 5)


        doctorQueueButton1 = Button(self,text="Queue 1", command=self.open_Doctor1)
        doctorQueueButton1.pack(side=BOTTOM, pady = 5)

        doctorQueueButton2 = Button(self,text="Queue 2", command=self.open_Doctor2)
        doctorQueueButton2.pack(side=BOTTOM, pady = 5)

        doctorQueueButton3 = Button(self,text="Queue 3", command=self.open_Doctor3)
        doctorQueueButton3.pack(side=BOTTOM, pady = 5)

        doctorQueueButton4 = Button(self,text="Queue 4", command=self.open_Doctor4)
        doctorQueueButton4.pack(side=BOTTOM, pady = 5)

        doctorQueueButton5 = Button(self,text="Queue 5", command=self.open_Doctor5)
        doctorQueueButton5.pack(side=BOTTOM, pady = 5)

    def quit(self):
        self.parent.destroy()


    def open_Doctor1(self):
        #getQueue(conn, tId)
        self.doctorTeam = 1
        self.newWindow = Toplevel(self.parent)
        self.app = doctorForm(self.newWindow)

    def open_Doctor2(self):
        #getQueue(conn, tId)
        self.doctorTeam = 2
        self.newWindow = Toplevel(self.parent)
        self.app = doctorForm(self.newWindow)

    def open_Doctor3(self):
        #getQueue(conn, tId)
        self.doctorTeam = 3
        self.newWindow = Toplevel(self.parent)
        self.app = doctorForm(self.newWindow)

    def open_Doctor4(self):
        #getQueue(conn, tId)
        self.doctorTeam = 4
        self.newWindow = Toplevel(self.parent)
        self.app = doctorForm(self.newWindow)

    def open_Doctor5(self):
        #getQueue(conn, tId)
        self.doctorTeam = 5
        self.newWindow = Toplevel(self.parent)
        self.app = doctorForm(self.newWindow)
'''
def main():

    root = Tk()
    root.geometry("700x300+300+300")
    app = queuePicker(root)
    root.mainloop()


if __name__ == '__main__':
    main()
'''
