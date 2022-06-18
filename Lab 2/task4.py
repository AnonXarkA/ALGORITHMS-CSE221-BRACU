
fdata=open('E:\Study Brac\Spring 22\CSE 221\LABs\Lab 2\input4.txt')
file=open('E:\Study Brac\Spring 22\CSE 221\LABs\Lab 2\output4.txt','w')

v = int(fdata.readline())

read_line = fdata.readline().split()

def Merge(X,first,mid,last):
    empty_list = [0]*(last-first+1)
    x = first
    y = mid+1
    z = 0

    while(x<= mid and y <= last):
        if (X[y] >= X[x]):
            empty_list[z] = X[x]
            z += 1
            x += 1
        empty_list[z] = X[y]
        z += 1
        y += 1

    while ( mid >= x):
        empty_list[z] = X[x]
        z += 1
        x += 1

    while (last >= y):
        empty_list[z] = X[y]
        z += 1
        y += 1

    for k in range(first,last+1):
        X[k] = empty_list[k-first]

def Mergesort(X,first,last):
    if last > first:
        mid = (first+last)//2
        Mergesort(X,first,mid)
        Mergesort(X,mid+1,last)
        Merge(X,first,mid,last)


arr = []
for x in read_line:
    arr.append(int(x))

Mergesort(arr,0,(v-1))
file.write(str(arr)[1:-1])
fdata.close()            