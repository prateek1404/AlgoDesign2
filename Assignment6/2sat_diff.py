import sys
import math
import random
from bitarray import bitarray


def createConstraints(graphfile):
    input_file = open(graphfile)
    lines = input_file.readlines()
    ncount= lines.pop(0).replace("\n","")
    ncount = int(ncount)
    constraints=[]
    
    for line in lines:
     variables = line.replace("\n","").split(" ")
     constraints.append(variables)
    return ncount,constraints


def generateRandomBitArray(doneHash,ncount):
    ar = bitarray(ncount)
    for i in range(0,ncount):
     ar[i]=random.randint(0,1)
    strar= ar.to01()
    if strar not in doneHash:
     doneHash[strar]=1
     return ar,doneHash 
    else:
     return generateRandomBitArray(doneHash,ncount),doneHash

 
print "main function"
ncount,constraints  = createConstraints(sys.argv[1])
conSat = []
doneHash={}
sucArray = bitarray(ncount)
for i in range(0,ncount):
 conSat.append(0)
print "done creating constraints"
print len(constraints)
print len(conSat)
log = int(math.log(ncount,2))+1
inner = 2*(ncount**2)
print log    
print inner
done=0
for i in range(0,log):
 if done==1:
  break
 valuebitArray,doneHash = generateRandomBitArray(doneHash,ncount)
 #print valuebitArray
 for j in range(0,ncount):
  if done==1:
   break
  satisfied =0
  failed=[]
  sucArray=[]
  for k in range(0,ncount):
   #print satisfied 
   cons = constraints[k]
   firstvar = int(cons[0])
   secondvar = int(cons[1])
   if firstvar<0:
    valinArray1 = ~valuebitArray[firstvar*(-1)-1]
   else:
       valinArray1 = valuebitArray[firstvar-1]
   
   if secondvar<0:
     valinArray2 = ~valuebitArray[secondvar*(-1)-1]
   else:
     valinArray2 = valuebitArray[secondvar-1]

   if valinArray1|valinArray2:
        #sucArray[k]=1
        sucArray.append(cons)
        satisfied = satisfied+1
   else:
        failed.append(cons)
        whichVar = cons[random.randint(0,1)]
        whichVar = int(whichVar)
        if whichVar<0:
          valuebitArray[whichVar*(-1)-1]= ~valuebitArray[whichVar*(-1)-1]
        else:
          valuebitArray[whichVar-1]= ~valuebitArray[whichVar-1]
        satisfied=0
        failed=[]
        sucArray=[]
        break
  print "satisfied= "+str(len(sucArray))
  print "failed ="+str(len(failed))
  if len(sucArray)== ncount:
   done=1
   break

print "hello"
print satisfied
