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


def permutations_x_at_y(ws, x, i):
    new_w = []
    for w in ws:
        if w[i] == x:
            new_w.append(w)
    return new_w


def permutations_start_with(ws, x):
    return permutations_x_at_y(ws, x, 0)


def permutations_end_with(ws, x):
    return permutations_x_at_y(ws, x, -1)


def permutations_x_greater_y(ws, i1, i2):
    new_w = []
    for w in ws:
        if int(w[i1]) > int(w[i2]):
            new_w.append(w)
    return new_w


def find_next_cycle_start(w:str, w_cycle):
    for i in range(1, len(w)+1):
        found_lowest_num = False
        for cycle in w_cycle:
            if str(i) in cycle:
                found_lowest_num = True
        if not found_lowest_num:
            return i
    return -1


def cycle_notation(ws):
    cycles = []
    for w in ws:
        w_cycle = []
        current_cycle = '1'
        current_index = 0
        l = 1
        while l <= len(w)-1:
            while int(w[current_index]) != int(current_cycle[0]):
                current_cycle += w[current_index]
                current_index = int(w[current_index]) - 1
                l+=1
            w_cycle.append(current_cycle)
            i = find_next_cycle_start(w, w_cycle)
            if i != -1:
                current_cycle = str(i)
                current_index = i -1
                l+=1
                if l == 5:
                    w_cycle.append(current_cycle)

        cycles.append(w_cycle)
    return cycles


w = permutations('12345')
# # ws = permutations_start_with(w, '1')
ws = permutations_end_with(w, '1')
# # print(permutations_x_greater_y(w, 2,3))
# # print(permutations_x_at_y(w, '1',0))
print(ws)
print(cycle_notation(ws))