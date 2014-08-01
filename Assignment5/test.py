from bitarray import bitarray
def arrayOfSetsOf(n,m):
 A={}
 nop = range(0,n)
 allSets=[]
 print nop
 for i in range(0,n):
   A[i]={}
   for k in range(0,m):
    A[i][k]=[]
    if k==0:
     A[i][k]= [[nop[i]]]
    else:
     if k>i:
      A[i][k]=[]
     else:
      array2=[]
      for j in range(0,i):
       for l in A[j][k-1]:
        toIns = l[:]
        toIns.append(nop[i])
        A[i][k].append(toIns)
        if k ==m-1:
         allSets.append(toIns)
# print allSets    
 return allSets

a = bitarray(25)
a.setall(0)
print a  
arrayOfSetsOf(25,2)

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
 arrayOfSets{m}= arrayOfSetsOf(n-1,m-1)
 for sett in arrayOfSets{m}:
   for j in sett:
    if j!=1:
     for k in sett:
      if k!=j:
       A[sett][j] = A[this_set-{J}][k]+ C[k,j]
    else:
     if sett[setid]==1:
      A[sett[setid],j]= 0
     else:
      A[sett[setid],j] = sys.maxint

