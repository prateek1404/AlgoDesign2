from bitarray import bitarray
def arrayOfSetsOf(n,m):
 A={}
 allSets=[]
 setOfSize={}
 previous = {}
 for k in range(0,m):
   print "processing for "+str(k)
   A={}
   setOfSize[k]=[]
   for i in range(1,n):
    print "value of i is "+str(i)
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
      print "nothing"
     else:
      #for j in range(1,i):
      for l in previous:
       temp = []
       #for l in previous:
       for j in range(1,i):
        print "l from previous "+str(l)
        s1=l[:]
        s1[j]=1
        print "inserting "+str(s1)
        A[i].append(s1)
        setOfSize[k].append(s1)
   #print setOfSize[k] 
   previous = setOfSize[k][:]
   print previous
 #print setOfSize[m-1]
 #print len(setOfSize[m-1])
 return setOfSize

arrayOfSetsOf(5,5)
