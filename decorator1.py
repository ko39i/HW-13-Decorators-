from datetime import datetime


def time_of_func(func):
    def wrapper():
        star = datetime.now()
        result = func()
        print(datetime.now() - star)
        return result
    return wrapper

@time_of_func
def data_info():
    data_user = input("enter your information: ")
    list_info = []
    for element in data_user:
        list_info.append(element)
    return print(list_info)



data_info()
