def make_average():
    items = []
    def average(value):
        items.append(value)
        return sum(items) / len(items)
    return average


def make_average1():
    total = 0
    count = 0
    def average(value):
        nonlocal count, total
        count += 1
        total += value
        return total / count
    return average


if __name__ == '__main__':
    avg = make_average1()
    print(avg(2))
    print(avg(3))
    # __code__ 属性是编译后的函数定义体，保留着局部变量和自由变量名
    print(avg.__code__.co_varnames) 
    print(avg.__code__.co_freevars)
    # __closure__ 属性中可以获得自由变量的值
    print(avg.__closure__) 
    print(avg.__closure__[0].cell_contents)
