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
    for i in range(0,int(ncount)+1):
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
     for i in range(1,ncount+1):
      shortDist[i]={}
      for j in range(1,ncount+1):
        shortDist[i][j]={}
      #  print str(i) + ","+str(j)+","+str(k)
        if k==0:
         if i==j:
          shortDist[i][j][k]=0
         elif j in adjcostlist[i]:
          shortDist[i][j][k]=adjcostlist[i][j]
          if(adjcostlist[i][j]<overallShort):
           overcallShort=adjcostlist[i][j]
         else:
          shortDist[i][j][k]=sys.maxint
        else:
           if k-1 in shortDist[i][j]:
            print "k-1 exists"
           else:
            print "k-1 does not exist"
            print shortDist[i][j].keys()
           ans1 = shortDist[i][j][k-1]
           #print ans1
           #print shortDist[i][k][k-1]
           #print shortDist[k][j][k-1]
           ans2 = sys.maxint
           if shortDist[i][k][k-1]!=sys.maxint and shortDist[k][j][k-1]!= sys.maxint:
            ans2 = shortDist[i][k][k-1]+shortDist[k][j][k-1] 
           if ans2 < ans1:
            shortDist[i][j][k]=ans2
            if ans2<overallShort:
             overallShort=ans2
           else:
            shortDist[i][j][k]=ans1
            if ans1<overallShort:
             overallShort=ans1
    print overallShort
    for i in range(1,ncount+1):
     if shortDist[i][i]<0:
      negativeCycle=1 
    print negativeCycle
    return overallShort,negativeCycle
def main():
    # do nothing
    print "main function"
    addestlist_g1,adjcst1,ncount1,ecount1 = createGraph("g1.txt")
    addestlist_g2,adjcst2,ncount2,ecount2 = createGraph("g2.txt")
    addestlist_g3,adjcst3,ncount3,ecount3 = createGraph("g3.txt") 
    short1,negCyc1=    FloydWarshall(addestlist_g1,adjcst1,ncount1,ecount1) 
        
if __name__ == '__main__':
    main()

