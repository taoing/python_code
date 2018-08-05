# -*- coding: utf-8 -*-

import wx

class HelloFrame(wx.Frame):
    """
    A Frame
    """

    def __init__(self, *args, **kwargs):
        # 调用父类的__init__方法
        super(HelloFrame, self).__init__(*args, **kwargs)

        # 创建面板
        pnl = wx.Panel(self)

        # 显示文本, 字体加大加粗
        st = wx.StaticText(pnl, label="hello world!", pos=(25,25))
        font = st.GetFont()
        font.PointSize += 10;
        font = font.Bold()
        st.SetFont(font)

        # 创建菜单栏
        self.makeMenuBar()

        # 创建状态栏
        self.CreateStatusBar()
        self.SetStatusText("Welcome to wxPython!")

    def makeMenuBar(self):
        fileMenu = wx.Menu()
        helloItem = fileMenu.Append(-1, "&hello...\tCtrl-H",
            "help string shown in status bar for this menu item")

        fileMenu.AppendSeparator()

        exitItem = fileMenu.Append(wx.ID_EXIT)

        helpMenu = wx.Menu()
        aboutItem = helpMenu.Append(wx.ID_ABOUT)

        menuBar = wx.MenuBar()
        menuBar.Append(fileMenu, '&File')
        menuBar.Append(helpMenu, '&Help')

        # 将菜单栏绑定在frame上
        self.SetMenuBar(menuBar)

        # 绑定事件句柄
        self.Bind(wx.EVT_MENU, self.OnHello, helloItem)
        self.Bind(wx.EVT_MENU, self.OnExit, exitItem)
        self.Bind(wx.EVT_MENU, self.OnAbout, aboutItem)

    def OnExit(self, event):
        self.Close(True)

    def OnHello(self, event):
        wx.MessageBox('hello again from wxPython')

    def OnAbout(self, event):
        wx.MessageBox('This is a wxPython hello world sample', 'about hello world 2', wx.OK|wx.ICON_INFORMATION)

if __name__ == '__main__':
    app = wx.App()
    frm = HelloFrame(None, title='hello world 2')
    frm.Show()
    app.MainLoop()