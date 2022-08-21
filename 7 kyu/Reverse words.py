def reverse_words(text):
    revers = text[::-1].split(' ')
    revers.reverse()
    return ' '.join(revers)
