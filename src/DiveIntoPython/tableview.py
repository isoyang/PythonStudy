#===============================================================================
# import wx, wx.grid
#  
# class GridData(wx.grid.PyGridTableBase):
#     _cols = "a b c".split()
#     _data = [
#         "1 2 3".split(),
#         "4 5 6".split(),
#         "7 8 9".split()
#     ]
#     _highlighted = set()
#  
#     def GetColLabelValue(self, col):
#         return self._cols[col]
#  
#     def GetNumberRows(self):
#         return len(self._data)
#  
#     def GetNumberCols(self):
#         return len(self._cols)
#  
#     def GetValue(self, row, col):
#         return self._data[row][col]
#  
#     def SetValue(self, row, col, val):
#         self._data[row][col] = val
#  
#     def GetAttr(self, row, col, kind):
#         attr = wx.grid.GridCellAttr()
#         attr.SetBackgroundColour(wx.GREEN if row in self._highlighted else wx.WHITE)
#         return attr
#  
#     def set_value(self, row, col, val):
#         self._highlighted.add(row)
#         self.SetValue(row, col, val)
#  
# class Test(wx.Frame):
#     def __init__(self):
#         wx.Frame.__init__(self, None)
#  
#         self.data = GridData()
#         self.grid = wx.grid.Grid(self)
#         self.grid.SetTable(self.data)
#  
#         btn = wx.Button(self, label="set a2 to x")
#         btn.Bind(wx.EVT_BUTTON, self.OnTest)
#  
#         self.Sizer = wx.BoxSizer(wx.VERTICAL)
#         self.Sizer.Add(self.grid, 1, wx.EXPAND)
#         self.Sizer.Add(btn, 0, wx.EXPAND)
#  
#     def OnTest(self, event):
#         self.data.set_value(1, 0, "x")
#         self.grid.Refresh()
#  
#  
# app = wx.PySimpleApp()
# app.TopWindow = Test()
# app.TopWindow.Show()
# app.MainLoop()
#===============================================================================

#===============================================================================
# import wx
# import os
# import xlrd
# import wx.lib.agw.xlsgrid as XG
#  
# class MyFrame(wx.Frame):
# 
#     def __init__(self):
# 
#         wx.Frame.__init__(self, None, -1, "Vessel List", size=(1000, 800))
# 
#         filename = os.path.join(os.getcwd(), "Excel", "/home/yang/Desktop/demo.xls")
#         sheetname = "Sheet1"
# 
#         book = xlrd.open_workbook(filename, formatting_info=1)
# 
#         sheet = book.sheet_by_name(sheetname)
#         rows, cols = sheet.nrows, sheet.ncols
# 
#         comments, texts = XG.ReadExcelCOM(filename, sheetname, rows, cols)
# 
#         xls_grid = XG.XLSGrid(self)
#         xls_grid.PopulateGrid(book, sheet, texts, comments)
# 
# 
# # our normal wxApp-derived class, as usual
# 
# app = wx.App(0)
# 
# frame = MyFrame()
# app.SetTopWindow(frame)
# frame.Show()
# 
# app.MainLoop()
#===============================================================================

import wx
import wx.grid
import xlrd

class TestFrame(wx.Frame):
    def __init__(self,filename):
        wx.Frame.__init__(self, None, title="Grid Attributes",size=(600,300))
        data = xlrd.open_workbook(filename,formatting_info=True)

        table = data.sheets()[0]

        nrow=table.nrows
        ncol=table.ncols
        
        grid = wx.grid.Grid(self)
        grid.CreateGrid(nrow,ncol)
        for col in range(ncol):
            for row in range(nrow):
                cell=table.cell(row,col)                
                if cell.ctype == 1:
                    content=cell.value.encode("UTF-8")
                elif cell.ctype == 2:
                    content=str(cell.value)
                
                grid.SetCellValue(row,col,content)
         
        grid.SetCellTextColour(1, 1, "red")
        grid.SetCellFont(1,1, wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD))
        grid.SetCellBackgroundColour(2, 2, "light blue")
        
        attr = wx.grid.GridCellAttr()
        attr.SetTextColour("navyblue")
        attr.SetBackgroundColour("pink")
        attr.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD))

        grid.SetAttr(2,0,attr)
       
        grid.SetRowAttr(0, attr)


app = wx.App()
frame = TestFrame('/home/yang/thesis/vessel.xls')
frame.Show()
app.MainLoop()





