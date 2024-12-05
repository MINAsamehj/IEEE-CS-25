n,k = list(map(int, input().split()))
arr = list(map(int, input().split()))

arr.sort()

i =0
num_of_diff=0
j=0


while j <n:
    if arr[j] - arr[i] <k:
        j+=1
    elif arr[j] - arr[i] >k:
        i+=1

    elif arr[j] -  arr[i] ==k:
        i+=1
        j+=1
        num_of_diff+=1



print(num_of_diff)


