# ALGORITHMS-CSE221-BRACU


# LAB ASSIGNMENTS

<h3 align="left">Languages:</h3>
<p align="left"> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> </p>

# LAB 1 - Time complexity Lab 📝

1) File I/O: [10 marks] 
Parity: A number has even parity if it’s an even number, and odd parity if it’s an odd number. 
Palindrome: A palindrome is a sequence of characters which reads the same backward as forward, such as “madam”, “racecar” or “bob”. 

Given pairs of a number and a string, check the parity of the number and whether the string is a palindrome or not. In case of float/ decimal, indicate that it cannot have parity. In a text file, some pairs will be given in separate lines. Read the words from a text (input.txt) file, do the above mentioned operations, and save the outputs in another text (output.txt) file using File I/O operations. Finally, in a text file named “records.txt”, write the percentage of odd, even and no parity, and percentage of palindromes and non-palindromes. Ideally you should store the inputs from the text file into a data structure (e.g. array, list etc. ). You can either: 
● pass the array as an argument to the isPalindrome function and return the output array, OR, 
● you can check the words one by one using a loop and return true/false

Sample input (inside input.txt file): [Download input.txt] 
1 madam 
2 apple 
3.6 racecar 
89 parrot 
45.2 discord 

Sample output (inside output.txt file): 
1 has odd parity and madam is a palindrome 
2 has even parity and apple is not a palindrome 
3.6 cannot have parity and racecar is a palindrome 
89 has odd parity and parrot is not a palindrome 
45.2 cannot have parity and discord is not a palindrome 

Sample output (inside record.txt file): 
Percentage of odd parity: 40% 
Percentage of even parity: 20% 
Percentage of no parity: 40% 
Percentage of palindrome: 40% 
Percentage of non-palindrome: 60% 

Pseudocode for isPalindrome function: 
Word <- input 
IF word=null/empty THEN 
Return not palindrome 
N<- length of word 
For i<N/2 
If word[i] != word[N-1-i] 
Return not palindrome 
i++ 
Return palindrome 

2) N-th Fibonacci Number: [3 marks] 
You are given two different codes for finding the n-th fibonacci number. Find the time complexity of both the implementations and compare the two. 
See Fibonacci sequence to understand if this is new to you. 
Implementation - 1
def fibonacci_1(n): 
if n <= 0: 
print("Invalid input!") 
elif n <= 2: 
return n-1 
else: 
return fibonacci_1(n-1)+fibonacci_1(n-2) 
n = int(input("Enter a number: ")) 
nth_fib = fibonacci_1(n) 
print("The %d-th fibonacci number is %d" % (n, nth_fib)) 
Implementation - 2 
def fibonacci_2(n): 
fibonacci_array = [0,1] 
if n < 0: 
print("Invalid input!") 
elif n <= 2: 
return fibonacci_array[n-1] 
else: 
for i in range(2,n): 
fibonacci_array.append(fibonacci_array[i-1] + fibonacci_array[i-2]) 
return fibonacci_array[-1] 
n = int(input("Enter a number: ")) 
nth_fib = fibonacci_2(n) 
print("The %d-th fibonacci number is %d" % (n, nth_fib)) 



3) Graph Plot: [2 marks] 
Append the following code segment after the implementations given in the previous problem. [Yes, The code is given. Just Copy-Paste it]. This will generate a graph with the value of n along the x-axis and time required along the y-axis. You can see both the curves in the same graph for better comparison. Generate graphs for different values of n and see how the performances change drastically for larger values of n. 
Code for plotting graph: 
import time 
import math 
import matplotlib.pyplot as plt 
import numpy as np 
#change the value of n for your own experimentation 
n = 30 
x = [i for i in range(n)] 
y = [0 for i in range(n)] 
z = [0 for i in range(n)] 
for i in range(n-1):
start = time.time() 
fibonacci_1(x[i+1]) 
y[i+1]= time.time()-start 
start = time.time() 
fibonacci_2(x[i+1]) 
z[i+1]= time.time()-start 
x_interval = math.ceil(n/10) 
plt.plot(x, y, 'r') 
plt.plot(x, z, 'b') 
plt.xticks(np.arange(min(x), max(x)+1, x_interval)) 
plt.xlabel('n-th position') 
plt.ylabel('time') 
plt.title('Comparing Time Complexity!') 
plt.show() 


Ans: ⚡  <a href="https://github.com/AnonXarkA/ALGORITHMS-CSE221-BRACU/tree/main/Lab%201"> LAB 1</a> <br> 

# LAB 2 - Sorting lab  📝

