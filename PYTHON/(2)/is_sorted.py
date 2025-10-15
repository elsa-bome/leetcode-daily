def is_sorted(thelist):
    for index in range(len(thelist) - 1):
        if thelist[index] > thelist[index + 1]:
            return False
    return True
