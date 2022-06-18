


fdata=open('E:\Study Brac\Spring 22\CSE 221\LABs\Lab 2\input1.txt')
file=open('E:\Study Brac\Spring 22\CSE 221\LABs\Lab 2\output1.txt','w')
read_line = int(fdata.readline())


v = fdata.readline().split()

bubble = list(map(int,v))

def Bubblesort(array):
    for x in range(len(array)-1):
        for y in range(len(array)-x-1):
            if array[y+1] < array[y]:
                array[y],array[y+1] = array[y+1],array[y]

    st = str(array)[1:-1]
    file.write(st)
    fdata.close()
Bubblesort(bubble)                 

"""
To allow faster Bubble Sort, we may check in the for loop if the items are swapped or not. 
If they aren't swapped, the array has been sorted, and we can exit the loop without completing all iterations.
For eaxmple,
1 < 2 => No swapping
2 < 3 => No swapping
3 < 4 => No swapping
5 > 4 => Swapping

so the best case for this code is O(n)
we can say sorted bubble sort best case is O(n)

"""