
FileHandle = open("SampleFile.TXT", "r")
LineOfText = FileHandle.readline()
while len(LineOfText) > 0:
    LineOfText = FileHandle.readline()
    print(LineOfText)
FileHandle.close()