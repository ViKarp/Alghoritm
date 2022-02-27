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

for i in range(n):
    for j in range(n):
        for k in range(n):
            T[i][j] = T[i][j] or (T[i][k] and T[k][j])

#Столбец сумм строк

S = []
Flag = False
for i in range(n):
    if False in T[i]:
        Flag = True
    S.append(sum(T[i]))

#if Flag == False:
    #exit()

#Матрица перестановок
#TODO
S_sort = sorted(S.copy())
P = np.array([np.array([0]*n)]*n)

for i in range(n):
    P[i][S.index(S_sort[i])] = 1
    if i != 0 and S_sort[i] == S_sort[i-1]:

        P[i][S.index(S_sort[i])] = 0
        P[i][S.index(S_sort[i], )] = 1



#Матрица

P_t = P.transpose()
Tau = P.dot(T).dot(P_t)



