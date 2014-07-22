import math

def find(unionF,n):
 return unionF[n]['head']

def merge(unionF,src,dest):

 headNode = unionF[src]['head']
 otherNode = unionF[dest]['head']
 size1 = int(unionF[headNode]['size'])
 size2 = int(unionF[otherNode]['size'])
 if int(size1)<int(size2):
  temp = headNode
  headNode = otherNode
  otherNode= temp
 #nprint "merging heads"+str(headNode)+str(otherNode)
 for x in unionF.keys():
  if int(unionF[x]['head'])== int(otherNode):
   #print "head of "+str(x)+" is also "+str(otherNode)
   unionF[x]['head']= headNode
 unionF[headNode]['size']=size1+size2

def fetchEdgeArray():
    input_file = open("testcase4.txt")
    #input_file = open("testcase2.txt")
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
nodeHash={}
for node in edgeArray:
 nodeHash[node]={'head':node,'size':1}
for x in range(0,len(edgeArray)):
 inputN = edgeArray[x]
 for x in range(0,nbits):
  toInsert1 = inputN^(1<<x)
  if toInsert1 in edgeArray:
   if(int(find(nodeHash,inputN))!=int(find(nodeHash,toInsert1))):
    merge(nodeHash,inputN,toInsert1)
  if x < nbits-1:
   for y in range(x+1,nbits): 
    toInsert2= toInsert1^(1<<y)
    if toInsert2 in edgeArray:
     if(int(find(nodeHash,inputN))!=int(find(nodeHash,toInsert2))): 
      merge(nodeHash,inputN,toInsert2)
print len(nodeHash)
uniqueHead=[]
for keyf in nodeHash.keys():
 if nodeHash[keyf]['head'] not in uniqueHead:
  uniqueHead.append(nodeHash[keyf]['head'])
print "value of k is "+str(len(uniqueHead))
 
