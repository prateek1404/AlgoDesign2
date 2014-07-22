import math

def find(unionF,n):
 return unionF[n]['head']

def merge(unionF,src,dest):

 headNode = unionF[src]['head']
 otherNode = unionF[dest]['head'][:]
 size1 = int(unionF[headNode]['size'])
 size2 = int(unionF[otherNode]['size'])
 if int(size1)<int(size2):
  temp = headNode[:]
  headNode = otherNode[:]
  otherNode= temp[:]
 #nprint "merging heads"+str(headNode)+str(otherNode)
 for x in unionF.keys():
  if int(unionF[x]['head'])== int(otherNode):
   #print "head of "+str(x)+" is also "+str(otherNode)
   unionF[x]['head']= headNode
 unionF[headNode]['size']=size1+size2

def fetchEdgeArray():
    input_file = open("../testcase5.txt")
    #input_file = open("testcase2.txt")
    lines = input_file.readlines()
    ncount,nbits= lines.pop(0).replace("\n","").split(" ")
    ncount = int(ncount)
    nbits = int(nbits)
    edgeArray=[]
    edgeArray2=[]
    for line in lines:
     edgeInt = line.replace(" ","").replace("\n","")
     edgeArray.append(edgeInt)
    #edgeArray.sort();
    return  edgeArray

edgeArray= fetchEdgeArray()
nodeHash={}
for node in edgeArray:
 nodeHash[node]={'head':node,'size':1}
for x in range(0,len(edgeArray)):
 inputN = edgeArray[x]
 inputNumber = list(inputN)
 ndigits = len(inputN)
 for x in range(0,ndigits):
  inputNumber2 = list(inputN)
  if(int(inputNumber2[x])==0):
   inputNumber2[x]="1"
  else:
   inputNumber2[x]="0"
  toInsert1 = "".join(inputNumber2)
  if toInsert1 in edgeArray:
   merge(nodeHash,inputN,toInsert1)
  if x < len(inputN)-1:
   for y in range(x+1,ndigits): 
    inputNumber2= list(toInsert1)
    if(int(inputNumber2[y])==0):
     inputNumber2[y]="1"
    else:
     inputNumber2[y]="0"
    toInsert2= "".join(inputNumber2)
    if toInsert2 in edgeArray:
     merge(nodeHash,inputN,toInsert2)
print len(nodeHash)
uniqueHead=[]
for keyf in nodeHash.keys():
 if nodeHash[keyf]['head'] not in uniqueHead:
  uniqueHead.append(nodeHash[keyf]['head'])
print "value of k is "+str(len(uniqueHead))
 
