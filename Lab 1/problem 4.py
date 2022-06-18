
fdata=open('E:\Study Brac\Spring 22\CSE 221\LABs\Lab 1\input2.txt')
file=open('E:\Study Brac\Spring 22\CSE 221\LABs\Lab 1\output2.txt','w')
dimension = int(fdata.readline())
A=[]
for x in range(dimension):
    r = fdata.readline().split()
    raw_line = list(map(int,r))
    A.append(raw_line)
B=[]
for x in range(dimension):
    r = fdata.readline().split()
    raw_line = list(map(int,r))
    B.append(raw_line)

def Multiply_matrix(A,B):
    
    C=[[0]*len(A) for y in range(len(A))]
    for x in range(0,len(A)):
        for y in range(0,len(A)):
            for j in range(0,len(A)):
                C[x][y] += A[x][j]*B[j][y]
    print(C) 
    file.write(str(C))
    fdata.close()

Multiply_matrix(A,B)



