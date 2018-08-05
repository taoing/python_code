# -*- coding: utf-8 -*-

import time
import wx

class MyApp(wx.App):
    """
    子类化App
    """

    def __init__(self, *args, **kwargs):
        super(MyApp, self).__init__(*args, **kwargs)

    # 程序开始的时候被调用, 返回True
    def OnInit(self):
        self.frame = wx.Frame(parent=None, title='hello wxapp')
        self.frame.Show()
        # 设置应用的顶级窗口为self.frame
        self.SetTopWindow(self.frame)
        return True

if __name__ == '__main__':
    app = MyApp()
    app.MainLoop()