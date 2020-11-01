from __future__ import absolute_import, division, print_function, unicode_literals



import sys



import win32con # Used for win32 constants

import win32gui

import wx
import wx.media

from win32api import GetSystemMetrics

width = GetSystemMetrics(0)
#NOTE: A LOT OF THIS CODE IS ME JUST COPYING SOME STUFF OFF OF STACK OVERFLOW AND TRYING TO WORK WITH IT IM NOT SURE EXACTLY WHAT EVERYTHING DOES
class TestPanel(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None,style= wx.CAPTION | wx.STAY_ON_TOP | wx.CLIP_CHILDREN)#,style=wx.CLIP_CHILDREN | wx.STAY_ON_TOP)
        self.Move(-10,0) #Moves the window to the left slightly
        self.SetSize(width+40,8000) #The height is 8000 because the static started covering more of the screen 
  
		

        self.testMedia = wx.media.MediaCtrl(self, style=wx.SIMPLE_BORDER,szBackend=wx.media.MEDIABACKEND_WMP10) #Loads the media player
        self.media = "snow.mp4"
        self.testMedia.Bind(wx.media.EVT_MEDIA_LOADED, self.play) #Loads the file
      
        if self.testMedia.Load(self.media):
            pass
        else:
            print("Media not found")
            self.quit(None)

    def play(self, event):
        self.testMedia.Play()

    def quit(self, event):
        self.Destroy()

if __name__ == '__main__':
    transparency = input("How Opaque do you want the static to be? (1-150):") #Gets your input
    if int(transparency) >= 151 or int(transparency) < 1:
        transparency = 150
        print("Input was above 150, lowered to 150")
    app = wx.App()
    Frame = TestPanel() #Creates the frame
 
    hwnd=Frame.GetHandle()
    extendedStyleSettings = win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) #makes the window click through-able
    
    win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, extendedStyleSettings | win32con.WS_EX_LAYERED | win32con.WS_EX_TRANSPARENT) 

    win32gui.SetLayeredWindowAttributes(hwnd, 0, 255, win32con.LWA_ALPHA) #Not sure what this does
    Frame.SetTransparent(int(transparency)) #Sets frame transparency




    Frame.Show()
    app.MainLoop()