from tkinter import *
import tkinter.messagebox
import ghjh
root = Tk()

 
# sets the name on the top of the gui
root.title("Number converter")
 
# sets the background color of the calculator
# as white
root.configure(background = 'white')
 
# fixed the width and height of the gui,
# hence can't be expanded/stretched

 
# sets the geometry
root.resizable(width=False,height=False)
root.geometry("430x568+0+0")
 
# holds the buttons in the calculator,
# act as a container for numbers and operators
calc = Frame(root)
 
# create a grid like pattern of the frame
# i.e buttons
calc.grid()
#this is called class which consist of func inshort
class Calc():
    #init special kind of func in class
    def __init__(self):
        self.total = 0
        self.current = ''
        self.input_value = True
        self.check_sum = False
        self.op = ''
        self.result = False
        self.transform = ''
    def numberEnter(self, num):
        self.result = False
        firstnum = txtDisplay.get()
        secondnum = str(num)
        if self.input_value:
            self.current = secondnum
            self.input_value = False
        else:
            if secondnum == '.':
                if secondnum in firstnum:
                    return
            self.current = firstnum+secondnum
        self.display(self.current)
 
    def sum_of_total(self):
        self.result = True
        self.current = (self.current)
        if self.check_sum == True:
            self.valid_function()
        else:
            self.total = float(txtDisplay.get())
 
    def display(self, value):
        txtDisplay.delete(0, END)
        txtDisplay.insert(0, value)
 
    def valid_function(self):
        if self.op == "sys":
            self.total = ghjh.f(self.total,self.current)
        if self.op == "asys":
            self.total = ghjh.af(self.total,self.current)
        self.input_value = True
        self.check_sum = False
        self.display(self.total)
 
    def operation(self, op):
        self.current = (self.current)
        if self.check_sum:
            self.valid_function()
        elif not self.result:
            self.total = self.current
            self.input_value = True
        self.check_sum = True
        self.op = op
        self.result = False
 
    def Clear_Entry(self):
        self.result = False
        self.current = "0"
        self.display(0)
        self.input_value = True
    def base(self):
        self.result = False
        self.current = ghjh.f(float(txtDisplay.get()),2)
        self.display(self.current)
 
    def All_Clear_Entry(self):
        self.Clear_Entry()
        self.total = 0

added_value = Calc()
txtDisplay = Entry(calc,
                   font=('Helvetica', 20,
                         'bold'),
                   bg='white',
                   fg='black',
                   bd=30,
                   width=25,
                   justify=RIGHT)
txtDisplay.focus_set()
txtDisplay.grid(row=0,
                column=0,
                columnspan=4,
                pady=1)
 
txtDisplay.insert(0, "0")
# store all the numbers in a variable
numberpad = "789456123"
 
# here i will count the rows for placing buttons
# in grid
i = 0
 
# create an empty list to store
# each button with its particular specifications
btn = []
 
# j is in that range to place
# the button in that particular row
for j in range(2, 5):
 
        # k is in this range to place the
    # button in that particular column
    for k in range(3):
        btn.append(Button(calc,
                          width=7,
                          height=2,
                          bg='white',
                          fg='black',
                          font=('Helvetica', 20, 'bold'),
                          bd=4, text=numberpad[i]))
 
        # set buttons in row & column and
        # separate them with a padding of 1 unit
        btn[i].grid(row=j, column=k, pady=1)
 
        # put that number as a symbol on that button
        btn[i]["command"] = lambda x=numberpad[i]: added_value.numberEnter(x)
        i += 1
btnClear = Button(calc, text=chr(67),
                  width=7, height=2,
                  bg='yellow',
                  font=('Helvetica', 20, 'bold'),
                  bd=4,
                  command=added_value.Clear_Entry).grid(
    row=1, column=0, pady=1)
 
btnAllClear = Button(calc, text="base 10", width=7,
                height=2, bg='yellow',
                font=('Helvetica', 20, 'bold'),
                bd=4, command=lambda: added_value.operation("asys")
                ).grid(row=1, column=1, pady=1)
btnZero = Button(calc, text="0", width=7,
                 height=2, bg='white', fg='black',
                 font=('Helvetica', 20, 'bold'),
                 bd=4, command=lambda: added_value.numberEnter(0)
                 ).grid(row=5, column=0, pady=1)
btnEquals = Button(calc, text="=", width=7,
                   height=2, bg='yellow',
                   font=('Helvetica', 20, 'bold'),
                   bd=4, command=added_value.sum_of_total
                   ).grid(row=5, column=2, pady=1)
btnAdd = Button(calc, text="base", width=7,
                height=2, bg='yellow',
                font=('Helvetica', 20, 'bold'),
                bd=4, command=lambda: added_value.operation("sys")
                ).grid(row=1, column=2, pady=1)
btn2 = Button(calc, text="base 2", width=7,
                height=2, bg='yellow',
                font=('Helvetica', 20, 'bold'),
                bd=4, command=added_value.base
                ).grid(row=5, column=1, pady=1)
 
def iExit():
    iExit = tkinter.messagebox.askyesno("Number Converter",
                                        "Do you want to exit ?")
    if iExit>0:
        root.destroy()
        return
 
 
 
def Standard():
    root.resizable(width=False, height=False)
    root.geometry("430x568+0+0")
 
menubar = Menu(calc)
 
# ManuBar 1 :
 
filemenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = 'File', menu = filemenu)
filemenu.add_command(label = "Standard", command = Standard)
filemenu.add_separator()
filemenu.add_command(label = "Exit", command = iExit)

# ManuBar 2 :
 
editmenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = 'Edit', menu = editmenu)
editmenu.add_command(label = "Cut")
editmenu.add_command(label = "Copy")
editmenu.add_separator()
editmenu.add_command(label = "Paste")

root.config(menu=menubar)
 
root.mainloop()
