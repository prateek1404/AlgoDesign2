import sys
import json
import operator

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
    input_file = open("clustering1.txt")
    #input_file = open("testcase2.txt")
    lines = input_file.readlines()
    ncount= lines.pop(0).replace("\n","")
    ncount = int(ncount)
    edgeArray=[]
    edgeArray2=[]
    for line in lines:
     source,dest,cost = line.replace("\n","").split(" ")
     source = int(source)
     dest = int(dest)
     cost = int(cost)
     edgeArray.append({'source':source,'dest':dest,'cost':cost});
     edgeArray2.append({'source':source,'dest':dest,'cost':cost});
    edgeArray.sort(key=operator.itemgetter('cost'))
    unionF= {}
    currentSpacing=edgeArray[0]['cost']
    #print edgeArray
    for k in range(1,ncount+1):
     unionF[k]={'head':k};
    numberOfHeads = ncount;
    edgeLenth = len(edgeArray)
    while numberOfHeads!=4:
     selectedEdge = edgeArray.pop(0)
     src = selectedEdge['source']
     dest = selectedEdge['dest']
     currentSpacing = selectedEdge['cost']
     if(int(find(unionF,src))!=int(find(unionF,dest))):
      numberOfHeads= merge(unionF,src,dest,numberOfHeads)
    uniqueHeads=[]
    for h in unionF.keys():
     if unionF[h]['head'] not in uniqueHeads:
      uniqueHeads.append( unionF[h]['head'])
    print uniqueHeads
    currentSpacing = edgeArray2[0]['cost']
    for edge in edgeArray2:
     if(find(unionF,edge['source'])!=find(unionF,edge['dest'])):
      if edge['cost']<currentSpacing:
       currentSpacing= edge['cost']
       print " minium spacing is between"+str(edge['source'])+" and "+str(edge['dest'])
    print currentSpacing

if __name__ == '__main__':
    main()

