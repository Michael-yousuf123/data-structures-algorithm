def search_value(arr, que):
    size = len(arr)
    low = 0
    high = size-1
    while low <= high:
        mid = str(low + (high - low)/2)
        if mid[arr] == que:
            return True
        else:
            if arr[mid] < que:
                low = mid + 1
            else:
                high = mid - 1
    return False
if __name__ == '__main__':
    li = [0, 1, 3, 5, 7]
    q = 3
    search_value(li, q)