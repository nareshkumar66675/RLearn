import numpy as np

#Create Random Map
def generate_random_map(size=8, p=0.8):
    valid = False

    def is_valid(res):
        frontier, discovered = [], set()
        frontier.append((0,0))
        while frontier:
            r, c = frontier.pop()
            if not (r,c) in discovered:
                discovered.add((r,c))
                directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
                for x, y in directions:
                    r_new = r + x
                    c_new = c + y
                    if r_new < 0 or r_new >= size or c_new < 0 or c_new >= size:
                        continue
                    if res[r_new][c_new] == 'T':
                        return True
                    if (res[r_new][c_new] not in '#x'):
                        frontier.append((r_new, c_new))
        return False

    while not valid:
        p = min(1, p)
        res = np.random.choice(['-', 'x'], (size, size), p=[p, 1-p])
        res[0][0] = 'S'
        res[-1][-1] = 'T'
        valid = is_valid(res)
    return ["".join(x) for x in res]

def categorical_sample(prob_n, np_random):
    prob_n = np.asarray(prob_n)
    csprob_n = np.cumsum(prob_n)
    return (csprob_n > np_random.rand()).argmax()
