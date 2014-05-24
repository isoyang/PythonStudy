import os
import sys
import wx
import wx.xrc


class MyFrame2 (wx.Frame):
     
    def __init__( self ):
        wx.Frame.__init__ ( self, None, id = wx.ID_ANY, title = u"wo cao ", pos = wx.DefaultPosition, size = wx.Size( 502,644 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
         
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
         
        bSizer3 = wx.BoxSizer( wx.VERTICAL )
         
        self.m_panel4 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.m_panel4.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVEBORDER ) )
         
        bSizer4 = wx.BoxSizer( wx.VERTICAL )
         
        self.m_static_fileName = wx.StaticText( self.m_panel4, wx.ID_ANY, u"unopen file", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_static_fileName.Wrap( -1 )
        bSizer4.Add( self.m_static_fileName, 0, wx.ALL|wx.EXPAND, 5 )
         
        self.m_staticline1 = wx.StaticLine( self.m_panel4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        bSizer4.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )
         
        self.m_textCtrl1 = wx.TextCtrl( self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
        self.m_textCtrl1.SetBackgroundColour( wx.Colour( 0, 0, 0 ) )
        self.m_textCtrl1.SetForegroundColour( wx.Colour( 240, 240, 240 ) )
        bSizer4.Add( self.m_textCtrl1, 1, wx.ALL|wx.EXPAND, 5 )
         
         
        self.m_panel4.SetSizer( bSizer4 )
        self.m_panel4.Layout()
        bSizer4.Fit( self.m_panel4 )
        bSizer3.Add( self.m_panel4, 1, wx.EXPAND |wx.ALL, 5 )
         
         
        self.SetSizer( bSizer3 )
        self.Layout()
        self.m_menubar3 = wx.MenuBar( 0 )
        self.m_menu1 = wx.Menu()
        self.m_openFile = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"open"+ u"\t" + u"------  ctrl + f", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu1.AppendItem( self.m_openFile )
         
        self.m_save = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"save"+ u"\t" + u"------  ctrl + s", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu1.AppendItem( self.m_save )
         
        self.m_menu1.AppendSeparator()
         
        self.m_close = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"close", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu1.AppendItem( self.m_close )
         
        self.m_ext = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"quit"+ u"\t" + u"------  alt + F4", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu1.AppendItem( self.m_ext )
         
        self.m_menubar3.Append( self.m_menu1, u"file" ) 
         
        self.m_menu2 = wx.Menu()
        self.m_run = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"run"+ u"\t" + u"------  F5", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu2.AppendItem( self.m_run )
         
        self.m_debug = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"debug"+ u"\t" + u"------  F3", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu2.AppendItem( self.m_debug )
         
        self.m_menuItem8 = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"replace", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu2.AppendItem( self.m_menuItem8 )
         
        self.m_menubar3.Append( self.m_menu2, u"tool" ) 
         
        self.SetMenuBar( self.m_menubar3 )
         
   
        self.m_statusBar = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
         
        self.Centre( wx.BOTH )
         
        # Connect Events 
        self.Bind( wx.EVT_MENU, self.OpenFile, id = self.m_openFile.GetId() )
        self.Bind( wx.EVT_MENU, self.FormDestory, id = self.m_ext.GetId() )
        self.Bind( wx.EVT_MENU, self.SaveFile, id = self.m_save.GetId() )
        self.Bind( wx.EVT_MENU, self.CloseForm, id = self.m_close.GetId() )
     
    def __del__( self ):
        pass
     
     
    # Virtual event handlers, overide them in your derived class
    def FormDestory( self, event ):
        self.Destroy()
   
 
    def OpenFile( self, event ):
        self.dirname = ''
        dlg = wx.FileDialog(self,"chose a file",self.dirname,"","*.*",wx.OPEN)
        if dlg.ShowModal() == wx.ID_OK:
                self.filename = dlg.GetFilename()
                self.dirname = dlg.GetDirectory()
                filePath = self.dirname + self.filename
                self.m_static_fileName.SetLabel(filePath)
                #print self.dirname
                f = open(os.path.join(self.dirname,self.filename),'r')
                self.m_textCtrl1.SetValue(f.read())
                f.close()
                dlg.Destroy()
                 
                 
    def SaveFile( self, event ):
                try:
                    f = open(os.path.join(self.dirname,self.filename),'w')
                except AttributeError:
                    print 'file not exit'
                    sys.exit(0)
                
                content = self.m_textCtrl1.GetValue()
                try:
                    f.write(content)
                except UnboundLocalError:
                    print 'file not exit'
                    sys.exit(0)
                finally:
                    f.close()
 
 
    def CloseForm( self, event ):
                self.m_static_fileName.SetLabel(u'unopen file')
                self.m_textCtrl1.SetValue(u'')
 
           
           
app = wx.PySimpleApp()
frame = MyFrame2()
frame.Show()
app.MainLoop()