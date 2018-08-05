# -*- coding: utf-8 -*-

# Listbox 控件
from tkinter import Tk, Frame, Label, Listbox, Button, EXTENDED, END, W

class Application(Frame):
    '''创建框架模板'''
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.label1 = Label(self, text='Select youi items')
        self.label1.grid(row=0, column=0, sticky=W)
        # 创建选择列表控件
        self.listbox1 = Listbox(self, selectmode=EXTENDED)
        items = ['item one', 'item two', 'item three']
        # 添加选择条目
        for item in items:
            self.listbox1.insert(END, item)
        self.listbox1.grid(row=1)
        self.button1 = Button(self, text='Submit', command=self.display)
        self.button1.grid(row=2, column=0, sticky=W)

    def display(self):
        # 获取被选中的条目
        # items为选项索引组成的元组
        items = self.listbox1.curselection()
        for item in items:
            str_item = self.listbox1.get(item)
            print(str_item)
            print('*'*20)

root = Tk()
root.title('Listbox widget test')
root.geometry('300x300')
app = Application(root)
app.mainloop()