from bitarray import bitarray
def arrayOfSetsOf(n,m):
 A={}
 allSets=[]
 setOfSize={}
 for k in range(0,m):
   print "processing for "+str(k)
   A={}
   setOfSize[k]=[]
   for i in range(1,n):
    A[i]=[]
    if k==0:
     ba = bitarray(n)
     ba.setall(0)
     ba[0]=1
     ba[i]=1
     A[i]= [ba]
     setOfSize[k].append(ba)
    else:
     if k>i:
      A[i]=[]
     else:
      for j in range(1,i):
       for l in previous[j]:
        s1=l[:]
        s1[i]=1
        A[i].append(s1)
        setOfSize[k].append(s1)
   print setOfSize[k]
   previous = A.copy()
 #print len(setOfSize[m-1])
 return setOfSize

arrayOfSetsOf(5,5)
