'''import tkinter as tk

class SampleApp(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        self.entry = tk.Entry(self)
        self.button = tk.Button(self, text="Get", command=self.on_button)
        self.button.pack()
        self.entry.pack()

    def on_button(self):
        print(self.entry.get())

w = SampleApp()
w.mainloop()
'''


from Tkinter import Tk, Text, TOP, BOTH, X, N, LEFT
from Tkinter import *
from ttk import Frame, Label, Entry


class Example(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent
        self.initUI()


    def initUI(self):

        self.parent.title("Review")
        self.pack(fill=BOTH, expand=True)


        entry = Entry(self)

        button = Button(self,text="Get", command=self.getSymptoms)
        button.pack(side=BOTTOM)

        frame1 = Frame(self)
        frame1.pack(fill=X)

        lbl1 = Label(frame1, text="Name", width=8)
        lbl1.pack(side=LEFT, padx=5, pady=5)

        self.entry1 = Entry(frame1)
        self.entry1.pack(fill=X, padx=5, expand=True)

        frame2 = Frame(self)
        frame2.pack(fill=X)

        lbl2 = Label(frame2, text="Age", width=8)
        lbl2.pack(side=LEFT, padx=5, pady=5)

        self.entry2 = Entry(frame2)
        self.entry2.pack(fill=X, padx=5, expand=True)

        frame3 = Frame(self)
        frame3.pack(fill=BOTH)

        self.var = IntVar()
        lbl3 = Label(frame3, text="Priority", width=8)
        lbl3.pack(side=LEFT, padx=5, pady=0)

        self.entry3 = Scale(frame3, from_=1, to=5, command=self.onScale, orient=HORIZONTAL)
        self.entry3.pack(side=LEFT , padx=0, pady=0)

        frame4 = Frame(self)
        frame4.pack(fill=X)



        lbl4 = Label(frame4, text="Symptoms", width = 8)
        lbl4.pack(side=LEFT, padx = 5, pady = 5)
        issue = ["Test1","Test2","Test3","Test5","Test6","Test7","Test8","Test9","Test10"]
        self.dVar = [0] * len(issue)
        issueCopy = issue[0:10]

        for i in range(0,len(issue)):
            issue[i] = Variable()
            print(issue[i])
            self.entry4 = Checkbutton(frame4, text=issue[i], variable=self.dVar[i])
            self.entry4.pack(side=LEFT, padx = 0, pady=0, expand=True)



    def on_button(self):
        print(self.entry1.get() + "\n" + self.entry2.get() + "\n" + str(self.entry3.get()) + "\n")

    def onScale(self,val):
        v = int(float(val))
        self.var.set(v)

    def getSymptoms(self): #How to get checkbox values?
        print (self.dVar[0])

    #def checkButton(self,in)



def main():

    root = Tk()
    root.geometry("600x600+300+300")
    app = Example(root)
    root.mainloop()


if __name__ == '__main__':
    main()
