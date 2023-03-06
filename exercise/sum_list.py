"""Write a method that will return the sum of all the elements of the integer list given
list and its size as an argument."""

def sum_list(arr):
    n = len(arr)
    summation = 0
    i = 0
    for i in range(0, n):
        summation += arr[i]
        i += 1
    print(summation)
if __name__ == '__main__':
    l = [1, 2, 3, 4]
    sum_list(l)
