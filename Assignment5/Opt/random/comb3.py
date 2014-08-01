from bitarray import bitarray
import sys
def distance(pointArray,a,b):
 return (((float(pointArray[a]['x'])-float(pointArray[b]['x']))**2) + (float(pointArray[a]['y'])-float(pointArray[b]['y']))**2)**0.5

 return ((xdiff**2)+(ydiff**2))**0.5

def takeInput():
 input_file = open(sys.argv[1])
 lines = input_file.readlines()
 count= lines.pop(0).replace("\n","")
 count = int(count)
 pointArray=[]
 for line in lines:
  x,y=  line.replace("\n","").split(" ")
  pointArray.append({'x':x,'y':y})
 return pointArray


def fillUpTSP(TSP,sett):

   TSP[sett.to01()]={}
   for j in range(0,len(sett)):
     if j!=0:
      if sett[j]==1:
   #    print "element at index "+str(j)+" exists in sett"
       smallest = sys.maxint
       for k in range(0,len(sett)):
        if k!=j:
         if sett[k]==1:
    #      print "value of j is "+str(j)+" value of k is"+str(k)
          ty = sett[:]
          ty[j]=0
          #print sett
          #print "ty "+str(ty)
          leng = TSP[ty.to01()][k]+ distance(pointArray,k,j)
          if leng<smallest:
           smallest=leng
       TSP[sett.to01()][j]= smallest
     else:
       TSP[sett.to01()][j] = sys.maxint
   return TSP,previous 





def arrayOfSetsOf(TSP,previous,n,k):
   A={}
   setOfSize={}
   A={}
   setOfSize=[]
   for i in range(1,n):
    A[i]=[]
    if k==0:
     ba = bitarray(n)
     ba.setall(0)
     ba[0]=1
     ba[i]=1
     A[i]= [ba]
     setOfSize.append(ba)
     fillUpTSP(TSP,ba)
    else:
     if k>i:
      A[i]=[]
     else:
      for j in range(1,i):
       for l in previous[j]:
        s1=l[:]
        s1[i]=1
        A[i].append(s1)
        #setOfSize.append(s1)
        fillUpTSP(TSP,s1)
   #print setOfSize[k]
   previous = A.copy()
 #print len(setOfSize[m-1])
   return TSP




pointArray= takeInput()
#print pointArray
count = len(pointArray)

TSP={}
set1= bitarray(count)
set1.setall(0)
set1[0]=1
set1s = set1.to01()
TSP[set1s]={}
TSP[set1s][0]=0

previous={}

for m in range(0,count):
 print "processing for m= "+str(m)
 TSP,previous = arrayOfSetsOf(TSP,previous,count,m)
 #for sett in setOfSize:
 # TSP = fillUpTSP(TSP,sett)


arrayOf1 = bitarray(count)
arrayOf1.setall(1)
arrayS = arrayOf1.to01()
#print TSP[arrayS]
ans= sys.maxint
for b in range(1,count):
  dis = distance(pointArray,0,b)
 # print dis
  if TSP[arrayS][b]+dis<ans:
   ans = TSP[arrayS][b]+dis
print ans

 


