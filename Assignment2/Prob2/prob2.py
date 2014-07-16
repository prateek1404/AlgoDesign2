import sys
import operator
import math 
incrementArray=[]
def prepareIncArray(nbits)
 for x in range(0,nbits):
  #incrementArray.append(int(math.pow(2,x)))
  for y in range(x+1,nbits):
   #print "x ="+str(x)+", y = "+str(y)
   diff2= int(math.pow(2,x) + math.pow(2,y))
   diff1 = int(math.pow(2,y)-math.pow(2,x))
   if diff1 not in incrementArray:
    incrementArray.append(diff1)
   if diff2 not in incrementArray:
    incrementArray.append(diff2)
 incrementArray.sort()
 


def find(unionF,n):
 return unionF[n]['head']

def merge(unionF,src,dest,numberOfHeads):
 
 headNode = unionF[src]['head']
 otherNode = unionF[dest]['head']
 #nprint "merging heads"+str(headNode)+str(otherNode)
 for x in range(1,len(unionF)+1):
  if int(unionF[x]['head'])== int(otherNode):
   #print "head of "+str(x)+" is also "+str(otherNode)
   unionF[x]['head']= headNode
 numberOfHeads = numberOfHeads-1
 #print numberOfHeads
 return numberOfHeads  


def main():
    input_file = open("clustering_big.txt")
    #input_file = open("testcase2.txt")
    lines = input_file.readlines()
    ncount,nbits= lines.pop(0).replace("\n","").split(" ")
    ncount = int(ncount)
    nbits = int(nbits)
    edgeArray=[]
    edgeArray2=[]
    for line in lines:
     edgeInt = int(line.replace(" ",""),2)
     edgeArray.append(edgeInt)
    edgeArray.sort(); 
    print edgeArray 
    prepareIncArray(nbits)   
    print incrementArray; 

if __name__ == '__main__':
    main()

