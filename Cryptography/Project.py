import numpy as np


def Convert_To_List(s):
    l = []
    print("Messege converted to list of number :- ", end=" ")
    for i in s.lower():
        if i != ' ':
            l.append(ord(i) - 96)
        else:
            l.append(0)
    print(l)
    return l


def Conver_To_Matrix(l, A):
    print("\nList converted to matrix of vectors :- ")
    if len(l) % 3 != 0:
        for i in range(3 - len(l) % 3):
            l.append(0)
    ar = np.array(l)
    ar.shape = (int(len(l) / 3), 3)
    ar = np.transpose(ar)
    print(ar)
    print("\nList converted to encoded matrix :- ")
    ar = np.dot(A, ar)
    print(ar)
    return ar


def Decode(A, B):
    print("\nEncoded matrix converted to decoded matrix :- ")
    x = np.dot(A, B)
    print(x)
    return x


def Convert_To_String(l):
    print("\nDecoded matrix converted to string(message) :- ", end=" ")
    s = ""
    for i in range(len(l[0])):
        for j in range(len(l)):
            k = int(l[j][i])
            if k != 0:
                s = s + chr(k + 96)
            else:
                s = s + " "
    s = s.upper()
    print(s)


matrix = np.array([[0, 2, -1], [1, -2, 1], [-1, -1, 1]])
print("\nMatrix A :- \n", matrix)
Inverted_matrix = np.linalg.inv(matrix)
print("\nInverted matrix of A :- \n", Inverted_matrix)

s = "STUDYLINEARALGEBRA"
print("\nMessage :- ", s)
a1 = Convert_To_List(s)
a2 = Conver_To_Matrix(a1, matrix)
a3 = Decode(Inverted_matrix, a2)

Convert_To_String(a3)