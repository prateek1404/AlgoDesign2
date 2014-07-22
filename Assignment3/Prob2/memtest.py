import sys
import json
import sys
sys.setrecursionlimit(300000)
valueArray=[]
weightArray=[]
solDict= {}
def knapsack(size,k):
    if size in solDict:
     if k in solDict[size]:
      print "solution of subproblem with size="+str(size)+" k="+str(k)
      return solDict[size][k]
     
    if k == 0:
     if weightArray[k]>size:
      if size not in solDict:
       solDict[size] = {}
       solDict[size][k]=0
      else:
       solDict[size][k]=0
      return 0;
     else: 
      if size not in solDict:
       solDict[size] = {}
       solDict[size][k]=valueArray[k]
      else:
       solDict[size][k]=valueArray[k]
      return valueArray[k]
    else: 
     if weightArray[k]>size:
      sol = knapsack(size,k-1)
      if size not in solDict:
       solDict[size] = {}
       solDict[size][k]=sol
      else:
       solDict[size][k]=sol
      return sol   
     else:
      val1 = knapsack(size,k-1)
      newNSsize = size-weightArray[k]
      val2 = valueArray[k]+knapsack(newNSsize,k-1)
      if size not in solDict:
        solDict[size] = {}
        solDict[size][k]=max(val1,val2)
      else:
        solDict[size][k]=max(val1,val2)
      return max(val1,val2)
    
def main():
    input_file = open("knapsack_big.txt")
    #input_file = open("testcase3.txt")
    lines = input_file.readlines()
    knapsackSize,noItems= lines.pop(0).replace("\n","").split(" ")
    knapsackSize = int(knapsackSize)
    noItems = int(noItems)
    for line in lines:
     value,weight = line.replace("\n","").split(" ")
     value1 = int(value)
     weight1 = int(weight)
     valueArray.append(value1)
     weightArray.append(weight1)
    print knapsack(knapsackSize,noItems-1)

if __name__ == '__main__':
    main()

