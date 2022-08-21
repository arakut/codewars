def validate_pin(pin):
    count = 0
    for val in pin:
        if val.isdigit():
            print(val)
            count+=1
        else:
            return False
    return count==4 or count==6
