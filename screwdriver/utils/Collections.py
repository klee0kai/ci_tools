def remove_doubles(originalList, key_func):
    outList = []
    key_list = []
    for it in originalList:
        key = key_func(it)
        if key in key_list:
            continue
        key_list += [key]
        outList += [it]

    return outList
