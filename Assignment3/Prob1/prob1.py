import sys
import json


def main():
    input_file = open("knapsack1.txt")
    lines = input_file.readlines()
    knapsackSize,noItems= lines.pop(0).replace("\n","").split(" ")
    knapsackSize = int(knapsackSize)
    noItems = int(noItems)
    itemArray=[]
    for line in lines:
     value,weight = line.replace("\n","").split(" ")
     value = int(value)
     weight = int(weight)
     itemArray.append({'value':value,'weight':weight})
    solution= []
    for y in range(0,knapsackSize+1):
     solution.append([])
     for z in range(0,noItems):
      solution[y].append(0)
   # print itemArray
    print len(solution[0])
    for x in range(0,knapsackSize+1):
     for k in range(0,noItems): 
      print "snapsack size"+str(x)+" k ="+str(k)    
      if int(itemArray[k]['weight'])<int(x):
       solution[x][k]= 0
      else:
       solution[x][k]= max(int(solution[x][k-1]),int(itemArray[k]['value'])+int(solution[int(x-itemArray[k]['weight'])][k-1]))
    print solution[knapsackSize][noItems-1]    
if __name__ == '__main__':
    main()

