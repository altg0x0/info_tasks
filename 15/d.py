def r_search(arr, k):
    left = 0
    right = len(arr)
    while right - left > 1:
        delim = (left + right) // 2
        t = arr[delim]
        if t > k:
            right = delim
        else:
            left = delim  
    return arr[left]
    

def l_search(arr, k):
    left = -1
    right = len(arr) - 1
    while right - left > 1:
        delim = (left + right) // 2
        t = arr[delim]
        if t >= k:
            right = delim
        else:
            left = delim  
    return arr[right] 
    
    
n, k = map(int, input().split())
ar1 = list(map(int, input().split()))
ar2 = list(map(int, input().split()))
for el in ar2:
    print(min(r_search(ar1, el), l_search(ar1, el), key=lambda x: abs(x - el)))
