total = 0
globals()['total'] = 0


def new_g(n, start, end, i, s, possibilities):
    if i == n:
        if end is None:
            globals()['total'] += len(possibilities[s[-1]])
            for p in possibilities[s[-1]]:
                print(s + p)
        else:
            if end in possibilities[s[-1]]:
                globals()['total'] += 1
                print(s + end)
        return
    if i == 0:
        new_g(n, start, end, i + 1, start, possibilities)
    else:
        for p in possibilities[s[-1]]:
            new_g(n, start, end, i + 1, s + p, possibilities)


if __name__ == '__main__':
    possibilities = {
        'A': ['B', 'A'],
        'B': ['A'],
        # 'C': ['A','B', 'C']
    }
    new_g(4, 'A', 'A', 0, '', possibilities)
    print(globals()['total'])
