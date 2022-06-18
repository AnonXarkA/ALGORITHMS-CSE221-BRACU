

fdata=open('E:\Study Brac\Spring 22\CSE 221\LABs\Lab 5\input2.txt')
file=open('E:\Study Brac\Spring 22\CSE 221\LABs\Lab 5\output2.txt','w')
n=(fdata.readline().splitlines())

def assignment(array,n):
    array=sorted(array,key=lambda x:x[1])
    emp_array=[]
    emp_array.append(array[0])
    c = 1
    a=array[0][1]
    for i in array:
        if i[0]>=a:
            c+=1
            a=i[1]
            emp_array.append(i)
    return c,emp_array

emp=n[0]
n=int(emp[0])
m=int(emp[2])
f=[]
array=[]
for j in fdata:
    line=j.strip()
    e=line.split()
    f.append(e)
for i in f:
    array.append([int(i[0]),int(i[1])])
x,output=assignment(array,n)
for i in range(0,m-1):
    for j in output:
        if len(output)==1:
            break
        else:
            array.remove(j)
    out,output= assignment(array,n)
    c=x+out
file.write(str(c)+"\n")       