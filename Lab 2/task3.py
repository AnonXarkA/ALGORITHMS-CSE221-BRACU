
from re import S


fdata=open('E:\Study Brac\Spring 22\CSE 221\LABs\Lab 2\input3.txt')
file=open('E:\Study Brac\Spring 22\CSE 221\LABs\Lab 2\output3.txt','w')

v = fdata.readline().split()
read_line1 = fdata.readline().split()
read_line2 = fdata.readline().split()

array_id =[]
array_mark = []

for x in read_line1:
    array_id.append(int(x))

for y in read_line2:
    array_mark.append(int(y))

def Insertionsort(v,stdnt_id,stdnt_marks):
    for x in range(len(stdnt_id)):
        i = stdnt_marks[x]
        j = stdnt_id[x]

        for y in range(x-1,-2,-1):
            if y <0:
                break
            elif i > stdnt_marks[y]:
                stdnt_marks[y] = stdnt_id[y]
                stdnt_id[y+1] = stdnt_id[y]

            else:
                break
        
        stdnt_marks[y+1] = i
        stdnt_id[y+1] = j

    st = str(stdnt_id)[1:-1]
    file.write(st)
    fdata.close()    

Insertionsort(v,array_id,array_mark)    