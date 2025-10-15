#övn 3
from makesmall import makesmall
from openfiles import openfiles
def files_smalltext(file):
    content=openfiles(file)
    content_small=makesmall(content)
    return content_small
