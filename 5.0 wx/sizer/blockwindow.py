# -*- coding: utf-8 -*-

# 块窗口

import wx

class BlockWindow(wx.Panel):
    def __init__(self, parent, id=-1, label='', pos=wx.DefaultPosition, size=(100, 25)):
        wx.Panel.__init__(self, parent, id, pos, size, wx.RAISED_BORDER, label)
        self.label = label
        self.SetBackgroundColour('White')
        self.SetMinSize(size)
        self.Bind(wx.EVT_PAINT, self.OnPaint)

    def OnPaint(self, event):
        # 获取窗口尺寸
        sz = self.GetClientSize()
        # 绘制设备上下文
        dc = wx.PaintDC(self)
        # 获取文本以当前字体显示的尺寸
        w, h = dc.GetTextExtent(self.label)
        dc.SetFont(self.GetFont())
        # 绘制文本在窗口的中央
        dc.DrawText(self.label, (sz.width-w)/2, (sz.height-h)/2)