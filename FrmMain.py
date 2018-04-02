# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc


###########################################################################
## Class FrmMain
###########################################################################

class FrmMain(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"GTM Link Sender", pos=wx.DefaultPosition,
                          size=wx.Size(-1, 265), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.Size(500, 265), wx.Size(500, 265))

        gbSizer3 = wx.GridBagSizer(0, 0)
        gbSizer3.SetFlexibleDirection(wx.BOTH)
        gbSizer3.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_ALL)

        gbSizer3.SetMinSize(wx.Size(-1, 265))
        self.m_staticText8 = wx.StaticText(self, wx.ID_ANY, u"Meeting Number", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText8.Wrap(-1)
        gbSizer3.Add(self.m_staticText8, wx.GBPosition(0, 0), wx.GBSpan(1, 1),
                     wx.ALL | wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_button2 = wx.Button(self, wx.ID_ANY, u"Open GTM", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer3.Add(self.m_button2, wx.GBPosition(0, 1), wx.GBSpan(1, 1),
                     wx.ALL | wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_button3 = wx.Button(self, wx.ID_ANY, u"Clear", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer3.Add(self.m_button3, wx.GBPosition(0, 2), wx.GBSpan(1, 1),
                     wx.ALL | wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.txtMeetingNum = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer3.Add(self.txtMeetingNum, wx.GBPosition(1, 0), wx.GBSpan(1, 3),
                     wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 5)

        self.m_staticText9 = wx.StaticText(self, wx.ID_ANY, u"Computer", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText9.Wrap(-1)
        gbSizer3.Add(self.m_staticText9, wx.GBPosition(2, 0), wx.GBSpan(1, 3),
                     wx.ALL | wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.txtComputer = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer3.Add(self.txtComputer, wx.GBPosition(3, 0), wx.GBSpan(1, 2),
                     wx.ALL | wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.btnPopulate = wx.Button(self, wx.ID_ANY, u"Populate", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer3.Add(self.btnPopulate, wx.GBPosition(3, 2), wx.GBSpan(1, 1),
                     wx.ALL | wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.lblUsername = wx.StaticText(self, wx.ID_ANY, u"Username", wx.DefaultPosition, wx.DefaultSize, 0)
        self.lblUsername.Wrap(-1)
        gbSizer3.Add(self.lblUsername, wx.GBPosition(4, 0), wx.GBSpan(1, 1),
                     wx.ALL | wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        cboUsernameChoices = []
        self.cboUsername = wx.ComboBox(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                       cboUsernameChoices, 0)
        gbSizer3.Add(self.cboUsername, wx.GBPosition(5, 0), wx.GBSpan(1, 3),
                     wx.ALL | wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.btnCopy = wx.Button(self, wx.ID_ANY, u"Copy Help Link", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer3.Add(self.btnCopy, wx.GBPosition(6, 0), wx.GBSpan(1, 3),
                     wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 5)

        gbSizer3.AddGrowableCol(0)
        gbSizer3.AddGrowableCol(1)
        gbSizer3.AddGrowableCol(2)

        self.SetSizer(gbSizer3)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.btnPopulate.Bind(wx.EVT_BUTTON, self.btnPopulateClick)
        self.btnCopy.Bind(wx.EVT_BUTTON, self.btnCopyClick)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def btnPopulateClick(self, event):
        event.Skip()

    def btnCopyClick(self, event):
        event.Skip()


