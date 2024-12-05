n_of_cities, n_of_towers = map(int, input().split())  

cities = list(map(int, input().split()))

towers = list(map(int, input().split()))




def binary(city,towers):
    left = 0
    right = len(towers) - 1

    while left <= right:
        mid = (left + right) // 2

        if towers[mid] < city:
            left = mid + 1
        else:
            right = mid - 1

    return left - 1 if left > 0 else None



redius =0
for city in cities:


    left_index = binary(city , towers=towers)

    if left_index==None:
        distance= abs(city-towers[0])
    elif left_index==len(towers) - 1:
        distance = abs(city-towers[-1])
    else:
        distance = min(abs(city-towers[left_index]) , abs(city-towers[left_index+1]))

    redius  =max(redius, distance)



print(redius)


















