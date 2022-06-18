
fdata=open('E:\Study Brac\Spring 22\CSE 221\LABs\Lab 2\input2.txt')
file=open('E:\Study Brac\Spring 22\CSE 221\LABs\Lab 2\output2.txt','w')
read_line = fdata.readline().split()
spt = fdata.readline().split()
array = []

v = int(read_line[0])
arr = int(read_line[1])
for x in spt:
    array.append(int(x))

X = array[-arr:]

def Selectionsort(k):
    for x in range(len(X)):
        min_index = x
        for y in range(x+1 , len(X)):
            if X[y] < X[min_index]:
                min_index = y
                X[x],X[min_index] = X[min_index],X[x]

    print(X)
    st = str(X)[1:-1]
    file.write(st)
    fdata.close()
Selectionsort(v)                