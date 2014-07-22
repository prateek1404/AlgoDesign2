import math
import timeit

def find(unionF,n):
 return unionF[n]['head']

def merge(unionF,src,dest,childList):
 #start_time = timeit.default_timer()
 headNode = unionF[src]['head']
 otherNode = unionF[dest]['head']
 size1 = int(unionF[headNode]['size'])
 size2 = int(unionF[otherNode]['size'])
 if int(size1)<int(size2):
  temp = headNode
  headNode = otherNode
  otherNode= temp
 #nprint "merging heads"+str(headNode)+str(otherNode)
 #for x in unionF.keys():
 for x in childList[otherNode]:
  #print "head of "+str(x)+" is also "+str(otherNode)
  childList[headNode].append(x)
  unionF[x]['head']= headNode
 childList[otherNode]=[]
 unionF[headNode]['size']=size1+size2
 #elapsed = timeit.default_timer() - start_time
 #print "time elapsed during merge "+str(elapsed)
def fetchEdgeArray():
    input_file = open("clustering_big.txt")
    #input_file = open("testcase5.txt")
    lines = input_file.readlines()
    ncount,nbits= lines.pop(0).replace("\n","").split(" ")
    ncount = int(ncount)
    nbits = int(nbits)
    edgeArray=[]
    edgeArray2=[]
    for line in lines:
     edgeInt = line.replace(" ","").replace("\n","")
     edgeArray.append(int(edgeInt,2))
    #edgeArray.sort();
    return  edgeArray,nbits

edgeArray,nbits= fetchEdgeArray()
print "got the edgeArray"

nodeHash={}
childList={}
xorArray=[]
for x in range(0,nbits):
 xor1 =0^(1<<x)
 xorArray.append(xor1)
 if x< nbits -1:
  for y in range(x+1,nbits):
   temp = 0^(1<<y)
   xor2 = xor1| temp
   xorArray.append(xor2)
print len(xorArray)
print xorArray
for node in edgeArray:
 nodeHash[node]={'head':node,'size':1}
 childList[node]=[]
 childList[node].append(node)
# xor with each one in array and then merge 
for x in range(0,len(edgeArray)):
 inputN = edgeArray[x]
 print "node "+str(x)+" starting"
 for x in xorArray:
  toInsert = inputN^(x)
  if toInsert in nodeHash:
   #print "found a matching element"
   if(int(find(nodeHash,inputN))!=int(find(nodeHash,toInsert))):
    #print "found a matching element from different set"
    merge(nodeHash,inputN,toInsert,childList)
print len(nodeHash)
uniqueHead=[]
for keyf in nodeHash.keys():
 if nodeHash[keyf]['head'] not in uniqueHead:
  uniqueHead.append(nodeHash[keyf]['head'])
print "value of k is "+str(len(uniqueHead))
 
