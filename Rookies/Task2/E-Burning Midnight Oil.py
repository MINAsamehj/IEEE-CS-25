


n,k = map(int, input().split())

def k_v_test(k,v):
    p=0
    total = 0
    while v // (k ** p) > 0:
        total = total + v //(k**p)
        p+=1

    return total


low = 1
high = n

#this is a random comment in the middle to confuse u

while low < high:
    mid = (low + high) // 2
    n_test = k_v_test(k, mid)
    if n_test >= n:
        high = mid  
    else:
        low = mid + 1  

print(low)

#another random comment
