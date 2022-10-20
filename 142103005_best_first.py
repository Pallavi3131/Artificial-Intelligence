import math
from functools import cmp_to_key

#142103005
#Pallavi Gaikwad
#Div2

graph={
    'X':[[('Y',3),('Z',2)],(0,0)],
       'Y':[[('M',4),('D',1)],(7,6)],
       'Z':[[('O',3),('R',1)],(1,3)],
       'O':[[('P',5)],(6,2)],
       'R':[[('K',2),('Q',3)],(1,1)],
       'M':[[()],(4,3)],
       'D':[[()],(1,2)],
       'P':[[()],(2,2)],
       'K':[[()],(5,4)],
       'Q':[[()],(-1,1)]
}
start='X'
def manhattenDist(v,u):
    x1=graph[v][1][0]
    y1=graph[v][1][1]
    x2=graph[u][1][0]
    y2=graph[u][1][1]
    return abs(x2-x1)+abs(y2-y1)
def eucledianDist(v,u):
    x1=graph[v][1][0]
    y1=graph[v][1][1]
    x2=graph[u][1][0]
    y2=graph[u][1][1]
    sum=(x1-x2)*(x1-x2)+(y1-y2)*(y1-y2)
    return math.sqrt(sum)

def successor(node):
    arr=graph[node][0]
    temp=[]
    for key,val in arr:
        temp.append(key)
    return temp   
def Keys(path):
    temp=[]
    for i in path:
        temp.append(i[0])
    return temp         
        
def bestfs(graph,start,goal,OL,CL,heuristic):
    OL=[(start,0)]
    while(len(OL)!=0):
        print("OpenList: ",Keys(OL))
        OL.sort(key=lambda x:x[1])
        ele=OL.pop(0)
        
        node=ele[0]
        if(ele[0] not in CL):
            CL.append(ele[0])
        if(node==goal):
            print("GoalTest: Goal Reached!True")
            return CL
        else:
            print("Present Node:",node)
            print("GoalTest: Goal not Reached!False")
            print("Closed List:", CL)
            print("Successors of Present Node:",successor(node))
            
            for i in graph[node][0]:
                
                if(i[0] not in OL and i[0] not in CL):
                    if(heuristic=="m"):
                        
                         OL.append((i[0],manhattenDist(i[0],start)))
                    elif(heuristic=="n"):
                        OL.append((i[0],eucledianDist(i[0],start)))
                             
        print()        
                   

def printstatement():
 try:
    start='X'
    goal='K'
    heuristic="m"
    arr=bestfs(graph,start,goal,[],[],heuristic)
    print("Start: ",start)
    print("Goal: ",goal)
    if(heuristic=="m"):
         print("Heuristic: Manhattan Distance")
    elif(heuristic=="e"):
         print("Heuristic: eucledianDist Distance")    

    temp=[]
    for i in arr:
        temp.append(i[0])
    sum=0    
    for j in range(len(temp)-1):
        for k in graph[temp[j]][0]:
            if(k[0]==temp[j+1]):
                sum=sum+k[1]
    print(temp)
    print("Cost:",sum)   
 except:
     print("Path unacheivable!")            
                
printstatement()



