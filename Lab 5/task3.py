fdata = open("E:\Study Brac\Spring 22\CSE 221\LABs\Lab 5\input3.txt")
file= open("E:\Study Brac\Spring 22\CSE 221\LABs\Lab 5\output3.txt","w")

data = fdata.read().split("\n")
n=int(data[0])
assi = [int(i) for i in data[1].split()]
call = data[2]
assi.sort()
ref = 0
serial =[]
jack_assignment =[]
jack_hours =0
jill_hours = 0

for i in call:
    if i == "J":
        serial.append(assi[ref])
        jack_assignment.append(assi[ref])
        jack_hours+= int(assi[ref])
        ref+=1
    elif i=="j":
        temp = jack_assignment.pop()
        jill_hours+= int(temp)
        serial.append(temp)

for x in serial:
    file.write(str(x))

file.write("\n")
file.write("Jack will work for "+str(jack_hours)+" hours"+'\n')
file.write("Jill will work for "+str(jill_hours)+" hours"+'\n')
