import numpy as np
def checkerboard(n):
    print("checker_board pattern")
    z=np.zeros((n,n),dtype=int)
    z[1::2,::2]=1
    z[::2,1::2]=1
    for i in range(n):
        for j in range(n):
            print(z[i][j],end=" ")
        print()
n=int(input("eneter your number"))
print(checkerboard(n))
