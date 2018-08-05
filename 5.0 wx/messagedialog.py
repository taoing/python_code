# -*- coding: utf-8 -*-
# 对话框

import wx

app = wx.App()
frame = wx.Frame(None, -1, title='Dialog...', size=(300, 200))
frame.Show()

# 消息对话框
dlg = wx.MessageDialog(None, 'Is this the coolest thing ever!', 'MessageDialog', wx.YES_NO|wx.ICON_QUESTION)
result = dlg.ShowModal()
print('result: ', result)

# 文本输入对话框
entry_dlg = wx.TextEntryDialog(None, 'what is your name?', 'A question', 'xiaoming')
if entry_dlg.ShowModal() == wx.ID_OK:
    response = entry_dlg.GetValue()
    print('response: ', response)

# 单选列表
select_dlg = wx.SingleChoiceDialog(None, 'what version of python are you using?', 'Single Choice', ['2.7', '3.4', '3.5.2', '3.6'])
if select_dlg.ShowModal() == wx.ID_OK:
    response = select_dlg.GetStringSelection()
    print('response: ', response)

# app.MainLoop()