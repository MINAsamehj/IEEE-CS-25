def generate_permutations(s, current, used, results):
    if len(current) == len(s):
        results.add("".join(current))
        return
    for i in range(len(s)):
        if used[i]:
            continue
        if i > 0 and s[i] == s[i-1] and not used[i-1]:
            continue
        used[i] = True
        current.append(s[i])
        generate_permutations(s, current, used, results)
        current.pop()
        used[i] = False

s = input().strip()
s = sorted(s)
results = set()
used = [False] * len(s)
generate_permutations(s, [], used, results)
results = sorted(results)
print(len(results))
print("\n".join(results))
