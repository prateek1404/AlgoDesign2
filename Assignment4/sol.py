import sys
import json


def createGraph(graphfile):
    input_file = open(graphfile)
    lines = input_file.readlines()
    ncount,ecount= lines.pop(0).replace("\n","").split(" ")
    ncount = int(ncount)
    ecount = int(ecount)
    adjdestlist=[]
    adjcostlist={}
    for i in range(0,int(ncount)):
     adjdestlist.append([])
     adjcostlist[i]={}   
    edgeArray=[]
    for line in lines:
     source,dest,cost = line.replace("\n","").split(" ")
     source = int(source)
     dest = int(dest)
     cost = int(cost)
     adjdestlist[source-1].append(dest-1)
     adjcostlist[source-1][dest-1]=cost
    return adjdestlist,adjcostlist,ncount,ecount

def FloydWarshall(adjdestlist,adjcostlist,ncount,ecount):
    shortDist= {}
    distancesArray=[]
    overallShort = sys.maxint
    negativeCycle=0


    for k in range(0,ncount):
     if negativeCycle==1:
      break
     for i in range(0,ncount):
      if negativeCycle==1:
       break
      if k==0:
       shortDist[i]={}
      for j in range(0,ncount):
        if negativeCycle==1:
         break;
        if k==0:
         if i==j:
          shortDist[i][j]=0
         elif j in adjcostlist[i]:
          shortDist[i][j]=adjcostlist[i][j]
          if(int(adjcostlist[i][j])<int(overallShort)):
           overallShort=adjcostlist[i][j]
         else:
          shortDist[i][j]=sys.maxint
        else:
          ans1 = shortDist[i][j]
          ans2 = shortDist[i][k]+shortDist[k][j]
          if i!=j: 
           if ans2 < ans1:
            shortDist[i][j]=ans2
            if ans2<overallShort:
             overallShort=ans2
           else:
            if ans1<overallShort:
             overallShort=ans1
          else:
           if ans2<0:
            negativeCycle=1
            break
    if negativeCycle==0:  
     print "overallshort is "+ str(overallShort)
    else:
     print "negative cycle exists...cant compute shortest path"

    return overallShort,negativeCycle
def main():
    # do nothing
    print "main function"
    addestlist_g1,adjcst1,ncount1,ecount1 = createGraph("g3.txt")
    print "done creting graph3"
    #addestlist_g2,adjcst2,ncount2,ecount2 = createGraph("g2.txt")
    #addestlist_g3,adjcst3,ncount3,ecount3 = createGraph("g3.txt") 
    short1,negCyc1=    FloydWarshall(addestlist_g1,adjcst1,ncount1,ecount1) 
        
if __name__ == '__main__':
    main()

