# -*- coding: utf-8 -*-

import wx

class InsertFrame(wx.Frame):

    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'Frame with button', size=(300,100))
        # 创建面板
        panel = wx.Panel(self)
        # 按钮添加到面板
        button = wx.Button(panel, label='Close', pos=(125, 10), size=(50, 50))
        # 绑定按钮的单机事件
        self.Bind(wx.EVT_BUTTON, self.OnCloseMe, button)
        # 绑定窗口的关闭事件
        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)

    def OnCloseMe(self, event):
        print('close...')
        self.Close(True)

    def OnCloseWindow(self, event):
        print('window destroy...')
        self.Destroy()


if __name__ == '__main__':
    app = wx.App()
    frame = InsertFrame(None, -1)
    frame.Show()
    app.MainLoop()