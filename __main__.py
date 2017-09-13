import pandas

def createLink(meetingID, computer, user):
    filepath = "\\\\{}\\C$\\Users\\{}\Desktop\\IT_Help.bat".format(computer, user)
    lines = []
    lines.append('START "" "https://www1.gotomeeting.com/join/{}"\n'.format(meetingID))
    lines.append('del {}\n'.format(filepath))

    file = open(filepath, 'w')
    for line in lines:
        file.write(line)
    file.close()

def getComputers():
    df1 = pandas.read_csv("computers.csv")
    print(df1)

#createLink("78946513", "test", "tester")
getComputers()

