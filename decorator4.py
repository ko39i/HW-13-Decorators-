def concertList(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        new_list = [str(arg) for arg in result]
        return new_list
    return wrapper


@concertList
def list_int(n):
    return list(range(0, n+1))

print(list_int(5))