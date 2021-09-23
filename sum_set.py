import numpy as np

def sum_set(A: set, B: set) -> set:
    """
    A, B: set of numbers
    """
    l_a = [0] * (max(A) + 1)
    l_b = [0] * (max(B) + 1)
    for i in A:
        l_a[i] = 1
    for i in B:
        l_b[i] = 1
    l_a.reverse()
    l_b.reverse()
    poly_A = np.poly1d(np.array(l_a))
    poly_B = np.poly1d(np.array(l_b))

    l_res = list(np.polymul(poly_A, poly_B).c)
    l_res.reverse()
    
    res = set()

    for (i, x) in enumerate(l_res):
        if x == 0:
            continue
        res.add(i)

    return res

def sum_set_nary(A: set, n : int = 1) -> set:
    if n == 1:
        return A

    res = []
    if n % 2 == 0:
        res = sum_set_nary(A, n // 2)
    else:
        res = sum_set_nary(A, n - 1)

    if n % 2 == 0:
        res = sum_set(res, res)
    else:
        res = sum_set(res, A)

    return res


        
if __name__ == "__main__":
    A = {3,4,5}
    print(sum_set_nary(A, 1))
    print(sum_set_nary(A, 2))
    print(sum_set_nary(A, 3))