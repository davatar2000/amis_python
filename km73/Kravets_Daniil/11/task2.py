def func(list):
    if (len(list) < 2):
        return list[0]
    else:
        if (list[0] > list[1]):
            list.pop(0)
        else:
            list.pop(1)
        return func(list)
