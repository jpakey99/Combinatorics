def combinations(n, comb:str, possibilities, total):
    if n == 0:
        # print(comb)
        total.append(comb)
        return 1, total
    if n < 0:
        return 0, []
    else:
        i = 0
        for p in possibilities:
            # comb += str(p)
            r = combinations(n-p, comb + str(p), possibilities, total)
            i += r[0]
        return i, total


def eliminate_combinations_multiples_of_x(combs, x):
    new_combs = []
    for comb in combs:
        add = True
        for i in comb:
            if (int(i) % x) == 0:
                add = False
        if add:
            new_combs.append(comb)
    return new_combs


def only_combs_that_start_with(combs, x):
    new_combs = []
    for comb in combs:
        if comb[0] == str(x):
            new_combs.append(comb)
    return new_combs


def only_combs_that_end_with(combs, x):
    new_combs = []
    for comb in combs:
        if comb[-1] == str(x):
            new_combs.append(comb)
    return new_combs


poss = {1,2,3}
r = combinations(3, '', poss, [])
r1 = eliminate_combinations_multiples_of_x(r[1], 2)
print(r1)
r2 = only_combs_that_start_with(r1, 3)
print(r2)
r3 = only_combs_that_end_with(r1, 1)
print(r3)