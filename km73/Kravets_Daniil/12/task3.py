def groups(list, iterator):
    if iterator == len(list):
        return max(a)
    list_two = "".join(list)
    count_of_element = list.count(list[iterator])
    if (count_of_element - iterator)*str(list[iterator]) in list_two:
        a.append(count_of_element - iterator)
    return groups(list, iterator + 1)


a = []
list = input("Enter list : ").split()
print(groups(list, 0))
