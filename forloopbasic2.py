def biggiesize(arr):
    for i in range(len(arr)):
        jf arr[i] > 0:
        arr[i]= "big"
    return arr

def countpostitives(arr):
    count = 0
    for i in range(len(arr)):
        if arr[i] > 0:
            count +=1
            arr[-1]= count
            return arr

def sumtotal(arr):
    count = 0
    for i in range(len(arr)):
        count = count + arr[i]
    return count

def average(arr):
    sum = 0
    for i in range(len(arr)):
        sum = sum + arr[i]
    return sum / len(arr)

def length(arr):
    return len(arr)

def minimum(arr):
    min = arr[0]
    if len(arr) == 0:
        return False
    for i in arr:
        if i < min:
            min = i
    return min

def maximum(arr):
    max = arr[0]
    if len(arr) == 0:
        return False
    for i in arr:
        if i > max:
            max = i
    return max

def ultimate_analyze(arr):
    dict = {
        'sumtotal' : sum_total(arr),
        'avg' : average(arr),
        'min' : minimum(arr),
        'max' : maximum(arr),
        'len' : length(arr)
    }
    return dict

def reversed(arr):
    arr = arr[::-1]
    return arr
