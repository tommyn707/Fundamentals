def countdown():
    for x in range(num, 0, -1):
        print(x)

def print_and_return(arr):
    print(arr[0])
    return arr[1]

def first_plus_length(arr):
    return arr[0] + len(arr)

def valuesgreaterthansecond(arr)
    newArr = []
    if len(arr) <= 1:
        return False
    for i in arr:
        if arr[i] > arr[1]:
            newArr.append(arr[i])
            print(len(newArr))
            return newArr

def lengthAndValue(size, value):
    newArr = []
    for i in range(0, size):
        newArr.append(value)
        return newArr