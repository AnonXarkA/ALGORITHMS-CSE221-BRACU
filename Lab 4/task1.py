from operator import le
import sys
import math
from queue import PriorityQueue


def dijkstra(graph,source):

    distance = [math.inf]* len(graph)
    distance[source-1] = 0

    visited = len(graph) * [False]
    prev = len(graph) * [None]

    Q = PriorityQueue()
    Q.put((distance[source-1],source))
    while Q.empty() is False:
        un = Q.get()[1]
        if visited[un-1]:
            continue
        visited[un-1] = True
        if graph[un] is not None:
            for y in graph[un]:
                v = y[0]
                alt = distance[un-1]+y[1]
                if distance[v-1] > alt:
                    distance[v-1] = alt
                    prev[v-1] = un
                    Q.put((distance[v-1],v))

    print(distance[-1])

fdata = open("E:\Study Brac\Spring 22\CSE 221\LABs\Lab 4\input1.txt")
sys.stdout = open("E:\Study Brac\Spring 22\CSE 221\LABs\Lab 4\output1.txt","w")

data = fdata.readlines()
new_route = []
new_case = []

for x in range(1,len(data)):
    y = data[x].split()
    if len(y) == 2:
        new_case.append(y)
    else:
        new_route.append(y)

for i in new_case:
    graph = {}
    for k in range(int(i[1])):
        edge = []
        value = list(map(int,new_route.pop(0))) 
        if value[0] in graph.keys():
            edge = graph[value[0]]
        edge.append(value[1:])
        graph[value[0]] = edge

    out = int(i[0])
    for j in range(1,out+1):
        if j not in graph:
            graph[j] = None

    graph = {un:v for un,v in sorted(graph.items())}
    dijkstra(graph,1)                           
