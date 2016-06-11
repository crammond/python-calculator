from tkinter import *


from functions import *
from model import Model


class App(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.model = Model()

        self.displayValue = IntVar()
        self.displayValue.set(self.model.values[0].value)

        self.display = Label(self, textvariable=self.displayValue)
        self.display.pack(side="top")

        self.one_b = Button(self)
        self.one_b["text"] = "1"
        self.one_b["command"] = self.one
        self.one_b.pack(side="bottom")

        self.add_b = Button(self)
        self.add_b["text"] = "+"
        self.add_b["command"] = self.sum
        self.add_b.pack(side="bottom")

    def one(self):
        if self.model.current().value == 0:
            self.model.current(Number(1))
        else:
            self.model.current(Number(self.model.current().value * 10 + 1))
        self.displayValue.set(self.model.values[self.model.index()].value)

    def sum(self):
        return



def main():

    # initialize root
    root = Tk()

    # create the application
    calculator = App(master=root)

    # here are method calls to the window manager
    calculator.master.title("Calculator")
    calculator.master.minsize(400, 400)
    calculator.master.resizable(width=False, height=False)

    # start the program
    calculator.mainloop()

if __name__ == "__main__":
    main()
