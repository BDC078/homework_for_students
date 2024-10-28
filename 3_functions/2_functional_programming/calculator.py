"""Реализуйте необходимые функции ниже."""

def zero(func = None):
    if func == None:
        return 0
    else:
        return func(0)

def one(func = None):
    if func == None:
        return 1
    else:
        return func(1)

def two(func = None):
    if func == None:
        return 2
    else:
        return func(2)

def three(func = None):
    if func == None:
        return 3
    else:
        return func(3)

def four(func = None):
    if func == None:
        return 4
    else:
        return func(4)

def five(func = None):
    if func == None:
        return 5
    else:
        return func(5)

def six(func = None):
    if func == None:
        return 6
    else:
        return func(6)

def seven(func = None):
    if func == None:
        return 7
    else:
        return func(7)

def eight(func = None):
    if func == None:
        return 8
    else:
        return func(8)

def nine(func = None):
    if func == None:
        return 9
    else:
        return func(9)

def plus(right: int):
    return lambda left: left + right

def minus(right: int):
    return lambda left: left - right

def times(right: int):
    return lambda left: left * right

def divided_by(right: int):
    if right == 0:
        print('На ноль делить нельзя!')
    else:
        return lambda left: eft // right