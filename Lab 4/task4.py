from calendar import c
from dis import dis
import math
from os import remove
given_graph = {"A":[["B",4],["H",6],["MOTIJHEEL",3]],"B":[["A",4],["G",2],["C",7]],"C":[["B",7],["F",7],["D",3]],"D":[["C",3],["E",1]],"E":[["D",1]],"F":[["C",7],["G",2],["MOGHBAZAR",4]],"G":[["B",2],["H",3],["J",1],["F",2]],"H":[["A",6],["I",5],["G",3]],"I":[["H",5],["J",7]],"J":[["G",7],["I",7],["K",6]],"K":[["J",6],["L",4],["MOGHBAZAR",7]],"L":[["K",4],["MOGHBAZAR",7]],"MOTIJHEEL":[["A",3]],"MOGHBAZAR":[["F",4],["K",7],["L",2]]}

def Dijkstra(given_graph,source,destination):
    if {} ==   given_graph:
        print(1, file = openFile2)
        return
    else:
        desti = {}
        queue = []
        previous = {}
        
        for keys in given_graph.keys():
            desti[keys] = math.inf
            previous[keys] = None
            queue.append(keys)

        desti[source] = 0
        while queue != []:
            minimum = math.inf
            min_indx = None
            for x in queue:
                if minimum > desti[x]:
                    minimum = desti[x]
                    min_indx = x
            val = given_graph[min_indx]
            for i in val:
                if previous[i[0]]==None or desti[i[0]]==math.inf:
                    alter = i[1]
                else:
                    alter = desti[previous[i[0]]]+i[1]
                if alter<desti[i[0]]:
                    desti[i[0]]=alter
                    previous[i[0]]=min_indx
            queue.remove(min_indx)
        c = destination
        road = []
        while c != None:
            road.append(c)
            c = previous[c]
        print(road)

Dijkstra(given_graph,"MOTIJHEEL","MOGHBAZAR")                                           

