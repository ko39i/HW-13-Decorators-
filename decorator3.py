def list_to_int(func):
    def wrapper(list):
        new_list = []
        for i in list:
            try:
                new_list.append(int(i))
            except ValueError:
                continue
        return func(new_list)
    return wrapper

@list_to_int
def listsum(list):
    ret=0
    for i in list:
        ret += i
    return ret


print(listsum([3, 4, '5', 'a']))