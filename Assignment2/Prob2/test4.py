import math
def find(nodeArray,s):
 return nodeArray[s]

def merge(nodeHash,src,dest):
 print "merging "+src+" and "+dest
 print "size of head of src "+str(int(nodeHash[nodeHash[src]['head']]['size']))
 print "size of head of dest "+str(int(nodeHash[nodeHash[dest]['head']]['size']))
 if int(nodeHash[nodeHash[src]['head']]['size'])>int(nodeHash[nodeHash[dest]['head']]['size']):
  headNode = nodeHash[src]['head']
  otherNode = nodeHash[dest]['head']
 else:
  headNode = nodeHash[dest]['head']
  otherNode = nodeHash[src]['head']
 nodeHash[headNode]['size'] = int(nodeHash[headNode]['size'])+int(nodeHash[otherNode]['size'])
 #nprint "merging heads"+str(headNode)+str(otherNode)
 for x in nodeHash.keys():
  if int(nodeHash[x]['head'],2)== int(otherNode,2):
   #print "head of "+str(x)+" is also "+str(otherNode)
   nodeHash[x]['head']= headNode
 return nodeHash



def fetchEdgeArray():
    input_file = open("testcase6.txt")
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
  uniqueHead.append(nodeHash[keyf])
print "value of k is "+str(len(uniqueHead))
 
