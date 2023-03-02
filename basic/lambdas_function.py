""" Lambda is an anonymous function
    it can take any numbers of arguments
    but it have only one expression
You can define the lambda function based on the following expression

lambda arguments(s): expressions

you can use the lambda function when you want to create simple expressions
but you dont use it when you create a little bit complex functions that in
cludes for loops, if conditions and so on.

# We can use the lambda functions in case of iterables in Python such as lists, dictionary,
tuples and strings. 

"""

# def f(x):
#     return x * 2
# if __name__ =="__main__":
#     print(f(3))

#print((lambda x: x * 2)(3))

## FILTER: when you want to focus in specific values in iterables you will use filter(function, list)

def func(x):
    for i in (x):
        if (i % 2 == 0):
            return i
    # return y
if __name__ == '__main__':
    list3 = [1,2,3,4,5,6,7,8,9,10]
    print(func(list3))
    


# it is a function definition that is not bound to an identifier
# are often an arguments that are being passed to a higher order functions
# used for constructing the result of a higher-order function that needs to return a function.



