#övn 1
def openfiles(file):
    imported_file = open(file,"r")
    content = imported_file.read()
    return content
