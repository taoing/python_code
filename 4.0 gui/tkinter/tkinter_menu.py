# -*- coding: utf-8 -*-

# Menu 控件
from tkinter import Tk, Frame, Label, Listbox, Button, EXTENDED, END, W, Menu

class Application(Frame):
    '''创建框架模板'''
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        # 创建窗口菜单控件
        menubar = Menu(self)
        filemenu = Menu(self)
        # 向菜单中添加菜单项
        filemenu.add_command(label='Convert', command=self.convert)
        filemenu.add_command(label='Clear', command=self.clear)
        # 将filemenu添加为menubar的下拉菜单
        menubar.add_cascade(label='File', menu=filemenu)
        menubar.add_command(label='Quit', command=self.quit)

        # 向窗口中添加菜单控件
        root.config(menu=menubar)

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

    def convert(self):
        print('This is a convert command')

    def clear(self):
        print('This is a clear command')

    def quit(self):
        print('This is a quit command')

root = Tk()
root.title('Listbox widget test')
root.geometry('300x300')
app = Application(root)
app.mainloop()