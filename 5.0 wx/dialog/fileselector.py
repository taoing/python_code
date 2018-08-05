# -*- coding: utf-8 -*-

import wx
import os

def main():
    app = wx.App()
    filepath = wx.FileSelector(message='select a file...', default_path=os.getcwd(), parent=None)
    print('filepath: ', filepath)

if __name__ == '__main__':
    main()