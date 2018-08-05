# -*- coding: utf-8 -*-

import wx

from blockwindow import BlockWindow

labels = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

class GridSizerFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'basic grid sizer')
        sizer = wx.GridSizer(rows=3, cols=3, hgap=5, vgap=5)
        for label in labels:
            bw = BlockWindow(self, label=label)
            sizer.Add(bw, 0, 0)

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