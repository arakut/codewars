def dig_pow(n, p):
    numbers = list(str(n))
    counter = 0
    for val in numbers:
        counter+=int(val)**p
        p+=1
    answ = counter/n
    return int(answ) if int(answ)-answ==0.0 else -1
