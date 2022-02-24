total = 0
globals()['total'] = 0


def new_g(n, start, end, i, s, possibilities):
    """
    Will find all paths in a graph that meets certain criteria
    :param n: total number of steps
    :param start: the starting node
    :param end: None if no end point is specified and a Node string if specified
    :param i: the number of steps taken
    :param s: the string construction to that point
    :param possibilities: A dictionary that has all nodes as keys and the values are out-vertices from that node.
    :return: Nothing, but will print out all paths as strings as well as calculate total number of paths
    """
    if n == 0:
        globals()['total'] = 0
        return
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
        globals()['total'] = 0
        new_g(n, start, end, i + 1, start, possibilities)
        return
    else:
        for p in possibilities[s[-1]]:
            new_g(n, start, end, i + 1, s + p, possibilities)


def get_total():
    return globals()['total']


if __name__ == '__main__':
    possibilities = {
        'A': ['B', 'A'],
        'B': ['A'],
        # 'C': ['A','B', 'C']
    }
    new_g(4, 'A', 'A', 0, '', possibilities)
    print(get_total())
