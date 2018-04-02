import pandas
import os
import wx
import FrmMain
import webbrowser
from difflib import get_close_matches

class MyFrame(wx.Frame):
    def createLinkFile(self, meetingid, usersdir, user):
        filepath = "{}\\{}\Desktop\\IT_Help.bat".format(usersdir, user)
        lines = ['START "" "https://www1.gotomeeting.com/join/{}"\n'.format(meetingid), 'del {}\n'.format(filepath)]

        file = open(filepath, 'w')
        for line in lines:
            file.write(line)
        file.close()
        print("Link Created: {} for Meeting #: {}".format(filepath, meetingid))

    def getComputers(self):
        df1 = pandas.read_csv("computers.csv")
        # print(df1.to_dict())
        return df1

    def getUsersDir(self):
        computer = self.txtComputer.GetValue()
        if computer != "":
            usersDir = "\\\\{}\\C$\\Users".format(computer)
            if os.path.exists(usersDir):
                return usersDir
            else:
                print("That Computer Does Not Exist")
        else:
            print("Computer Field Empty")

    def getUsers(self, usersDir):
        # print(usersDir)
        try:
            users = [d for d in os.listdir(usersDir) if os.path.isdir(os.path.join(usersDir, d))]
            return users
        except AttributeError:
            return []
        except OSError:
            return []
        except TypeError:
            return []

    def getUser(self, users):
        if len(users) > 0:
            for user in users:
                print("{} | {}".format(users.index(user), user))
            selection = int(input("Select User #: "))
            user = users[selection]
            return user
        else:
            return ""

    def createLink(self, meetingid):
        try:
            usersdir = self.getUsersDir()

            #user = self.getUser(self.getUsers(usersdir))
            user = self.cboUsername.GetStringSelection()

            #meetingid = input("Enter Meeting ID: ")

            self.createLinkFile(meetingid, usersdir, user)
        except AttributeError as e:
            print(e)

    def btnOpenGTMClick(self, instance):
        try:
            webbrowser.open("https://www.gotomeeting.com", new=0, autoraise=True)
        except AttributeError as e:
            print(e)

    def btnClearClick(self, instance):
        self.txtComputer.SetValue("")
        self.txtMeetingNum.SetValue("")
        self.cboUsername.Clear()

    def btnPopulateClick(self, instance):
        try:
            usersdir = self.getUsersDir()
            users = self.getUsers(usersdir)
            print(users)
            self.cboUsername.Clear()
            self.cboUsername.Append(users)
        except AttributeError as e:
            print(e)

    def btnCopyClick(self, instance):
        self.createLink(self.txtMeetingNum.GetValue())

    def __init__(self, parent):
        FrmMain.FrmMain.__init__(self, parent)
        self.Show(True)


app = wx.App(False)
frame = MyFrame(None)
app.MainLoop()
