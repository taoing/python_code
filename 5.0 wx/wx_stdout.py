# -*- coding: utf-8 -*-

import wx
import sys

class Frame(wx.Frame):

    def __init__(self, parent, id, title):
        print('Frame__init__')
        super(Frame, self).__init__(parent, id, title)

class App(wx.App):

    def __init__(self, redirect=True, filename=None):
        print('App__init__')
        super(App, self).__init__(redirect, filename)

    def OnInit(self):
        print('OnInit') # 输出到stdout
        self.frame = Frame(parent=None, id=-1, title='Startup')
        self.frame.Show()
        self.SetTopWindow(self.frame)
        print(sys.stderr, 'a pretend error message') # 输出到stderr
        return True

    def OnExit(self):
        print('OnExit')
        return 0

if __name__ == '__main__':
    app = App(redirect=True, filename='output.txt') # 输出流重定向从这里开始
    print('before mainloop')
    app.MainLoop()
    print('after mainloop')