# -*- coding: utf-8 -*-

from tkinter import Tk, Frame, Entry, Button, Label, W, END

class Application(Frame):
    '''框架模板子类'''
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.label1 = Label(self, text='Please enter some text in lower case')
        self.label1.grid(row=0, column=0, sticky=W)

        # 创建表单控件
        self.text1 = Entry(self)
        self.text1.grid(row=2)

        self.button1 = Button(self, text='Convert text', command=self.convert)
        self.button1.grid(row=6, column=0)
        self.button2 = Button(self, text='Clear result', command=self.clear)
        self.button2.grid(row=6, column=1)
        # 获取输入焦点
        self.text1.focus_set()

    def convert(self):
        '''获取输入字符串并转换为大写'''
        var_text = self.text1.get()
        var_replaced = var_text.upper()
        # 清空表单
        self.text1.delete(0, END)
        self.text1.insert(END, var_replaced)

    def clear(self):
        '''清空表单, 重新获取输入焦点'''
        self.text1.delete(0, END)
        self.text1.focus_set()


root = Tk()
root.title('Testing and Entry widget')
root.geometry('500x200')
app = Application(root)
app.mainloop()