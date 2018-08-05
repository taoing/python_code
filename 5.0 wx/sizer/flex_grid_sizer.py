# -*- coding: utf-8 -*-

import wx

from blockwindow import BlockWindow

labels = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

class GridSizerFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'basic grid sizer')
        sizer = wx.FlexGridSizer(rows=3, cols=3, hgap=5, vgap=5)
        for label in labels:
            bw = BlockWindow(self, label=label)
            sizer.Add(bw, 0, 0)

        # 由name属性获取子窗口
        center = self.FindWindowByName('five')
        center.SetMinSize((150, 50))
        # 列扩展
        sizer.AddGrowableCol(0, 1)
        sizer.AddGrowableCol(1, 2)
        sizer.AddGrowableCol(2, 1)
        # 行扩展
        sizer.AddGrowableRow(0, 0)
        sizer.AddGrowableRow(1, 5)
        sizer.AddGrowableRow(2, 1)
        # 将sizer附加到窗口
        self.SetSizer(sizer)
        # 调整窗口的尺寸以适应子窗口的尺寸
        self.Fit()

def main():
    app = wx.App()
    frame = GridSizerFrame()
    frame.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()