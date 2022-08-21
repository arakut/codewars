def is_isogram(string):
    return len(set([i.lower() for i in string]))==len(string)
