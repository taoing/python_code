# -*- coding: utf-8 -*-

import wx

class ToolbarFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(ToolbarFrame, self).__init__(*args, **kwargs)
        panel = wx.Panel(self)
        panel.SetBackgroundColour('White')

        statusBar = self.CreateStatusBar()

        toolbar = self.CreateToolBar()
        # toolbar.AddTool(-1, 'New',wx.Bitmap() 'Long help for New')
        toolbar.Realize()

        menubar = wx.MenuBar()
        menu1 = wx.Menu()
        menubar.Append(menu1, '&File')

        menu2 = wx.Menu()
        menu2.Append(-1, 'Copy', 'Copy in status bar')
        menu2.Append(-1, 'C', 'CCC')
        menu2.Append(-1, 'Paste', 'Paste in status bar')
        menu2.AppendSeparator()
        menu2.Append(-1, 'More', 'Display Options')
        # 菜单栏上附上菜单
        menubar.Append(menu2, '&More')
        # 在框架上附上菜单栏
        self.SetMenuBar(menubar)

if __name__ == '__main__':
    app = wx.App()
    frame = ToolbarFrame(None, -1, 'Toolbars', size=(300, 200))
    frame.Show()
    app.MainLoop()
