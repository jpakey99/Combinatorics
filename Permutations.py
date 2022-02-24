def permutations(n):
    if len(n) <= 1:
        return n
    else:
        ws = []
        for i in range(0, len(n)):
            e = n[i]
            rest = n[:i] + n[i+1:]
            for p in permutations(rest):
                ws.append(e + p)
    return ws


w = permutations('12345')

