def simulate_sequence(n, result=None):
    if result is None:
        result = []
    
    result.append(n)
    
    if n == 1:
        return result
    
    if n % 2 == 0:
        return simulate_sequence(n // 2, result)
    else:
        return simulate_sequence(3 * n + 1, result)

n = int(input())
sequence = simulate_sequence(n)
print(" ".join(map(str, sequence)))
