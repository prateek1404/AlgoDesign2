import sys
import json


def main():
    input_file = open("jobs.txt")
    lines = input_file.readlines()
    jobcount= lines.pop(0)
    jobArray=[]
    for line in lines:
     weight,length = line.replace("\n","").split(" ")
     #print "weight= "+str(weight)
     #print "length= "+str(length) 
     greedyKey = int(weight)-int(length)
     k=0
     jobVal = {'greedyKey':int(greedyKey),'weight':int(weight),'length':int(length)}
     if(len(jobArray)==0):
      jobArray.append(jobVal)
     else:
      while(k< len(jobArray) and greedyKey<=int(jobArray[k]['greedyKey'])):
       if(greedyKey==int(jobArray[k]['greedyKey'])):
        if(int(weight)>jobArray[k]['weight']):
         break;
       k = k+1
      jobArray.insert(k,jobVal)
    clock =0;
    wsc =0
    for job in jobArray:
     clock = clock+job['length']
     wsc = wsc +(clock*job['weight'])
    print "WSC = "+str(wsc) 
     
if __name__ == '__main__':
    main()

