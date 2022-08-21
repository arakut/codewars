import string
letters = list(string.ascii_letters)

def find_missing_letter(chars):
    l1 = letters.index(chars[0])
    l2 = letters.index(chars[-1]) + 1
    ar2 = letters[l1:l2]
    letter = set(chars).symmetric_difference(set(ar2))
    return ''.join(letter)
