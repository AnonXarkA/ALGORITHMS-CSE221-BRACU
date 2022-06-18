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

![image](http://0x0.st/ou4b.png)

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

# LAB 3 - BFS Lab (graph, array list, matrix coding) 📝

<br>
![image](http://0x0.st/ou4c.png) 

Suppose one fine morning, you woke up in the world of Pokémon. Now you decided to become a Pokémon master just like your childhood idol Ash Ketchum. 
In order to do so, you have to defeat the gyms/bad guys in the places you walk into in a limited amount of time. Your goal is to get to the Victory Road as quickly as possible. 
Task 1: Graph Building [5 marks]
You were given a map of the region. Create a Graph (preferably with adjacent lists) that represents all the places of the region. To help us calculate, we shall assign a number to each of the places on the map:
Places
Designated Number
Connected Places
Pallet Town (Starting Point)
1
2
Cerulean City
2
3, 4, 5
Celadon City
3
4,7,11
Lavender Town
4


Viridian City
5
6, 7
Cinnabar Island
6
7, 8
Fuchsia City 
7
11
Safari Zone
8
9, 10
Team Rocket’s Lair
9
10
Indigo Plateau
10
11
Pewter City
11
12
Victory Road (Destination)
12




Sample Inputs:
12
17
1	2
2	3
2	4
2	5
3	4
3           7
3           11
5	6
5	7
6	7
6	8
7	11
8	9
8	10
9	10
10	11
11	12

[Here in the first row, 12 means the number of places. In the second row, 17 means the total number of connections. The third row indicates that 1 and 2 are connected. The same rule applies for the rest of the rows. Assume that the first place is the Starting point and the last place is the destination]
12
1	2
2	3	4	5
3	4         7          11
4
5	6	7
6	7         8
7	11
8	9	10
9	10
10	11
11	12
12

[Here in the first row, 12 means the number of places. In the second row, 1 is connected to 2. In the third row, 2 is connected to 3, 4, and 5. The same rule applies for the rest of the rows. Assume that the first place is the Starting point and the last place is the destination]


Create a graph using the above values!


Task 2: Breadth-First Search (BFS) [5 marks]
Since you are a genius and you have an idea of the BFS algorithm, you can calculate the least number of cities you need to visit to get to your destination, Victory Road. Implement a BFS algorithm to determine the places you need to visit to get to the victory road!

Sample Pseudocode for the BFS implementation: (You are allowed to try different approaches  with same or less time complexity, but the outputs must match)

visited =[0]*noOfPlacesOrNodes , queue =[]
BFS (visited, graph, node, endPoint)
	Do visited[int(node)-1] 🡨 1
	Do queue 🡨 append(node)
	While queue not empty
    	Do m 🡨 pop()
    	Print m  // [into output text file]
    	If m= endPoint break
    	For each neighbour of m in graph
        	If visited[int(neighbour)-1] = 0
       		 Do visited[int(neighbour)-1] 🡨 1
       		 Do queue 🡨 append(neighbour)

#Driver
Read data from input.txt and create a graph
BFS(visited, graph, ‘1’, ‘12’)

Sample Inputs: 
Same as Task 1

Sample Output:
Places: 1 2 3 4 5 7 11 6 12

Task 3: Depth-First Search (DFS) [5 Marks]
Now, imagine your rival, Gary, who was also sent to the Pokémon world, wants to become Pokémon master before you. He is planning to get to Victory Road using the DFS algorithm. Implement a DFS algorithm to determine the places he needs to visit to get to the victory road!

Sample Pseudocode for the DFS implementation: (You are allowed to try different approaches with same or less time complexity, but the outputs must match)

visited =[0]*noOfPlacesOrNodes
printed = [] #this will store the graph traversing sequence
DFS_VISIT (graph, node)
           Do visited[int(node)-1] 🡨 1
	printed.append(node)
	For each node in in graph[node]
		If node not visited
			DFS_VISIT (graph, node)

#This part is needed if the graph is disconnected. 
DFS (graph, endPoint)
	For each node in graph
		If node not visited
			DFS_VISIT (graph, node)
	Print “printed” list in a loop till you get the end point

#Driver
Read data from input.txt and create a graph
DFS(graph, ‘12’)


Sample Inputs: 
Same as Task 1

Sample Output:
Places: 1 2 3 4 7 11 12




Task 4
Dalai Lama is visiting Maldives, the land of thousand islands. There are a total of N islands in Maldives numbered from 1 to N. All pairs of islands are connected to each other by bidirectional bridges running over water.
Given Dalai Lama’s health condition, crossing these bridges require a lot of efforts. He is standing at Island #1 and wants to reach the Island #N, where he will attend a ceremony where leaders of all countries are gathered to celebrate his life and achievements. Find the minimum number of bridges that Dalai Lama shall have to cross, if he takes the optimal route.


Input:
First line contains T. T testcases follow.
First line of each test case contains two space-separated integers N, M.
Each of the next M lines contains two space-separated integers X and Y, denoting that there is a bridge between Island X and Island Y.

Output:
Print the answer to each test case in a new line.

Constraints:
1 ≤ T ≤ 10
1 ≤ N ≤ 104
1 ≤ M ≤ 105
1 ≤ X, Y ≤ N

Sample Input:
2 – there are 2 graphs in the test case (text file)
3 2 – 3 indicates that the first graph contains 3 vertices. 2 indicates the number of edges/connections
1 2 – there is a connection between vertex 1 and 2 
2 3 – there is a connection between vertex 2 and 3
4 4 - 4 indicates that the second graph contains 4 vertices. 4 indicates the number of edges/connections
1 2  – there is a connection between vertex 1 and 2
2 3 – there is a connection between vertex 2 and 3
3 4 – there is a connection between vertex 3 and 4
4 2 – there is a connection between vertex 4 and 2
 
 
Sample Output:
2
2
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Task 5: Comparison [5 Marks]
Now, calculate the time-complexity of the BFS (Task 2) and DFS (Task 3) algorithms you used (both for matrix and adjacency list). Also show who gets to the victory road first and why. 



Not mandatory task(But Try it for Yourself): (No marks)
Can you print the places’ names instead of the designated numbers as output? 
The given BFS code will not work for disconnected graphs. Can you modify this bfs code so that it can work for disconnected graphs as well?
Can you detect the cycle using dfs? 

If you don’t know these, try to find it out. Take help from STs and faculties . 
Remember that: a bit more learning will never hurt. 

<br>

Ans: ⚡  <a href="https://github.com/AnonXarkA/ALGORITHMS-CSE221-BRACU/tree/main/Lab%203"> LAB 3</a> <br> 

# LAB 4 - Shortest path Lab 📝

TASK 1 [5 Marks]

Oh No! Wall Maria is Breached! Titans (human eating creatures) are coming. Eren has to reach his home as soon as possible to save his mother.

For simplicity, let’s think of Eren's hometown map containing N places and M roads. A road is a connection between two places.Here, each place is represented by a unique number between 1 and N. 

Suppose, each road is represented by i and each ith road connects 2 places ui and vi (ui and vi are the unique number of the places) and this road is overrun by wi titans. You can assume Eren’s current position as 1 and Eren’s home as N. Now help Eren to find a path so that he has to face as minimum number of titans as possible.

For example, in the following graph (vertices represent places and edges represent roads), Eren has to face a minimum 5 titans by using the path 1 → 4 → 3 → 5.

![image](http://0x0.st/ou4A.png)

Input Format:


First line contains a number T which represents the number of test cases.

For each test case:


First line will contain 2 numbers N, M representing the number of places and roads respectively. 

Each of the following M lines will contain 3 numbers ( ui vi wi ) representing one of the roads that connects places ui, vi and is guarded by wi titans.


Output Format:


For each test case, print one number which will be the minimum number of titans Eren has to face to reach his home. It is ensured that there exists roads connecting Eren’s current position to his home.

Sample Input:
3
1 0
2 1
1 2 10
5 6
3 5 1
1 2 1
2 3 4
1 4 2
4 3 2
2 5 5

Sample Output:
0
10
5

Sample Description:
Here we have 3 test cases.

In the 1st case, there is 1 place and 0 roads. So, Eren is already at home, i.e. he has to face 0 titans.

In the 2nd case, there are 2 places and 1 road connecting them which is guarded by 1 10 titans. So, Eren has to face 10 titans to reach home.

In the 3rd case, the example graph shown before is given. For that, it was shown that Eren has to face at least 5 titans.


Hint 1:
You can use the following pseudocode of Dijkstra’s algorithm.

function Dijkstra(Graph,source):
dist[source]0                           	// Initialization
create a priority queue Qfor the vertices		// min-heap
create a list visited for the vertices
for each vertex v in Graph:
if vsource:
dist[v]                	// Unknown distance from source to v
prev[v]␀             	// Predecessor of v
add v to Q with priority value dist[v]
visited[v]False
while Q is not empty:                      	// The main loop
uQ.extract_min()              // Remove and return best vertex
if visited[u]:
continue
visited[u]True
for each neighbor v of u:
altdist[u]+length(u,v)
if alt<dist[v]:
dist[v]alt
prev[v]u
add v to Q with priority value dist[v]
return dist,prev
Note:
What are you supposed to return for problem 1?
Do you need to compute prev?
Hint 2:
	Min-heap data structure is used to implement the priority queue. There are libraries that implement this.
Hint 3:
	Use adjacency list representation of Graph while reading from input.
Hint 4:
	Try to incorporate wi’s into the adjacency list.

TASK 2 [5 Marks]

Modify your code for the first problem to find the path Eren has to follow to face the minimum number of titans.

For the previous sample input, the output is:
1
1 2
1 4 3 5

Sample Description:
Here we have 3 test cases.

In the 1st case, there is 1 place and 0 roads. So, Eren is already at home, i.e. the path is: 1.

In the 2nd case, there are 2 places and 1 road connecting them which is guarded by 1 10 titans. So, the path to face minimum titans is the only existing path: 1 → 2.

In the 3rd case, the example graph shown before is given. For that, it was shown that, to face the minimum number of titans, Eren has to follow the path: 1 → 4 → 3 → 5.


TASK 3 [1.5+ 1.5 + 2 = 5 Marks]

If there are N places and M roads, what are the time complexities of the solutions you provided in problem 1 & problem 2 respectively?
If the number of titans in each road is exactly 1, there is an O(N+M) algorithm to solve this problem. What is it?
Note: If you can use any known algorithm, write its name and the inputs that will be given to it. Otherwise, give a pseudocode of the algorithm.

TASK 4 [5 marks]
Problem Description: A portion of the map of Dhaka is given in the picture. 
There are 2 mother nodes Motijheel, which is the source, and Moghbazar the destination. The other nodes from A to L represent intersections. There are multiple routes to reach from source to destination. The table below shows the weights of each route which represent the level of traffic. The higher the value, higher the traffic. Using your knowledge on graph implement Dijkstra’s algorithm. Print the output. 
BFS also gives the shortest path between source and destination. Why not use BFS in this situation?


![image](http://0x0.st/ou4m.png)




TASK 5 [5 Marks]

In a computer network, there are N devices and M links. A link is a one way connection from one device to another. Each link has a data transfer rate d it can support.

The data transfer rate of a connection from one device to another is the minimum data transfer rate of the links in that connection. [You can think of connection as a directed path. So, a connection from device u to device v is a sequence of links that joins a sequence of distinct devices where the links are directed from u to v.]


![This is an image](http://0x0.st/ou4a.png)



For example, in the network above, there can be three possible connections from 1 to 4:

(i) 1 → 2 → 4 : alt = 3
(ii) 1 → 3 → 4: alt = 2>3
(iii) 1 → 3 → 2 → 4: alt = 6 >3

In connection (i), there are two links: 1 → 2 with data rate 3, 2 → 4 with data rate 7. So, data transfer rate of this connection is minimum of 3 and 7, that is 3.
Similarly, data transfer rate of connection (ii) and (iii) are 2 and 6 respectively.

Now, the maximum data transfer rate from a device u to a device v is the maximum of the data transfer rates of all possible connections from u to v. For example, the maximum data transfer rate from 1 to 4 that this network supports is 6 (through connection (iii)).


Now, given a computer network, you have to calculate the maximum data transfer rate this network supports from a designated source device to all other devices.

Input Format :


First line contains a number T which represents the number of test cases.

For each test case:

First line contains 2 numbers N, M representing the number of devices and links respectively. 

Each of the following M lines will contain 3 numbers ( ui vi di ) representing a link from device ui to device vi with data transfer rate di.
The last line contains a number s, which is the source device.

Output Format :

For each test case, print a list of numbers, where ith number represents the maximum data transfer rate from s to i.
Note: print 0 when s == i and print -1 if there is no connection from s to i.


Sample Input: 
4
1 0
1
2 1
1 2 1
1
2 1
1 2 1
2
4 5
3 2 6
1 2 3
2 4 7
3 4 2
1 3 8
1

Sample Output:
0
0 1
-1 0
0 6 8 6

Sample Description:

Here we have 4 test cases.

In the 1st case, there is 1 device and 0 links, so there is no edge. Here the source device is 1. As the maximum data transfer rate between device 1 to 1 itself  is 0, the output is 0.

In the 2nd case, there are 2 devices and 1 link. Here the source device is 1. From device 1→1 the data transfer rate is 0. The maximum data transfer rate between 1→ 2 devices is 1 (As there is only 1 data rate).  So the output is 0 1.

In the 3rd case, there are 2 devices and 1 link. Here the source device is 2. From the input we can see that there is a connection between 1→ 2 with a data transfer rate of 1. but there is no connection between 2→1. So, from 2→1 the output will be -1 as noted above in the output format. And for 2→2 the output will be 0. So, the output is -1 0.

In the 4th test case, the example graph is given. Here the source device is 1. From 1→1, output is 0. From device 1 to device 2 there can be 2 possible paths, 1→2  and 1→3→2. The maximum data transfer rate for 1→2 will be 6 if we consider this path 1→3→2. Similarly, From 1→3, there is only one path and the data transfer rate is 8, so output is 8. For 1→4 the example is given in the beginning. So the output is 0 6 8 6.

Hint:
In the shortest path problem, you calculate path length by summing all edge weights in the path. Whereas in this problem you need to calculate data transfer rate which is obtained by taking the minimum of all edge weights in the path.
In the shortest path problem, you are trying to minimize path length, whereas in this problem you are trying to maximize data transfer rate.
[In Dijsktra’s algorithm, initialize dist array differently and change the codes related to priority queue for maximization]

You can use the following pseudocode which is based on these hints.
function Network(Graph,source):
         
dist[source]                           	// Initialization
create a priority queue Qfor the vertices		// Max-priority Queue
for each vertex v in Graph:
if vsource:
dist[v] -       // Unknown data transfer rate from source to v
prev[v]NULL         // Predecessor of v
add v to Q with priority value dist[v]
while Q is not empty:                      	// The main loop
uQ.extract_max()              // Remove and return best vertex
for each neighbor v of u:
altmin(dist[u],length(u,v))
if alt>dist[v]:
dist[v]alt
prev[v]u
add v to Q with priority value dist[v]
return dist,prev

Note: The libraries for priority queue may only implement min-heap data structure. But for this problem, we need a max-heap.

Ans: ⚡  <a href="https://github.com/AnonXarkA/ALGORITHMS-CSE221-BRACU/tree/main/Lab%204"> LAB 4</a> <br> 

# LAB 5 - Greedy 📝

Task 1 [10 marks]:
Suppose, you have N number of assignments with their time intervals- i.e. starting and ending times. As you are a student, you need to find out how you can finish the maximum number of assignments. Now, Implement a greedy algorithm to find the maximum number of assignments that can be completed by you.The following conditions must be met when writing the code: A student can only work on a single assignment at a time.
The input will contain N assignments, and then N lines with the starting time and ending time in the format given below:
N
S₁ E₁
S₂ E₂
…….
Sn En

You have to read input from a file. The output will contain the maximum number of assignments that can be completed followed by  the intervals of the selected assignment. Sample input and output is given below.  Name your input file “task1_input.txt”. Make sure to try out different input examples to ensure that your code is working for different cases. Include the input file in your zipped submission folder.

![image](http://0x0.st/ou4u.png)


A  greedy algorithm for the above problem is discussed below. Before you look at the algorithm it is recommended that you spend some time and try to think of a solution yourself.

//arr[ ][ ] is a 2D array-each index contains the start and finish time of each assignment
Assignment_Selection (arr[ ][ ], n) 
Add the 1st assignment from the sorted array in a queue/list “selected”
initialize a variable count = 1. 
Current finish time f = arr[0][1] //(finish time of first assignment)
For each remaining assignment in index c:
If the starting time of this assignment is greater or equal to the ending time of previously selected assignment, f
then count++
f=arr[c][1]
Add the start and finish time of assignment in index c to “selected”
Print count.
Print the queue/list selected 

Task 2 [5 marks]:

 . Each activity has a time interval- i.e. a start and a finish time. The activities can be distributed between M people. Implement a greedy algorithm to find the total number of activities that can be completed by M people. The following conditions must be met when writing the code:
One person cannot do activities with overlapping time intervals, so each person can do only one activity at a given time interval. 
Each activity can be completed by only one person.

For task 2 the pseudocode is provided below. You have to modify the pseudocode to complete Task 2. 

![image](http://0x0.st/ou4S.png)

The input will contain N and M, and then N lines with the start time and finish time in the format given below:

N M
S₁ F₁
S₂ F₂
…….
Sn Fn

You have to read input from a file. The output will contain the total number of activities that can be completed. Sample input and output is given below.  Name your input file “task2_input.txt”. Make sure to try out different input examples to ensure that your code is working for different cases. Include the input file in your zipped submission folder.

![image](http://0x0.st/ou4Q.png)

Task 3 [5 marks]:

Jack and Jill’s parents decide to make their children do some house chores. So they list a set of activities that can be completed in a whole day. In order to complete each activity a certain amount of time (in hours) is required. The parents randomly call each of their children several times separately to choose from the given activities. In each call the children choose an activity based on the following conditions:
In each call, each of them chooses one activity
Jack has to choose an activity that has not been selected yet.
Jill, being very little, should choose an activity that Jack has already chosen so that she can help her older brother because she cannot do such tasks by herself.
Jack does not like doing chores, so he decides he would choose the activity that requires the shortest amount of time to complete among the remaining activities. 
Jill really adores her brother and wants to help him out the most she can, so in each call she decides to choose the activity that needs the maximum time to complete out of the activities chosen by Jack so far.

Implement a greedy algorithm that will meet all above conditions. The input will be N- the number of tasks, followed by a sequence of N numbers denoting the time it takes to complete each task and then a call string which is a string of characters only containing J or j representing who is called next Jack (J) or Jill (j). The input format will be:

N
T₁ T₂…… Tn
JJjJjjJ

Assume that both the children will be called and Jack will be called either the same or greater number of times than Jill. You should output the sequence of tasks chosen and the total hours each of the children will be working. Sample input output is given below. You should read from a file. Name the file “task3_input.txt” and include it in the submission folder. Sample input output is given below:

![image](http://0x0.st/ou4j.png)

A possible greedy algorithm for the above problem is discussed below. Before you look at the algorithm it is recommended that you spend some time and try to think of a solution yourself.

Sort the activities in ascending order of time in an array
Create a stack or priority queue for Jack’s current chosen task. 
Initialize index to 0.
Create variables for sequence, Jack’s hours and Jill’s hours
For each character c in the call string
If (c==”J”)
Push value of the index of sorted array in the stack/priority queue
Append the value in the sequence
Increment index
Add the value to Jack’s hours
else if  (c==”j”)
Pop the top of the stack or highest value from priority queue
Append the popped value in the sequence
Add the popped value to Jill’s hours
Print sequence, Jack’s hours and Jill’s hours



Task 4: (5 marks)
A square number is an integer number whose square root is also an integer. For example 1, 4, 81 are some square numbers. Given two numbers a and b you will have to find out how many square numbers are there between a and b (inclusive).
 
Input 
Each line contains two integers a and b (0 < a ≤ b ≤ 100000). Input is terminated by a line containing two zeroes. This line should not be processed. 

Output
For each line of input produclllle one line of output. This line contains an integer which denotes how many square numbers are there between a and b (inclusive). 

Sample Input 
1 4
1 10
0 0 

Sample Output 
2 
3

Ans: ⚡  <a href="https://github.com/AnonXarkA/ALGORITHMS-CSE221-BRACU/tree/main/Lab%205"> LAB 5</a> <br> 

# LAB 6 - LCS code 📝

Problem 1 [5 marks]
We would like to find the minimum number of steps required to get 0 from any number, when you can only subtract a digit present in that number in a single step.
For example, if you are given 25. Then you can either subtract 2 or 5 from 25. Let's subtract 5 then we will get 20. Then we can subtract 2 and get 18 and so on. The minimum number of steps to get from 25 to 0 is shown below:
25→20→18→10→9→0.
Now you need to write a DP program to find the minimum number of steps to solve the problem for any input. Input range will be from 0 to 999.
Pseudo-code is not given because it is quite a basic dp problem!




Problem 2 (LCS) [10 Marks]:


PUBGM (Player Unknown’s BattleGrounds Mobile) is one of the most popular online battle royale games. PMPL (PUBGM Pro League) is the biggest tournament of south asia and Future Station a team from Bangladesh has qualified for the final round of the tournament. MagneT also known as “The zone magnet” for his accuracy of in-game zone predictions is the IGL (Team leader) of the team and he predicted the zone sequence before a match in the finals. For the match of map Erangel his prediction was,

![image](http://0x0.st/ou42.png)

On that match the team had a very good result and actual zone sequence of that match was:

![image](http://0x0.st/ou4_.png)

Now, you have to find out the longest common zone sequence from MagneT’s prediction and actual match by using LCS (Longest Common Subsequence) algorithm. Then verify the correctness of MagneT’s prediction. For correctness you will use the formula given below.
Correctness = (Length of longest common zone sequence × 100) ÷ Number of zones 
Note: Zone meta given here is completely fictional. Please do not match it with the real game zone meta.

Hint: You have to store zone center values according to keywords first. You can use the following pseudo code of LCS algorithm.

LCS(X, Y):
m <- length of X + 1
n <- length of Y + 1
for i <- 1 to m:
c[i,0] <- 0
t[i,0] <- null/None
for j <- 1 to n:
	c[0,j] <- 0
	t[0,j] <- null/None
	for i <- 1 to m:
		for j <-1 to n:
			if X[i] = Y[j]:
				c[i,j] <- c[i-1,j-1]+1
				t[i,j] <- diagonal
			else if c[i-1,j] >= c[i,j-1]:
				c[i,j] <- c[i-1,j]
				t[i,j] <- up
			else: 
				c[i,j] <- c[i,j-1]
				t[i,j] <- left

Sample Input:
8	//Number of zones           
YRSPFMHI	//Zone sequence of the match
YPSRFMHI	//Zone sequence of MagneT’s prediction

Sample Output:
Yasnaya Pochinki Farm Mylta Shelter Prison
Correctness of prediction: 75%



Problem 3 (LCS for 3 string) [10 Marks]:

You know about how to find the Longest Common Subsequence (LCS) between two strings using dynamic programming. Let’s make it a bit challenging. I will give you three strings instead of two, and now you need to find out the Longest Common Subsequence (LCS) among these three strings. Sounds interesting, right? I know you can do it!

Input:
Each input will consist of three strings in each line. The length of each string will be no greater than 100. 

Output:
Output the length of the longest common subsequence of the given three strings.

Sample Input 1:
hell
hello
bella

Sample Output 1:
3

Sample Input 2:
abbcdab
daccbadb
abccdaab

Sample Output 2:
4

Hint: For this problem you have to construct LCS for 3 parameters. You can use the following pseudo code to find out the longest common subsequence of three strings.


The followings are for your understanding:

 
LCS(X, Y, Z):
    m <- length[X] + 1
    n <- length[Y] + 1
    o <- length[Z] + 1
    c[m][n][o]
    t[m][n][o]
    for i <- 1 to m:
    	for j <- 1 to n:
		for k <-1 to o:
			if i = 0 Or j = 0 Or k = 0:
				c[i][j][k] <- 0
				t[i][j][k] <- null/None
			else:
				if x[i] = y[j] And x[i] = z[k]:
					c[i][j][k] <- 1 + c[i-1][j-1][k-1]
                            			t[i][j][k] <- diagonal
				else:
					if c[i-1][j][k] >= c[i][j-1][k]:
						max <- c[i-1][j][k]
						if max >= c[i][j][k-1]:
							c[i][j][k] <- max
                                    				t[i][j][k] <- up-up-left
						
						else:
							max <- c[i][j][k-1]
                                    				c[i][j][k] <- max
                                    				t[i][j][k] <- left-up-up
					else:
						max <- c[i][j-1][k]
						if max >= c[i][j][k-1]:
							c[i][j][k] <- max
                                    				t[i][j][k] <- up-left-up
						else:
							max <- c[i][j][k-1]
                                    				c[i][j][k] <- max
                                    				t[i][j][k] <- left-up-up




3D Array:
We already know how to operate 2D arrays. Now we have to use 3D arrays in order to construct LCS with 3 parameters. Multidimensional array means multiple arrays of different dimensions or sizes can be held by a single array. We will learn about 3D arrays with an example.
Suppose we want to store midterm and final marks separately of four different courses of three students in a single array. We can easily do it by using a 3D array.

![image](http://0x0.st/ou4L.png)

This is the pictorial view of the given scenario.Normally we can denote an array of 3 dimensions by this notation A[ ][ ][ ]. If we initialize this array empirically it will be like,
A[3][4][2]
Here, A is a 3D array where it has a size of 3 which represents 3 students. Each of 3 indices can hold an array of size 4 which indicates the different courses. And indices of these arrays can hold arrays of size 2 where each index represents the marks of mid and final.
For extracting the specific values from array A, we can simply use these instructions,

print(A[0][1][0])
print (A[2][2][1])
print(A[1][3][0])
First command will give 35 as output because first it will access the 0 th index of A. Then it will go through the index number 1 of it’s connected array and finally index number 0 of the array which is connected with the index number 1 of 2nd array will be accessed and give its value as output which is 35. Same procedure will be applied for the rest of the instructions. The second and third commands will give outputs 17 and 46 respectively. For traversing this array you can use the given codes.

Python:
for i in range(len(A)):
    print("Student: ",(i+1))
    for j in range(len(A[i])):
        print("Course: ",(j+1))
        print("Marks of Mid and Final: ")
        for k in range(len(A[i][j])):
            print(A[i][j][k],end=" ")
        print()
    print()

Java:
for (int i = 0; i < A.length; i++) {
	System.out.println("Student: "+(i+1));
	for (int j = 0; j < A[i].length; j++) {
		System.out.println("Course: "+(j+1));
		System.out.println("Marks of Mid and Final: ");
		for (int k = 0; k < A[i][j].length; k++) {
			System.out.print(A[i][j][k]+" ");
		}
		System.out.println();
	}
	System.out.println();
}




Output: 
Student:  1
Course:  1
Marks of Mid and Final: 
30 25
Course:  2
Marks of Mid and Final:
35 40
Course:  3
Marks of Mid and Final:
41 45
Course:  4
Marks of Mid and Final:
26 26

Student:  2
Course:  1
Marks of Mid and Final:
41 45
Course:  2
Marks of Mid and Final:
43 47
Course:  3
Marks of Mid and Final:
49 44
Course:  4
Marks of Mid and Final:
46 47

Student:  3
Course:  1
Marks of Mid and Final:
10 15
Course:  2
Marks of Mid and Final:
35 20
Course:  3
Marks of Mid and Final:
11 17
Course:  4
Marks of Mid and Final:
29 16



Ans: ⚡  <a href="https://github.com/AnonXarkA/ALGORITHMS-CSE221-BRACU/tree/main/lab%206"> LAB 6</a> <br> 



