 
def summation(var1, var2):
    """The function for adding the
    two numbers and returning the result"""
    var3 = var1 + var2
    print("adding", var1, "and", var2, "will give", var3)
    return var3
if __name__ == '__main__':
    result = summation(3, 4)
    print(result)