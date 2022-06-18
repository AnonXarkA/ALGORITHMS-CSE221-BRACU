
fdata=open('E:\Study Brac\Spring 22\CSE 221\LABs\lab 6\input2.txt')
file=open('E:\Study Brac\Spring 22\CSE 221\LABs\lab 6\output2.txt','w')


def LCS(X,Y):
    m=len(X)
    n=len(Y)
    L=[]
    t=[0]*(m+1)
    for i in range(m+1):
        L.append(t)
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                L[i][j]=0
            elif X[i-1]==Y[j-1]:
                L[i][j]=L[i-1][j-1]+1
            else:
                L[i][j]=max(L[i-1][j],L[i][j-1])

    position=L[m][n]
    algo_string=[""]*(position+1)
    algo_string[position]=""
    i=m
    j=n
    while i>0 and j>0:
        if X[i-1]==Y[j-1]:
            algo_string[position-1]=X[i-1]
            i-=1
            j-=1
            position-=1
        elif L[i-1][j]>L[i][j-1]:
            i-=1
        else:
            j-=1
    return algo_string

length=fdata.readline()
strings=fdata.read().splitlines()
first=strings[0]
second=strings[1]
out_string=LCS(first, second)
out_string.pop()

pubg = {'Y':'Yasnaya', 'P':'Pochinki', 'S':'School', 'R':'Rozhok', 'F':'Farm', 'M':'Mylta', 'H':'Shelter', 'I':'Prison'}
for i in out_string:
    file.write(pubg[i]+" ")
file.write('\n')
prediction = (len(out_string)*100)//int(length)
file.write('Correctness of prediction: '+ str(prediction)+'%')