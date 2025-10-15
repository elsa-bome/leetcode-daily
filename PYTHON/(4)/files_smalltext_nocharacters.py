#övn 7
# filnamn för textfil: test_seven.txt
from files_smalltext import files_smalltext
from nospace_nocharacters import nospace_nocharacters
def files_smalltext_nocharacters(file):
    text_small=files_smalltext(file)
    text_small_nocharacters=nospace_nocharacters(text_small)
    return text_small_nocharacters
