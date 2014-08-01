from bitarray import bitarray
def arrayOfSetsOf(n,m):
 A={}
 allSets=[]
 setOfSize={}
 for k in range(0,m):
   print "processing for "+str(k)
   A[k]={}
   setOfSize[k]=[]
   for i in range(1,n):
    A[k][i]=[]
    if k==0:
     ba = bitarray(n)
     ba.setall(0)
     ba[0]=1
     ba[i]=1
     A[k][i]= [ba]
     setOfSize[k].append(ba)
    else:
     if k>i:
      A[k][i]=[]
     else:
      for j in range(1,i):
       for l in A[k-1][j]:
        s1=l[:]
        s1[i]=1
        A[k][i].append(s1)
        setOfSize[k].append(s1)
   print setOfSize[k]
 #print len(setOfSize[m-1])
 return setOfSize

arrayOfSetsOf(5,5)
