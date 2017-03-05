def r_search(arr, k):
    la = 0
    r = len(arr)
    while r - la > 1:
        d = (la + r) // 2
        t = arr[d]
        if t > k:
            r = d
        else:
            la = d  
    return arr[la]
    

def la_search(arr, k):
    la = -1
    r = len(arr) - 1
    while r - la > 1:
        d = (la + r) // 2
        t = arr[d]
        if t >= k:
            r = d
        else:
            la = d  
    return arr[r] 
    
    
n, k = map(int, input().split())
ar1 = list(map(int, input().split()))
ar2 = list(map(int, input().split()))
for ela in ar2:
    print(min(r_search(ar1, ela), la_search(ar1, ela), key=lambda x: abs(x - ela)))
