from bitarray import bitarray

def distance(a,b):
 print "hello"

def arrayOfSetsOf(n,m):
 A={}
 allSets=[]
 setOfSize={}
 for k in range(0,m):
   A[k]={}
   setOfSize[k]=[]
   for i in range(0,n):
    #print str(k) + ","+str(i)
    A[k][i]=[]
    if k==0:
     ba = bitarray(n)
     ba.setall(0)
     ba[i]=1
     A[k][i]= [ba]
     setOfSize[k].append(ba)
    else:
     if k>i:
      A[k][i]=[]
     else:
      for j in range(0,i):
       for l in A[k-1][j]:
        s1=l[:]
        s1[i]=1
        A[k][i].append(s1)
        setOfSize[k].append(s1)
 #print setOfSize[m-1]
 #print len(setOfSize[m-1])
 return setOfSize

input_file = open("tsp.txt")
lines = input_file.readlines()
count= lines.pop(0).replace("\n","")
count = int(count)
pointArray=[]
xArray=[]
yArray=[]
for line in lines:
 x,y=  line.replace("\n","").split(" ")
 pointArray.append({'x':x,'y':y})
 xArray.append(x)
 yArray.append(y)
setid =0;
arrayOfSets= {}

#print pointArray
#print xArray
#print yArray




TSP={}
#total number of cities = 6
arrayOfSets= arrayOfSetsOf(5,5)
for m in range(0,5):
 print "m="+str(m)
 print arrayOfSets[m]
 for sett in arrayOfSets[m]:
   print "processing set "+str(sett)
   for j in range(0,len(sett)):
      if sett[j]==1:
       print "element at index "+str(j)+" exists in sett"
       TSP[sett]={}   
       for k in range(0,len(sett)): 
        if k!=j:
         if sett[k]==1:
          print "value of j is "+str(j)+" value of k is"+str(k)
          ty = sett[:]
          ty[j]=0
          #print sett
          print "ty "+str(ty)
         TSP[sett][j] = TSP[ty][k]+ distance(k,j)
    else:
     if k=='1000000000000000000000000':
      TSP[k][j]= 0
     else:
      TSP[k][j] = sys.maxint
'''
