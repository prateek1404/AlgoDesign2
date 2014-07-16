import math



def fetchEdgeArray():
    input_file = open("clustering_big.txt")
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
    edgeArray.sort();
    return  edgeArray

edgeArray= fetchEdgeArray()
nodeHash={}
for x in range(0,len(edgeArray)):
 inputN = edgeArray[x]
 print "INPUT is "+str(inputN)
 inputNumber = list(inputN)
 if inputN not in nodeHash.keys():
  nodeHash[inputN]=inputN
  ndigits = len(inputN)
  for x in range(0,ndigits):
   inputNumber2 = list(inputN)
   if(int(inputNumber2[x])==0):
    inputNumber2[x]="1"
   else:
    inputNumber2[x]="0"
   toInsert1 = "".join(inputNumber2)
   print "with one change "+ toInsert1
   if toInsert1 not in nodeHash.keys(): 
    nodeHash[toInsert1]=inputN
   if x < len(inputN)-1:
    for y in range(x+1,ndigits): 
     inputNumber2= list(toInsert1)
     print inputNumber2
     if(int(inputNumber2[y])==0):
      inputNumber2[y]="1"
     else:
      inputNumber2[y]="0"
     toInsert2= "".join(inputNumber2)
     if toInsert2 not in nodeHash.keys():
      nodeHash[toInsert2]=inputN 
print nodeHash 
print len(nodeHash) 
