
def zero(x):
    arr = [1e9 for y in range(x+1)]
    arr[0] = 0
    for y in range(x+1):
        for v in str(y):
            arr[y] = min(arr[y],
                          arr[y-(ord(v)-48)]+1)
    return arr[x]

file = open("E:\Study Brac\Spring 22\CSE 221\LABs\lab 6\input1.txt","r")
file2 = open("E:\Study Brac\Spring 22\CSE 221\LABs\lab 6\output1.txt","w")
x = file.readline()
x = int(x)
print(zero(x),file=file2)