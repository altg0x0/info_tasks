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
    return left if arr[left] == k else -1 
    

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
    return right if arr[right] == k else -1 
    
    
input()
ar1 = list(map(int, input().split()))
input()
ar2 = list(map(int, input().split()))
for el in ar2:
    t = l_search(ar1, el)
    if t == -1:
        print (0)
        continue
    print(r_search(ar1, el) - t + 1)
