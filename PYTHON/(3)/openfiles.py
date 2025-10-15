#övn 1
def openfiles(file):
    imported_file = open(file,"r")
    #imported_file=imported_file.strip("\n")
    content = imported_file.read()
    return content
