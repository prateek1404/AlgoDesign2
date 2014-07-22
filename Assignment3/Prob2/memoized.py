import sys
import json


def main():
    input_file = open("knapsack1.txt")
    #input_file = open("testcase3.txt")
    lines = input_file.readlines()
    knapsackSize,noItems= lines.pop(0).replace("\n","").split(" ")
    knapsackSize = int(knapsackSize)
    noItems = int(noItems)
    itemArray=[]
    for line in lines:
     value,weight = line.replace("\n","").split(" ")
     value1 = int(value)
     weight1 = int(weight)
     itemArray.append({'value':value1,'weight':weight1})
    solution= []
    includedArray = []
    for y in range(0,knapsackSize+1):
     solution.append([])
     for z in range(0,noItems):
      solution[y].append(0)
    for x in range(0,knapsackSize+1):
     for k in range(0,noItems): 
      if x==0:
       solution[x][k]= 0
      else:
       if int(itemArray[k]['weight']) > x:
        solution[x][k] = solution[x][k-1]
       else:
        smallNSsize = x -int(itemArray[k]['weight'])
        currentElVal = int(itemArray[k]['value'])
        if k==0:
         larger= currentElVal
        else:
         larger= max(int(solution[x][k-1]),currentElVal + solution[smallNSsize][k-1])
        solution[x][k]= larger
    print solution[knapsackSize][noItems-1]    
if __name__ == '__main__':
    main()

