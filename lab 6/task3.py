fdata=open('E:\Study Brac\Spring 22\CSE 221\LABs\lab 6\input3.txt')
file=open('E:\Study Brac\Spring 22\CSE 221\LABs\lab 6\output3.txt','w')


def LCS(X,Y,Z):
    m=len(X)
    n=len(Y)
    o=len(Z)
    L=[[[0 for i in range(o + 1)] for j in range(n + 1)] for k in range(m + 1)]
    for i in range(m+1):
        for j in range(n+1):
            for k in range(o+1):
                if (i==0 or j==0 or k==0):
                    L[i][j][k]=0

                elif (X[i-1]==Y[j-1] and
                      X[i-1]==Z[k-1]):
                    L[i][j][k]=L[i-1][j-1][k-1]+1
                else:
                    L[i][j][k]=max(max(L[i-1][j][k],L[i][j-1][k]),L[i][j][k-1])

    return L[m][n][o]

new=fdata.read().split()
X=new[0]
Y=new[1]
Z=new[2]
file.write(str(LCS(X,Y,Z)))