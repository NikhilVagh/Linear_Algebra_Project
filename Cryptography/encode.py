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

def Conver_To_Matrix(l,A):
    print("\nList converted to matrix of vectors :- ")
    if(len(l)%3!=0):
        for i in range(3 - len(l) % 3):
            l.append(0)
    ar = np.array(l)
    ar.shape = (int(len(l) / 3),3)
    ar=np.transpose(ar)
    print("B = \n",ar)
    print("\nList converted to encoded matrix :- ")
    ar=np.dot(A,ar)
    print("A*B = \n",ar)
    return ar

l = [0,2,-1,1,-2,1,-1,-1,1]
matrix = np.array(l)
matrix.shape = (3, 3)
print("\nSender key A :- \n",matrix)

s = "STUDYLINEARALGEBRA"
print("\nMessage :- ", s)
a1 = Convert_To_List(s)
a2 = Conver_To_Matrix(a1,matrix)