import heapq
from collections import defaultdict


fdata = open("E:\Study Brac\Spring 22\CSE 221\LABs\Lab 4\input1.txt")
file = open("E:\Study Brac\Spring 22\CSE 221\LABs\Lab 4\output2.txt",'w')

data = int(fdata.readline())

def dijkstra(graph,source,destination):
    emp_list = []
    heapq.heappush(emp_list,(0,source))
    new_path = []
    new_titan = []
    emp = "0"

    while len(emp_list) != 0:

        cost,vertex = heapq.heappop(emp_list)
        new_titan.append(cost)
        for n,ncost in graph[vertex]:
            heapq.heappush(emp_list,(cost+ncost,n))
        if emp != vertex:
            new_path.append(vertex)
            emp = vertex
        elif vertex ==  destination:
            break
        else:
            pass

    return ((new_path))

for x in range(data):
    graph = defaultdict(list)
    v,num = map(int,fdata.readline().split())
    for x in range(num):
        u,v,w = map(str,fdata.readline().split())
        graph[u].append((v,int(w)))

    source,destination = "1","5"
    i = dijkstra(graph,source,destination)
    for x in i:
        file.write(x+" ")
    file.write('\n') 

