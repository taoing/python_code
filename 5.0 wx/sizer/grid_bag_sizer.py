# -*- coding: utf-8 -*-

import wx

from blockwindow import BlockWindow

labels = "one two three four five six seven eight nine".split()

class TestFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, "GridBagSizer Test")
        sizer = wx.GridBagSizer(hgap=5, vgap=5)
        for col in range(3):
            for row in range(3):
                bw = BlockWindow(self, label=labels[row*3 + col])
                sizer.Add(bw, pos=(row,col))
        # 跨行
        bw = BlockWindow(self, label="span 3 rows")
        sizer.Add(bw, pos=(0,3), span=(3,1), flag=wx.EXPAND)
        # 跨列
        bw = BlockWindow(self, label="span all columns")
        sizer.Add(bw, pos=(3,0), span=(1,4), flag=wx.EXPAND)
        # 使最后的行和列可增长
        sizer.AddGrowableCol(3)
        sizer.AddGrowableRow(3)
        self.SetSizer(sizer)
        self.Fit()

app = wx.App()
TestFrame().Show()
app.MainLoop()