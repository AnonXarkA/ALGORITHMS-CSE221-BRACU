fdata =open("E:\Study Brac\Spring 22\CSE 221\LABs\Lab 5\input1.txt")
file=open("E:\Study Brac\Spring 22\CSE 221\LABs\Lab 5\output1.txt","w")

n = int(fdata.readline())

def assignment(array,n):
    array = sorted(array,key=lambda x:x[1])
    emp_arr = []
    emp_arr.append(array[0])
    c = 1
    a = array[0][1]
    for x in array:
        if a <= x[0]:
            c+=1
            a= x[1]
            emp_arr.append(x)

    file.write(str(c)+"\n")
    for y in emp_arr:
        file.write(str(y[0])+" "+str(y[1])+"\n")

f =[]
array =[]
for i in fdata:
    line = i.strip()
    e = line.split()
    f.append(e)
for j in f:
    array.append([int(j[0]),int(j[1])])
assignment(array,n)                
