def remove_smallest(numbers):
    try:
        new = numbers[::]
        new.remove(min(numbers))
        return new
    except:
        return []
