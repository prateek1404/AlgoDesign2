import sys
import json


def main():
    input_file = open("testcase1.txt")
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
    for y in range(0,knapsackSize+1):
     solution.append([])
     for z in range(0,noItems):
      solution[y].append(0)
   # print itemArray
    print len(solution[0])
    for x in range(0,knapsackSize+1):
     for k in range(0,noItems): 
      if x==0:
       solution[x][k]= 0
       print "solution for x="+str(x)+" k="+str(k)+" is 0"
      else:
      # print itemArray[k]
       print "value of x is "+str(x)
       print "value of itemArray[k]['weight'] is "+str(itemArray[k]['weight'])
       if int(itemArray[k]['weight']) > x:
       # print "inside less than knapsack block"
        solution[x][k] = solution[x][k-1]
       else:
       # print "inside greater than knapsack block"
        larger= max(int(solution[x][k-1]),int(itemArray[k]['value'])+int(solution[int(x-itemArray[k]['weight'])][k-1]))
        solution[x][k]= larger
       print "solution for x="+str(x)+" k="+str(k)+" is "+str(solution[x][k])
    print solution[knapsackSize][noItems-1]    
if __name__ == '__main__':
    main()

