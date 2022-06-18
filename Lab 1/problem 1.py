
num_even = 0
total_num =0
num_odd= 0
non_parity=0
palindromes = 0
non_palindromes = 0
word = 0


fdata=open('E:\Study Brac\Spring 22\CSE 221\LABs\Lab 1\input.txt')
fdata2=fdata.read()
file=open('E:\Study Brac\Spring 22\CSE 221\LABs\Lab 1\output.txt','w')
data=(fdata2.split('\n'))


for x in data:
    i = x.split(" ")
    if (float(i[0])%2 == 0):
        
        file.write(i[0]+" " + " has even parity and ")
        num_even += 1
        total_num += 1
        

    else:
        try:
            int(i[0])
        except:
            file.write(i[0]+" " +" cannot have parity and ")
            total_num += 1
            non_parity += 1
    
        else:
            file.write((i[0])+" " + " has odd parity and ")
            num_odd += 1
            total_num += 1
            
    
    #code for pallindrome
    z = i[1]
    
    strg= z.lower()
    reverse = reversed(z)
    if list(z) == list(reverse):
        file.write(z + " " + " is a palindrome")
        palindromes += 1
        word +=1
        file.write('\n')
    else:
        file.write(z + " "+ " is a not palindrome")
        non_palindromes += 1
        word += 1
        file.write('\n')


   
output = open('E:\Study Brac\Spring 22\CSE 221\LABs\Lab 1\\records.txt','w')
output.write("Percentage of odd parity: " +str(((num_odd/total_num)*100))+'%' +'\n' + "Percentage of even parity:" + str(((num_even/total_num)*100))+'%'+"\n" +"Percentage of no parity:" + str(((non_parity/total_num)*100))+'%'+"\n" + "Percentage of palindrome:" + str(((palindromes/word)*100))+'%'+"\n" +"Percentage of non-palindrome:"+ str(((non_palindromes/word)*100))+'%')
output.write("\n")
fdata.close()
output.close()


        




    






