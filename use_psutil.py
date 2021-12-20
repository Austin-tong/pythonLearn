import psutil
from tkinter import *
import tkinter.messagebox as messagebox

class Application(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()
    
    # def createWidgets(self):
    #     self.helloLabel = Label(self, text='Hello, world!')
    #     self.helloLabel.pack()
    #     self.quitButton = Button(self, text='Quit', command=self.quit)
    #     self.quitButton.pack()
    
    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self, text='hello', command=self.hello)
        self.alertButton.pack()

    def hello(self):
        name = self.nameInput.get or 'world'
        messagebox.showinfo('tonry', 'hello,%s' % name)

app = Application()
app.master.title('hello world')
app.mainloop()