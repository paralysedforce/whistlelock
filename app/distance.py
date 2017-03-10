import numpy as np

def edit_distance(s1, s2, del_cost, ins_cost, sub_cost = None):
    """Calculates Levenshtein distance between s1 and s2, with substitution
    costs given by the L1 norm"""
    d = np.zeros((len(s1)+1, len(s2)+1), dtype=int, order='F')
    m = len(s1) + 1; n = len(s2) + 1

    if not sub_cost:
        def sub_cost(c1, c2): return abs(c1 - c2)

    for i in range(m):
        d[i, 0] = i * del_cost
    for j in range(n):
        d[0, j] = j * ins_cost

    for jj in range(len(s2)):
        for ii in range(len(s1)):
            i, j = ii + 1, jj + 1
            if s1[ii] == s2[jj]:
                d[i, j] = d[i-1, j-1]
            else:
                d[i, j] = min([d[i-1, j] + del_cost,
                    d[i, j-1] + ins_cost,
                    d[i-1, j-1]+ sub_cost(s1[ii], s2[jj])])
    return d[-1, -1]

def main():
    a1 = np.array([1, 2, 3])
    a2 = np.array([1, 2, 9])
    print(edit_distance(a1, a2, 100, 1))

if __name__ == '__main__':
    main()
