def print_info(func):
    def wrapper(x, y):
        q = func(x, y)
        print(f"With legs {x}, {y} - hypotenuse door {q}")
        return q
    return wrapper

@print_info
def calc_hyp(x, y):
    return (x ** 2 + y ** 2)** 0.5

calc_hyp(3,4)
