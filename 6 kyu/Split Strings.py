def solution(s):
    box  = []
    sentence = list(s)
    if len(sentence)%2==1:
        sentence.append('_')
    for item in range(len(sentence)//2):
        box.append(sentence[0]+sentence[1])
        sentence.remove(sentence[0])
        sentence.remove(sentence[0])
    return box
