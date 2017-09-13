import pandas
import os
from difflib import get_close_matches


def createLinkFile(meetingid, usersdir, user):
    filepath = "{}\\{}\Desktop\\IT_Help.bat".format(usersdir, user)
    lines = ['START "" "https://www1.gotomeeting.com/join/{}"\n'.format(meetingid), 'del {}\n'.format(filepath)]

    file = open(filepath, 'w')
    for line in lines:
        file.write(line)
    file.close()
    print("Link Created: {} for Meeting #: {}".format(filepath, meetingid))


def getComputers():
    df1 = pandas.read_csv("computers.csv")
    #print(df1.to_dict())
    return df1


def getUsersDir():
    computer = input("Enter Computer Name: ")
    usersDir = "\\\\{}\\C$\\Users".format(computer)
    if os.path.exists(usersDir):
        return usersDir
    else:
        print("That Computer Does Not Exist")
        exit()


def getUsers(usersDir):
    #print(usersDir)
    try:
        users = [d for d in os.listdir(usersDir) if os.path.isdir(os.path.join(usersDir, d))]
        return users
    except AttributeError:
        return []
    except OSError:
        return []


def getUser(users):
    if len(users) > 0:
        for user in users:
            print("{} | {}".format(users.index(user), user))
        selection = int(input("Select User #: "))
        user = users[selection]
        return user
    else:
        return ""


def createLink():
    try:
        usersdir = getUsersDir()

        user = getUser(getUsers(usersdir))

        meetingid = input("Enter Meeting ID: ")

        createLinkFile(meetingid, usersdir, user)
    except AttributeError as e:
        print(e)


createLink()