<br>
Task 1: (5 marks)
Here is code of bubble sort. It’s run time complexity is θ(n2). Change the code in a way so that its time complexity is θ(n) for the best case scenario. Find the best case and change the code a little bit. And explain how you did it in a comment block of your code. 



def bubbleSort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1): 
            if arr[j] > arr[j+1]:
                swap( arr[j+1], arr[j] )
             
The first line of the input will contain N, which is the size of the array. Next line will contain the N number of elements. Output will contain the sorted elements.
 P.S: sample input and output may not be the preferred answer choice.
Input 1:
5 
3 2 1 4 5
Input 2:
6
10 20 5 15 25 30
Output 1:
1 2 3 4 5
Output 2:
5 10 15 20 25 30



Task 2: (5marks)
You have a list of elements and their prices. Select your preferred lists from the item based on lowest price. So to complete the task you have a tool called selection sort.
In selection sort:
Select the minimum element from the unsorted part of the given array.
Move the selected element to a sorted part of the array.
Repeat this process to make the unsorted array sorted.

Here is pseudo code:
for i ← 0 to n-1
   m=argminj (A[i], A[i+1], ....... A[n-1]) 
   swap (A[i], A[m])
end for

Use the above pseudo code to complete the selection sort.
First line of the input will contain N items and M preferred choices (where M ≤ N). The next line will contain the price of each element. Output will contain the price of M number of preferred elements. 

Input 1:
5 3
5 10 2 1 4
Input 2:
7 4
10 2 3 4 1 100 1
Output 1:
1 2 4 
Output 2:
1 1 2 3





Task 3: (5 marks)

Suppose you are given a task to rank the students. You have gotten the marks and id of the students. Now your task is to rank the students based on their marks using only insertion sort.
Here is the pseudocode for insertion sort for ascending order. You need to change it to descending order.
for i ← 0 to n-1
   temp ← A[i+1]
    j= i
   while j>=0
       if(A[j]>temp)
       	A[j+1] ←A[j]
        else
break 	
      j= j-1      
   end for
A[j+1] ← temp
end for
Implement this pseudocode to complete your task. 

First line will contain an integer N. The next line will contain N number of id of the students.The next line will contain the N number of the marks of corresponding students. Output will be ranking the id based on their marks (descending order).


Input 1:
5 
11 45 34 22 12
40 50 20 10 10 
Input 2:
6
1 2 3 4 5 6
50 60 80 20 10 30
Output 1:
45 11 34 22 12
Output 2:
3 2 1 6 4 5



Task 4: (5 marks)
Here is the problem, just simply sorting an array. Now, to sort the array you should use efficient sorting techniques. It will have worst-case time complexity better than the above sorting algorithms. The sorting algorithm pseudocode is given below:

MERGE (A, p, q, r )      
 n1 ← q − p + 1
 n2 ← r − q
Create arrays L[1 . . n1 + 1] and R[1 . . n2 + 1]
FOR i ← 1 to n1
 	DO L[i] ← A[p + i − 1]
FOR j ← 1 to  n2
 	DO R[j] ← A[q + j ]
L[n1 + 1] ← ∞
R[n2 + 1] ← ∞
 i ← 1
 j ← 1
FOR k ← p TO r
DO IF L[i ] ≤ R[ j]
THEN A[k] ← L[i]
          i ← i + 1
 		ELSE A[k] ← R[j]
j ← j + 1
 
MERGE-SORT (A, p, r)
if p < r                                                    // Check for base case
     q = (p + r)/2            
    MERGE-SORT  (A, p, q)                        
    MERGE -SORT (A, q+1, r)                         
    MERGE (A, p, q, r)                       


Take help from pseudocode or use your way to complete the task.
First line will contain N . The next line will contain N number of elements. The output will contain a sorted N number of elements (ascending order).
Input 1:
5 
5 -1 10 2 8


Input 2:
6
10 20 3 40 5 6
Output 1:
-1 2 5 8 10
Output 2:
3 5 6 10 20 40



Task 5 (5 marks)
Study the algorithm below and implement the quickSort method . Additionally you will also need to implement the “partition” method. After sorting, print both the unsorted array and sorted array and also the time it takes to complete sorting.

https://prnt.sc/cTkRiHjurDnh


b. Implement an algorithm “findK” that uses the “partition” algorithm to find the kth 
(smallest) element from an array without sorting. E.g. for the array in our example, the 5th element will be “9” 

Input:
The array: 1 3 4 5 9 10 10
K=5
K=7
K= 2
Output:
 9
10
3

<br>

Ans: ⚡  <a href="https://github.com/AnonXarkA/ALGORITHMS-CSE221-BRACU/tree/main/Lab%202"> LAB 2</a> <br> 
