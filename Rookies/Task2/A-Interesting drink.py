n = int(input())
prices = list(map(int, input().split()))

q=int(input())
money = [int(input()) for _ in range(q)]

prices.sort()

def binary(prices, day):
    low =0
    high = len(prices) -1


    while low <= high:
        mid = (low + high) // 2
        if prices[mid] <= day:
            low = mid + 1  # Search for more affordable shops
        else:
            high = mid - 1  # Reduce the range
    return low


for day in money:
    index = binary(prices,day )
    print(index)