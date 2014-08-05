import sys
import math
import random
from bitarray import bitarray
def createGraph(graphfile):
    input_file = open(graphfile)
    adjList= {}
    adjListReverse= {}
    lines = input_file.readlines()
    ncount= lines.pop(0).replace("\n","")
    ncount = int(ncount)
    for i in range(1,ncount+1):
     adjList[i]=[]
     adjList[-i]=[]
     adjListReverse[i]=[]
     adjListReverse[-i]=[]
    for line in lines:
     l1,l2 = line.replace("\n","").split(" ")
     l1= int(l1)
     l2= int(l2)
     adjList[0-l1].append(l2)
     adjList[0-l2].append(l1)
     adjListReverse[l2].append(0-l1)
     adjListReverse[l1].append(0-l2)
    return adjList,adjListReverse,ncount

def DFSPost(adjListReverse):
    marked={}
    stack =[]
    print len(adjListReverse.keys())
    for k in adjListReverse:
     marked[k]=False
    sortMarked =  sorted(marked.keys())[:]
    #print sortMarked
    for k in sortMarked:
     if marked[k]==False:
      marked,stack = DFS1(stack,k,marked,adjListReverse)
    return stack    


def DFS1(stack,current,marked,adjListReverse):
    marked[current]=True
    for l in adjListReverse[current]:
     #print l
     if marked[int(l)]==False:
      marked,stack= DFS1(stack,l,marked,adjListReverse)
    stack.append(current) 
    return marked,stack

def DFS2(current,adjList,compHash,count):
    compHash[current]=count
    for l in adjList[current]:
     if compHash[l]<0:
      compHash= DFS2(l,adjList,compHash,count)
    return compHash

print "main function"
adjList,adjListReverse,ncount  = createGraph(sys.argv[1])
print "DFS reverse starting"
stack = DFSPost(adjListReverse)
print "DFS reverse ended"
compHash={}
for key in adjList.keys():
 compHash[key]= -1
#print compHash
count=0;
print "DFS forward starting"
while(len(stack)!=0):
  item = stack.pop()
  if compHash[item]<0:
   compHash = DFS2(item,adjList,compHash,count)
   count= count+1
#print compHash 
print "DFS forward ending"
ans=1
for x in range(1,ncount+1):
 if compHash[x]==compHash[-x]:
  ans=0
  break
print ans
