# -*- coding: utf-8 -*-

import wx
from sketch_window import SketchWindow


class SketchFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, -1, "Sketch Frame",
                size=(800,600))
        self.sketch = SketchWindow(self, -1)
        self.sketch.Bind(wx.EVT_MOTION, self.OnSketchMotion)
        self.initStatusBar() #1 这里因重构有点变化
        self.createMenuBar()
        self.createToolBar()

    # 创建工具栏
    def createToolBar(self):
        toolbar = self.CreateToolBar()
        for each in self.toolbarData():
            self.createSimpleTool(toolbar, *each)
        toolbar.AddSeparator()

        for each in self.toolbarColorData():
            self.createColorTool(toolbar, each)
        # 显现工具栏
        toolbar.Realize()

    # 创建常规工具
    def createSimpleTool(self, toolbar, label, filename, help, handler):
        if not label:
            toolbar.AddSeparator()
            return
        bmp = wx.Image(filename, wx.BITMAP_TYPE_BMP).ConvertToBitmap()
        tool = toolbar.AddTool(-1, label, bmp, help)
        # 绑定事件
        self.Bind(wx.EVT_MENU, handler, tool)

    def toolbarData(self):
        return (('New', 'new.bmp', 'Createa new sketch', self.OnNew),
                ('', '', '', ''),
                ('Open', 'open.bmp', 'open ...', self.OnOpen),
                ('Save', 'save.bmp', 'save...', self.OnSave))

    # 创建颜色工具
    def createColorTool(self, toolbar, color):
        bmp = self.MakeBitmap(color)
        # tool = toolbar.AddRadioTool(-1, bmp, shortHelp=color)
        tool = toolbar.AddRadioTool(-1, color, bmp)
        self.Bind(wx.EVT_MENU, self.OnColor, tool)

    # 创建纯色位图
    def MakeBitmap(self, color):
        bmp = wx.Bitmap(16, 15)
        dc = wx.MemoryDC()
        dc.SelectObject(bmp)
        dc.SetBackground(wx.Brush(color))
        dc.Clear()
        dc.SelectObject(wx.NullBitmap)
        return bmp

    def toolbarColorData(self):
        return ('Black', 'Red', 'Green', 'Blue')

    # 创建状态栏
    def initStatusBar(self):
        self.statusbar = self.CreateStatusBar()
        self.statusbar.SetFieldsCount(3)
        self.statusbar.SetStatusWidths([-1, -2, -3])

    def OnSketchMotion(self, event):
        self.statusbar.SetStatusText("Pos: %s" %
                str(event.GetPosition()), 0)
        self.statusbar.SetStatusText("Current Pts: %s" %
                len(self.sketch.curLine), 1)
        self.statusbar.SetStatusText("Line Count: %s" %
                len(self.sketch.lines), 2)
        event.Skip()

    def menuData(self): #2 菜单数据
        return [("File", (
                    ("New", "New Sketch file", self.OnNew),
                    ("Open", "Open sketch file", self.OnOpen),
                    ("Save", "Save sketch file", self.OnSave),
                    ("", "", ""),
                    ("Color", (
                        ("Black", "", self.OnColor,
                           wx.ITEM_RADIO),
                        ("Red", "", self.OnColor,
                           wx.ITEM_RADIO),
                        ("Green", "", self.OnColor,
                           wx.ITEM_RADIO),
                        ("Blue", "", self.OnColor,
                           wx.ITEM_RADIO))),
                    ("", "", ""),
                    ("Quit", "Quit", self.OnCloseWindow)))]

    def createMenuBar(self):
        menuBar = wx.MenuBar()
        for eachMenuData in self.menuData():
            menuLabel = eachMenuData[0]
            menuItems = eachMenuData[1]
            menuBar.Append(self.createMenu(menuItems), menuLabel)
        self.SetMenuBar(menuBar)

    def createMenu(self, menuData):
        menu = wx.Menu()
#3 创建子菜单
        for eachItem in menuData:
            if len(eachItem) == 2:
                label = eachItem[0]
                subMenu = self.createMenu(eachItem[1])
                menu.Append(-1, label, subMenu)

            else:
                self.createMenuItem(menu, *eachItem)
        return menu

    def createMenuItem(self, menu, label, status, handler,
                       kind=wx.ITEM_NORMAL):
        if not label:
            menu.AppendSeparator()
            return
        menuItem = menu.Append(-1, label, status, kind)#4 使用kind创建菜单项
        self.Bind(wx.EVT_MENU, handler, menuItem)

    def OnNew(self, event): pass
    def OnOpen(self, event): pass
    def OnSave(self, event): pass

    # def OnColor(self, event):#5 处理颜色的改变
    #     menubar = self.GetMenuBar()
    #     itemId = event.GetId()
    #     item = menubar.FindItemById(itemId)
    #     color = item.GetLabel()
    #     self.sketch.SetColor(color)

    def OnColor(self, event):
        menubar = self.GetMenuBar()
        itemId = event.GetId()
        item = menubar.FindItemById(itemId)
        # 若事件不是由菜单项产生, 而是由工具栏中工具产生
        if not item:
            toolbar = self.GetToolBar()
            item = toolbar.FindById(itemId)
        color = item.GetLabel()
        self.sketch.SetColor(color)

    def OnCloseWindow(self, event):
        self.Destroy()


if __name__ == '__main__':
    app = wx.App()
    frame = SketchFrame(None)
    frame.Show()
    app.MainLoop()