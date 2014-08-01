from bitarray import bitarray
def arrayOfSetsOf(n,m):
 A={}
 nop = range(0,n)
 allSets=[]
 ba = bitarray(n)
 ba.setall(0)
 print nop
 for i in range(0,n):
   A[i]={}
   for k in range(0,m):
    print str(i) + ","+str(k)
    A[i][k]=[]
    if k==0:
     ba = bitarray(n)
     ba.setall(0)
     ba[i]=1
     A[i][k]= [ba]
     print A[i][k]
    else:
     if k>i:
      A[i][k]=[]
     else:
      for j in range(0,i):
       #print A[j][k-1]
       for l in A[j][k-1]:
       # print "l=" +str(l)
        s1=l[:]
        s1[i]=1
       # print "s1="+str(s1)
        #toIns.append(nop[i])
        A[i][k].append(s1)
        if k ==m-1:
         allSets.append(s1)
 print len(allSets)
 print allSets
 #print allSets
 return allSets

arrayOfSetsOf(5,2)

