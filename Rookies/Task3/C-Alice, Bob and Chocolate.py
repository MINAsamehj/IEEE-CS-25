number_of_choco = int(input())
time = list(map(int, input().split()))



i = 0
j = number_of_choco -1

while j-i >1:
    if time[i] > time[j]:
        time[i] = time[i] - time[j]
        j-=1
    elif time[j] > time[i]:
        time[j] = time[j] - time[i]
        i+=1

    elif time[i] == time[j]:
        i+=1
        j-=1


if i ==j:
    j+=1

alice = i+1
bob = number_of_choco-j

print(alice , bob)

