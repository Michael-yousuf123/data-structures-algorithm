"""A higher order function"""


def twice(f):
    def result(x):
        return f(f(x))
    return result

if __name__ == '__main__':
    plus_three = lambda i : i + 3
    g = twice(plus_three)
    print(g(7))

# @twice
# def g(i):
#     return i + 3
