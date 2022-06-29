import numpy as np


def Decode(A, B):
    print("\nEncoded matrix converted to decoded matrix :- ")
    x = np.dot(A, B)
    print("A^(-1)*(AB) = \n", x)
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


matrix = np.array([[1, 1, 0], [2, 1, 1], [3, 2, 2]])
print("\nReciever Key A^(-1) :- \n", matrix)

a1 = np.array([[19, 38, 23, 35, 9, 35], [0, -34, -14, -34, 3, -33], [-18, -17, -18, -18, -14, -19]])
print("\nEncoded Matrix :- \n", a1)
a2 = Decode(matrix, a1)
Convert_To_String(a2)
