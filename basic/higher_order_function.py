"""A higher order function"""


def twice(f):
    def result(x):
        return f(f(x))
    return result

if __name__ == '__main__':
    plus_three = lambda i : i + 3
    g = twice(plus_three)
    print(g(7))

# Python decorator syntax is often used to replace a function with the result of 
# passing that function through a higher-order function. 
# @twice 
# def g(i):
#     return i + 3
