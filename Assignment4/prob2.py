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
    '''for i in range(0,ncount):
     shortDist.append([])
     for j in range(0,ncount):
      shortDist[i].append([])
      for k in range(0,ncount):
       shortDist[i][j].append(sys.maxint) 
   '''  
    for k in range(0,ncount):
     shortDist[k]={}
     for i in range(0,ncount):
      shortDist[k][i]={}
      for j in range(0,ncount):
        shortDist[k][i][j]={}
        #print str(i) + ","+str(j)+","+str(k)
        if k==0:
         if i==j:
          shortDist[k][i][j]=0
         elif j in adjcostlist[i]:
          shortDist[k][i][j]=adjcostlist[i][j]
          if(adjcostlist[i][j]<overallShort):
           overcallShort=adjcostlist[i][j]
         else:
          shortDist[k][i][j]=sys.maxint
        else:
           ans1 = shortDist[k-1][i][j]
           #print ans1
           #print shortDist[i][k][k-1]
           #print shortDist[k][j][k-1]
           ans2 = sys.maxint
           #if shortDist[k-1][i][k]!=sys.maxint and shortDist[k-1][k][j]!= sys.maxint:
           ans2 = shortDist[k-1][i][k]+shortDist[k-1][k][j] 
           if ans2 < ans1:
            shortDist[k][i][j]=ans2
            if ans2<overallShort:
             overallShort=ans2
           else:
            shortDist[k][i][j]=ans1
            if ans1<overallShort:
             overallShort=ans1
    print "overallshort is "+ str(overallShort)
    for i in range(0,ncount):
     if shortDist[ncount-1][i][i]<0:
      negativeCycle=1 
    print negativeCycle
    return overallShort,negativeCycle
def main():
    # do nothing
    print "main function"
    addestlist_g1,adjcst1,ncount1,ecount1 = createGraph("testcase1.txt")
    print "done creting graph1"
    #addestlist_g2,adjcst2,ncount2,ecount2 = createGraph("g2.txt")
    #addestlist_g3,adjcst3,ncount3,ecount3 = createGraph("g3.txt") 
    short1,negCyc1=    FloydWarshall(addestlist_g1,adjcst1,ncount1,ecount1) 
        
if __name__ == '__main__':
    main()

