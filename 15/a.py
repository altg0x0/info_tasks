def search(arr, k):
    left = -1
    right = len(arr)
    while right - left > 1:
        delim = (left + right) // 2
        t = arr[delim]
        if t == k:
            return delim
        elif t > k:
            right = delim
        else:
            left = delim  
    return -1
    

n, k = map(int, input().split())  # not a repetition1
ar1 = list(map(int, input().split()))
ar2 = list(map(int, input().split()))
for el in ar2:
    print("YES" if (search(ar1, el) + 1) else "NO")
