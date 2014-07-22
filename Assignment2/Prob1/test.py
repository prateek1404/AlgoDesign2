import sys
import json
import operator

def find(unionF,n):
 return unionF[n]['head']

def merge(unionF,src,dest,numberOfHeads):
 headNode = unionF[src]['head']
 otherNode = unionF[dest]['head']
 for x in range(1,len(unionF)+1):
  if int(unionF[x]['head'])== int(otherNode):
   print "head of "+str(x)+" is also "+str(otherNode)
   unionF[x]['head']= headNode
 numberOfHeads = numberOfHeads-1
 print unionF
 return numberOfHeads  


def main():
    input_file = open("testcase2.txt")
    lines = input_file.readlines()
    ncount= lines.pop(0).replace("\n","")
    ncount = int(ncount)
    edgeArray=[]
    for line in lines:
     source,dest,cost = line.replace("\n","").split(" ")
     source = int(source)
     dest = int(dest)
     cost = int(cost)
     edgeArray.append({'source':source,'dest':dest,'cost':cost});
    edgeArray.sort(key=operator.itemgetter('cost'))
    unionF= {}
    for k in range(1,ncount+1):
     unionF[k]={'head':k};
    numberOfHeads = ncount; 
    #for l in range(0,len(edgeArray)-4):
    while numberOfHeads!=4:
     selectedEdge = edgeArray.pop(0)
     src = selectedEdge['source']
     dest = selectedEdge['dest']
     print "source is "+str(src)
     print "dest is "+str(dest)
     if(int(find(unionF,src))!=int(find(unionF,dest))):
      numberOfHeads= merge(unionF,src,dest,numberOfHeads)
     #print "no of sets"+str(numberOfHeads)
    for h in unionF.keys():
     print unionF[h]['head'] 
if __name__ == '__main__':
    main()

