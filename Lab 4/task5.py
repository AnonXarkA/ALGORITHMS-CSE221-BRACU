from posixpath import split
import re


fdata = open("E:\Study Brac\Spring 22\CSE 221\LABs\Lab 4\input4.txt")
file = open("E:\Study Brac\Spring 22\CSE 221\LABs\Lab 4\output4.txt",'w')
data = int(fdata.readline())
def network(graph,source,c):
    new_detail = ["0"] * (c+1)
    new_detail[source] = 0
    new_data = ["&"]*(c+1)
    new_data[source] = 0
    path_node = ["None"] * (c+1)
    path_node[source] = source
    detail = {source:0}

    while len(detail) != 0:
        present_node = max(detail, key = lambda max_val: detail[max_val])
        del detail[present_node]

        if present_node in graph:
            for i in graph[present_node]:
                adjacency,len_of_adj = i
                if new_data[adjacency] == "&":
                    new_data[adjacency] = len_of_adj
                    detail[adjacency] = new_data[adjacency]
                else:
                    if new_data[adjacency] > new_data[present_node]+len_of_adj:
                        new_data[adjacency] = new_data[present_node]+len_of_adj
                        detail[adjacency] = new_data[adjacency]
                    path_node[adjacency] = str(path_node[present_node])+" "+ str(adjacency)
                    new_detail[adjacency] = str(new_detail[present_node])+" "+str(len_of_adj)
    output = ' '
    for i in range(1,c+1):
        x = list(map(int,str(new_detail[i]).split()))
        if str(source) == str(i):
            x.append(0)
        x.pop(0)
        if len(x) == 0:
            x.append(-1)
        if len(x) != 0:
            output += str((min(x)))+" "

    return(output)

for j in range(data):
    vertex,r = (map(int,fdata.readline().split()))
    emp_dict = {}
    i = 1
    while r >= i:
        s = list(map(int,fdata.readline().split()))
        if s[0] in emp_dict:
            emp_dict[s[0]].append((s[1],s[2]))
        else:
            emp_dict[s[0]] = [(s[1],s[2])]
        i += 1
    source = int(fdata.readline())
    if r == 0:
        file.write("0")
        file.write('\n')
    else:
        file.write(network(emp_dict,source,vertex))
        file.write("\n")