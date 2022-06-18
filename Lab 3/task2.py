fdata=open('E:\Study Brac\Spring 22\CSE 221\LABs\Lab 3\input1.txt')
file=open('E:\Study Brac\Spring 22\CSE 221\LABs\Lab 3\output2.txt','w')
di = int(fdata.readline())

arr = []
for x in range(di):
    r = fdata.readline().split()
    arr.append(r)

class graphbuild:
    def __init__(self,new_node):
        self.new_node =new_node
        self.adj = {}
        for x in self.new_node:
            self.adj[x] = []
    def last(self,x,y):
        self.adj[str(x)].append(str(y))
    def BFS(self,nodes,endpoints):
        visited = []
        queue =[]
        visited.append(nodes)
        queue.append(nodes)
        #print('Visited',end=" ")

        file.write('Places: ')
        while queue:
            y = queue.pop(0)
            #print(y,end=' ')
            file.write(y + " ")
            if y == endpoints:
                break
            else:
                for x in self.adj[y]:
                    if x not in visited:
                        visited.append(x)
                        queue.append(x)


node=[]
for x in arr:
    node.append(str(x[0]))
new_graph= graphbuild(node)
for y in arr:
    for z in range(1,len(y)):
        new_graph.last(y[0],y[z])
new_graph.BFS('1','12')