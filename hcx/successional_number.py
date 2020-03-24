import numpy as np
def find_successional_number(N, L):
    n = int(N / L) + 1
    for i in range(n, 0, -1):
        for l in range(L, i + 1):
            s = (i + i - l + 1) * l / 2
            if s == N:
                return list(range(i, i - l, -1))
            if s > N:
                break
        if (i + 1) * i / 2 < N:
            break
    return "No"

N =18
L =5
print(find_successional_number(N,L))