
def rotate_list(arr):
    size = len(arr)
    print("Normal List: ", arr)
    array = [arr[(i +2) % size]\
        for i, x in enumerate(arr)]
    print("Rotated List:", array)
if __name__ == '__main__':
    li = [10, 20, 30, 40, 50, 60]
    rotate_list(li)
    