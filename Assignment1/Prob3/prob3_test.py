import sys
import json


def main():
    input_file = open("edges2.txt")
    lines = input_file.readlines()
    print lines
    ncount,ecount= lines.pop(0).replace("\n","").split(" ")
    ncount = int(ncount)
    ecount = int(ecount)
    adjlist=[]
    for i in range(0,int(ncount)+1):
     adjlist.append([])   
    edgeArray=[]
    for line in lines:
     source,dest,cost = line.replace("\n","").split(" ")
     source = int(source)
     dest = int(dest)
     cost = int(cost)
     #if len(adjlist[source]) == 0:
     #  adjlist[source] = [{'dest':dest,'cost':cost}]
     #else:
     adjlist[source].append({'dest':dest,'cost':cost})
     #if len(adjlist[dest]) ==0:
     # adjlist[dest] = [{'dest':source,'cost':cost}]
     #else:
     adjlist[dest].append({'dest':source,'cost':cost})
    U =[]
    B = []
    for i in range(0,ncount):
     U.append(i+1)
    for i in range(1,ncount):
     B.append(i+1)
    A =[]
    A.append(1)
    totalCost = 0
    print adjlist
    while(len(A)!=len(U)):
     # pick the edge in adjacency lists of A with minimum edge length
     selectedEdge=0
     #minCost = adjlist[A[0]][0]['cost']
     minCost = 82343
     A.sort()
     print A
     for edge in A:
      for a in adjlist[edge]:
       if a['dest'] not in A:
        if a['cost']<minCost:
         minCost = a['cost']
         selectedEdge = a
     totalCost = totalCost+int(minCost) 
     #print "Edge selected"+str(selectedEdge)
     print selectedEdge 
     A.append(selectedEdge['dest'])
    print "totalCost="+str(totalCost) 
if __name__ == '__main__':
    main()

