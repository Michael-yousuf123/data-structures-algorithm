"""Write a method, which will search a list for some given value."""

def sequence_search(lists, number):
    size = len(lists)
    for index in range(0, size):
        if number == lists[index]:
            print(index)
            index += 1
if __name__ == '__main__':
    l = [1,2,3]
    n = 3
    sequence_search(l, n)