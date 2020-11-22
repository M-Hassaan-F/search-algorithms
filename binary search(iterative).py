def BinarySearch(arr, data):
    lowerBound = 0
    upperBound = len(arr)

    while lowerBound <= upperBound:
        mid = ((upperBound + lowerBound) // 2)
        if arr[mid] == data:
            return mid
        elif arr[mid] < data:
            lowerBound = mid + 1
        else:
            upperBound = mid - 1
    return -1

print("example data [a,b, c, d ,e ,f ,g ,h, i]")
arr = ["a", "b", "c", "d", "e", "f", "g", "h","i"]
data = input("enter data to be searched: ")
result = BinarySearch(arr, data)
if result == -1:
    print("element was not found")
else:
    print("element was found at: ", result)