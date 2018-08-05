# -*- coding: utf-8 -*-

import wx
import math
import random

class RadarGraph(wx.Window):
    def __init__(self, parent, title, labels):
        wx.Window.__init__(self, parent)
        self.title = title
        self.labels = labels
        self.data = [0.0] * len(labels)
        self.titleFont = wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD)
        self.labelFont = wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL)

        self.InitBuffer()

        self.Bind(wx.EVT_SIZE, self.OnSize)
        self.Bind(wx.EVT_PAINT, self.OnPaint)

    def OnSize(self, evt):
        # 窗口尺寸改变时, 需要创建缓冲上下文
        self.InitBuffer()

    def OnPaint(self, evt):
        # 绘制完成时, 缓冲设备上下文自动传送到屏幕设备上下文
        dc = wx.BufferedPaintDC(self, self.buffer)

    def InitBuffer(self):
        # 窗口客户区尺寸
        w, h = self.GetClientSize()
        # 创建一个缓冲位图, 缓冲设备上下文在其上完成绘制
        self.buffer = wx.Bitmap(w, h)
        # 创建缓冲设备上下文, 在缓冲设备上下文完成绘制后, 会传送到屏幕设备上下文中
        dc = wx.BufferedDC(wx.ClientDC(self), self.buffer)
        self.DrawGraph(dc)

    def GetData(self):
        return self.data

    def SetData(self, newData):
        assert len(newData) == len(self.data)
        self.data = newData[:]

        # self.data改变, 更新缓冲设备上下文和屏幕显示
        dc = wx.BufferedDC(wx.ClientDC(self), self.buffer)
        self.DrawGraph(dc)

    def PolarToCartesian(self, radius, angle, cx, cy):
        x = radius * math.cos(math.radians(angle))
        y = radius * math.sin(math.radians(angle))

        return (cx+x, cy-y)

    def DrawGraph(self, dc):
        # 在缓冲设备上下文中绘制
        spacer = 10
        scaledmax = 150.0

        dc.SetBackground(wx.Brush(self.GetBackgroundColour()))
        dc.Clear()
        dw, dh = dc.GetSize()

        # 在窗口顶部中间绘制文本
        dc.SetFont(self.titleFont)
        tw, th = dc.GetTextExtent(self.title)
        dc.DrawText(self.title, (dw-tw)/2, spacer)

        # 计算剩余空间的中心点
        th = th + 2*spacer
        cx = dw/2
        cy = (dh-th)/2 + th

        mindim = min(cx, (dh-th)/2)
        scale = mindim/scaledmax

        # 在中心点绘制圆圈
        dc.SetPen(wx.Pen('black', 1))
        dc.SetBrush(wx.TRANSPARENT_BRUSH)
        dc.DrawCircle(cx, cy, 25*scale)
        dc.DrawCircle(cx, cy, 50*scale)
        dc.DrawCircle(cx, cy, 75*scale)
        dc.DrawCircle(cx, cy, 100*scale)

        # 中心绘制 '十' 字轴线
        dc.SetPen(wx.Pen('black', 2))
        dc.DrawLine(cx-110*scale, cy, cx+110*scale, cy)
        dc.DrawLine(cx, cy-110*scale, cx, cy+110*scale)

        dc.SetFont(self.labelFont)
        maxval = 0
        angle = 0
        polypoints = []
        for i, label in enumerate(self.labels):
            val = self.data[i]
            point = self.PolarToCartesian(val*scale, angle, cx, cy)
            polypoints.append(point)
            # 将数据转换为坐标点
            x, y = self.PolarToCartesian(125*scale, angle, cx, cy)
            dc.DrawText(label, x, y)
            if val > maxval:
                maxval = val
            angle = angle + 360/len(self.labels)

        c = 'forest green'
        if maxval > 70:
            c = 'yellow'
        if maxval > 95:
            c = 'red'

        dc.SetBrush(wx.Brush(c))
        dc.SetPen(wx.Pen('navy', 3))
        dc.DrawPolygon(polypoints)


class TestFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title='Double Buffered Drawing', size=(480, 480))
        self.plot = RadarGraph(self, "Sample 'Radar' Plot", ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'])

        data = []
        for d in self.plot.GetData():
            val = d + random.uniform(-5, 5)
            if val < 0:
                val = 0
            if val > 110:
                val = 110
            data.append(val)
        self.plot.SetData(data)

        self.Bind(wx.EVT_TIMER, self.OnTimeout)
        self.timer = wx.Timer(self)
        self.timer.Start(500)

    def OnTimeout(self, evt):
        data = []
        for d in self.plot.GetData():
            val = d + random.uniform(-5, 5)
            if val < 0:
                val = 0
            if val > 110:
                val = 110
            data.append(val)
        self.plot.SetData(data)

def main():
    app = wx.App()
    frame = TestFrame()
    frame.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()