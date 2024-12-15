def find_min_diff(n, weights, idx, curr_sum, total_sum):
    if idx == n:
        return abs((total_sum - curr_sum) - curr_sum)
    
    include = find_min_diff(n, weights, idx + 1, curr_sum + weights[idx], total_sum)
    exclude = find_min_diff(n, weights, idx + 1, curr_sum, total_sum)
    
    return min(include, exclude)

n = int(input())
weights = list(map(int, input().split()))
total = sum(weights)

result = find_min_diff(n, weights, 0, 0, total)
print(result)
