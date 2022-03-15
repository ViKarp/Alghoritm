import numpy as np
f = open("A_matrix.txt")
A = []
T = []
for line in f:
    targ = list(map(int, line.split()))
    A.append(targ)
    T.append(list(map(bool, targ.copy())))
A = np.array(A)
T = np.array(T)

#Проверка на правильность

n = len(A)
for i in A:
    if len(A) != len(i):
        exit()
#Построение транзитивной матрицы

for k in range(n):
    for i in range(n):
        for j in range(n):
            T[i][j] = T[i][j] or (T[i][k] and T[k][j])

#Столбец сумм строк

S = []
Flag = False
for i in range(n):
    if False in T[i]:
        Flag = True
    S.append(sum(T[i]))

if Flag == False:
    exit(0)

#Матрица перестановок

S_sort = sorted(S.copy(), reverse=True)
P = [[0]*n for i in range(n)]
for i in range(n):
    P[i][S.index(S_sort[i])] = 1
    if i != 0 and S_sort[i] == S_sort[i-1]:
        P[i][S.index(S_sort[i])] = 0
        P[i][S.index(S_sort[i], P[i-1].index(1)+1)] = 1

P = np.array(P)

#Матрица

P_t = P.transpose()
Tau = P.dot(T).dot(P_t)
K = P.dot(A).dot(P_t)
print("")



