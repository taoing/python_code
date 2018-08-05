# -*- coding: utf-8 -*-

# 计算3场比赛的平均成绩

from tkinter import Tk, Frame, Label, Button, Menu, Entry, END

class Application(Frame):
    '''创建框架模板'''
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        menubar = Menu(self)
        filemenu = Menu(self)
        filemenu.add_command(label='Calculate', command=self.calculate)
        filemenu.add_command(label='Reset', command=self.clear)
        menubar.add_cascade(label='File', menu=filemenu)
        menubar.add_command(label='Quit', command=root.quit)
        root.config(menu=menubar)

        self.label1 = Label(self, text='The Bowling Calculator')
        # columnspan: 跨3列
        self.label1.grid(row=0, columnspan=3)

        self.label2 = Label(self, text='Enter score from game 1:')
        self.label3 = Label(self, text='Enter score from game 2:')
        self.label4 = Label(self, text='Enter score from game 3:')
        self.label5 = Label(self, text='Average:')
        self.label2.grid(row=2, column=0)
        self.label3.grid(row=3, column=0)
        self.label4.grid(row=4, column=0)
        self.label5.grid(row=5, column=0)

        self.score1 = Entry(self)
        self.score2 = Entry(self)
        self.score3 = Entry(self)
        self.average = Entry(self)
        self.score1.grid(row=2, column=1)
        self.score2.grid(row=3, column=1)
        self.score3.grid(row=4, column=1)
        self.average.grid(row=5, column=1)

        self.button1 = Button(self, text='Calculate Average', command=self.calculate)
        self.button1.grid(row=6, column=0)
        self.button2 = Button(self, text='Clear result', command=self.clear)
        self.button2.grid(row=6, column=1)
        # 第一个输入框自动获取焦点
        self.score1.focus_set()

    def calculate(self):
        '''计算平均值'''
        num_score1 = int(self.score1.get())
        num_score2 = int(self.score2.get())
        num_score3 = int(self.score3.get())
        average = (num_score1+num_score2+num_score3) / 3
        self.average.insert(0, '{0:.2f}'.format(average))

    def clear(self):
        '''清空当前输入'''
        self.score1.delete(0, END)
        self.score2.delete(0, END)
        self.score3.delete(0, END)
        self.average.delete(0, END)
        # 重新获取输入焦点
        self.score1.focus_set()


root = Tk()
root.title('Bowling Average Calculator')
root.geometry('500x200')
app = Application(root)
app.mainloop()
