def findNearestGreaterFrequency(a):
    freq_dict = {}
    stack = []
    result = [-1] * len(a)

    for i in range(len(a)-1, -1, -1):
        freq_dict[a[i]] = freq_dict.get(a[i], 0) + 1
        while stack and freq_dict[a[stack[-1]]] <= freq_dict[a[i]]:
            stack.pop()
        if stack:
            result[i] = a[stack[-1]]
        stack.append(i)

    return result


a = [1, 1, 2, 3, 4, 2, 1]
output = findNearestGreaterFrequency(a)
print(output)
