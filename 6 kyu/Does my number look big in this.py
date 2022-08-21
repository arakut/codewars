def narcissistic(value):
    numbers = [int(i) for i in str(value)]
    box = 0
    for num in numbers:
        box += num**len(numbers)
    return box==value
