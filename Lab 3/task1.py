fdata=open('E:\Study Brac\Spring 22\CSE 221\LABs\Lab 3\input1.txt')
file=open('E:\Study Brac\Spring 22\CSE 221\LABs\Lab 3\output1.txt','w')
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
    def output(self):
        for y in self.new_node:
            #print(node,"  ",self.adj[node])
            g =str(y) + "  " + str(self.adj[str(y)]) + '\n'
            #print(g)
            file.write(str(g))
            fdata.close()
node=[]
for x in arr:
    node.append(str(x[0]))
new_graph= graphbuild(node)
for y in arr:
    for z in range(1,len(y)):
        new_graph.last(y[0],y[z])
new_graph.output()