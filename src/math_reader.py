

def divide(l):
    counter = 0
    for i, eq in enumerate(l):
        if i == 0:
            counter = int(eq)
        else:
            counter /= int(eq)
    return counter


def multiply(l):
    counter = 0

    for i, eq in enumerate(l):
        if isinstance(eq, list):
            if i == 0:
                counter = divide(eq)
            else:
                counter *= divide(eq)
        else:
            if i == 0:
                counter = int(eq)
            else:
                counter *= int(eq)
    return counter


def add(l):
    counter = 0
    for i, eq in enumerate(l):
        if isinstance(eq, list):
            if i == 0:
                counter = multiply(eq)
            else:
                counter += multiply(eq)
        else:
            if i == 0:
                counter = int(eq)
            else:
                counter += int(eq)
    return counter


def subtract(l):
    counter = 0
    for i, eq in enumerate(l):
        if isinstance(eq, list):
            if i == 0:
                counter = add(eq)
            else:
                counter -= add(eq)
        else:
            if i == 0:
                counter = int(eq)
            else:
                counter -= int(eq)
    return counter


def parseInput(input1):

    a = input1

    a = a.split('-')

    for i in range(len(a)):
        a[i] = a[i].split('+')

    for i in range(len(a)):
        for j in range(len(a[i])):
            a[i][j] = a[i][j].split('*')

    for i in range(len(a)):
        for j in range(len(a[i])):
            for k in range(len(a[i][j])):
                a[i][j][k] = a[i][j][k].split('/')
    return a


def solveParsed(l):
    return subtract(l)
