def func(list, t, i = 0):
    if (t <= 0):
        return
    list[i] = float(list[i])
    if (list[i] > 0):
        list[i] = list[i] + t/list[i]
    if (i == len(list)-1):
        return list
    return func(list, t, i+1)
