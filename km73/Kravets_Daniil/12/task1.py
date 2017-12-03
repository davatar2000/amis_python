def integer(list, iterator):
    if iterator == -1:
        return
    list[iterator] = int(list[iterator])
    return integer(list, iterator - 1)


def second_maximum(list):
    if len(list) == 0:
        return
    if len(list) == 1:
        return list[0]
    maximum = second_maximum(list[1:])
    return maximum if maximum > list[0] else list[0]


def delete_max(list, iterator):
    if iterator == -1:
        return
    if list[iterator] < mx:
        result.append(list[iterator])
    return delete_max(list, iterator - 1)


result = []
list = input("Enter list: ").split()
integer(list, len(list) - 1)
mx = max(list)
delete_max(list, len(list) - 1)

print(second_maximum(result))
