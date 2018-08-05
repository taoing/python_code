# -*- coding: utf-8 -*-

from tkinter import Tk, Frame, Label, W, Button, Checkbutton, IntVar

class Application(Frame):
    '''定义框架模板子类'''
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.varSausage = IntVar()
        self.varPepp = IntVar()
        self.create_widgets()

    def create_widgets(self):
        '''在框架中定义控件'''
        # 显示文本
        self.label1 = Label(self, text='welcome to my window!')
        # 定义控件为网格定位, W左对齐控件
        self.label1.grid(row=0, column=0, sticky=W)

        # 创建checkbutton选择控件
        self.check1 = Checkbutton(self, text='Sausage', variable=self.varSausage)
        self.check2 = Checkbutton(self, text='Pepperoni', variable=self.varPepp)
        self.check1.grid(row=1, column=0, sticky=W)
        self.check2.grid(row=2, column=0, sticky=W)

        # 创建按钮
        self.button1 = Button(self, text='Click me!', command=self.display)
        self.button1.grid(row=3, column=0, sticky=W)

    def display(self):
        '''时间处理方法, 点击按钮后, 执行的代码'''
        print('The button in the window was clicked!')
        print('sausage:', self.varSausage.get())
        print('pepperino:', self.varPepp.get())

        if self.varSausage.get():
            print('you want sausage')
        if self.varPepp.get():
            print('you want pepperoni')
        if not self.varSausage.get() and not self.varPepp.get():
            print('you don\'t want anything on your pizza')
        print('*' * 20)

root = Tk()
root.title('Test Application window')
root.geometry('300x100')
app = Application(root)
app.mainloop()