# -*- coding: utf-8 -*-

'''
没有标题栏的窗口实现鼠标拖动
'''

import wx

class NoCaptionFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(NoCaptionFrame, self).__init__(*args, **kwargs)
        panel = wx.Panel(self, -1)
        text = wx.StaticText(panel, -1, 'no caption window')
        self.make_bind()

    def make_bind(self):
        for event_type, handler in self.bind_data():
            self.Bind(event_type, handler)

    def bind_data(self):
        return ((wx.EVT_LEFT_DOWN, self.on_left_down),
                (wx.EVT_LEFT_UP, self.on_left_up),
                (wx.EVT_MOTION, self.on_motion),
                )

    def on_left_down(self, event):
        self.CaptureMouse()
        # 鼠标按下位置相对屏幕的坐标
        # 返回wx.Point()对象, 结构类似于元组
        pos = self.ClientToScreen(event.GetPosition())
        # 窗口的坐标
        frame_pos = self.GetPosition()
        # 鼠标位置相对于窗口位置的偏差
        # 鼠标按下之后, 在松开之前, 偏差固定
        # wx.Point直接相减, 可以计算差值
        self.delta_pos = pos - frame_pos
        
    def on_left_up(self, event):
        if self.HasCapture():
            self.ReleaseMouse()

    def on_motion(self, event):
        if event.Dragging() and event.LeftIsDown():
            # 鼠标移动之后的新位置
            new_pos = self.ClientToScreen(event.GetPosition())
            # 计算窗口的新位置
            new_frame_pos = new_pos - self.delta_pos
            self.Move(new_frame_pos)

def main():
    app = wx.App()
    frame = NoCaptionFrame(None, -1, 'no caption window', style=0)
    frame.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()
