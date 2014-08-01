import sys


def arrayOfSetsOf(m,n):
 nop = range(0,n)
 for i in range(0,n):
   A[i]={}
   for k in range(1,k1+1):
    if k==1:
     A[i][k]=[nop[i]]
    else:
     array2=[]
     for j in range(0,i):
      #print "adding "+str(A[j][k-1])
      k= A[j][k-1].append(nop[i])
      #A[i][k] = nop[i]
      A[j][k].append(k)
     #print str(i)+","+str(k)+" "+str(A[i][k])
 


input_file = open("tsp.txt")
lines = input_file.readlines()
count= lines.pop(0).replace("\n","")
print count
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

print pointArray
print xArray
print yArray
for m in range(1,count+1):
 arrayOfSets{m}= arrayOfSetsOf(m)
 for sett in arrayOfSets{m}:
   for j in sett:
    if j!=1: 
     for k in sett:
      if k!=j:
       A[setid,j] = A[this_set-{J},k]+ C{k,j}
    else:
     if sett[setid]==1:
      A[sett[setid],j]= 0
     else:
      A[sett[setid],j] = sys.maxint
     

