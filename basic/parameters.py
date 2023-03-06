# class ParameterPass:
#     def __init__(self):
#         A= 1 
#         self.Change(A)
#         print(A)
#     def Change(self, B):
#         B = 2
#         return B
# if __name__ == '__main__':
#     var = ParameterPass().Change(2)
#     print(var)

class ParameterPass:
    def __init__(self):
        A= [1, 2] # the changes inside the called function results in a change in the calling fun
        self.Change(A)
        print(A)
    def Change(self, B):
        B.append(2)
        return 
if __name__ == '__main__':
    var = ParameterPass().Change(2)
    print(var)

# class Main():
#     def __init__(self):
#         self.String1 = "Michael"
#         self.String2 = "Yousuf"
#     def Function2(self):
#         print("My Name is:", self.String1)
#         return
#     def Function1(self):
#         self.Function2()
#         print("My Father Name is:", self.String2)
#         return
# if __name__ == '__main__':
#     name = Main()
#     name.Function1()
    