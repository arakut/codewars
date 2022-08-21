def disemvowel(string_):
    vowels = list('aeiou') 
    return ''.join([i for i in string_ if i.lower() not in vowels])
