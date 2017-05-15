#Python 2.7.0
#William Skagerstrom, Teodor Karlgren

from Tkinter import Tk, Text, TOP, BOTH, X, N, LEFT
from Tkinter import *
from ttk import Frame, Label, Entry
from ttk import *
from doctorForm import *
from nurseForm import *
from queuePicker import *
#from main import *

class Menu(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent
        self.menuForm()

    def quit(self):
        self.parent.destroy()

    def open_Nurse(self):
        self.newWindow = Toplevel(self.parent)
        self.app = nurseForm(self.newWindow)

    def open_Doctor(self):
        self.newWindow = Toplevel(self.parent)
        self.app = doctorForm(self.newWindow)

    def open_QueuePicker(self):
        self.newWindow = Toplevel(self.parent)
        self.app = queuePicker(self.newWindow)

    def menuForm(self):
        self.parent.title("Hosiptal menu")
        self.pack(fill=BOTH)


        menuEntry = Entry(self)
        menuQuitButton = Button(self, text ="Exit", command=self.quit)
        menuQuitButton.pack(side=BOTTOM, pady = 5)


        menuQueueButton = Button(self,text="Add to queue", command=self.open_Nurse)
        menuQueueButton.pack(side=BOTTOM, pady = 5)

        menuRemoveButton = Button(self,text="Remove from queue", command=self.open_QueuePicker)
        menuRemoveButton.pack(side=BOTTOM, pady = 5)

def main():

    root = Tk()
    root.geometry("300x120+300+300")
    app = Menu(root)
    root.mainloop()

if __name__ == '__main__':
    main()
