import math
from functools import cmp_to_key

#142103005
#Pallavi Gaikwad
#DIV2

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

def successor_Node(node):
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
def Astar_manhattenDist(graph,start,goal,OL,CL):
    OL=set([start])
    CL=set([])
    g={}
    g[start]=0
    parents={}
    parents[start]=start
    while(len(OL)!=0):
        print("The OpenList:",OL)
        print("The ClosedList: ",CL)
        n=None
        for v in OL:
            if(n==None or g[v]+manhattenDist(start,v)<g[n]+manhattenDist(start,n)):
                n=v
        if(n==None):
            print("Path Unavailable!")
            return None  
        if n==goal:
            path=[]
            while(parents[n]!=n):
                path.append(n)
                n=parents[n]
            path.append(start)
            path.reverse()
            return path
        else:
            print("Present Node: ",n)
            print("GoalTest: Goal Not Reached! False")
            print("Successors of Present Node: ",successor_Node(n))
            for i,val in graph[n][0]:
                if(i not in OL and i not in CL):
                    OL.add(i)
                    parents[i]=n
                    g[i]=g[n]+val   
                else:
                    if(g[i]>g[n]+val):
                        g[i]=g[n]+val
                        parents[i]=n
                        if i in CL:
                            CL.remove(i)
                            OL.add(i)
            OL.remove(n)
            CL.add(n)
            print()
    return []
def Astar_eucledianDist(graph,start,goal,OL,CL):
    OL=set([start])
    CL=set([])
    g={}
    g[start]=0
    parents={}
    parents[start]=start
    while(len(OL)!=0):
        print("The OpenList:",OL)
        print("The ClosedList: ",CL)
        
        n=None
        for v in OL:
            if(n==None or g[v]+eucledianDist(start,v)<g[n]+eucledianDist(start,n)):
                n=v
        if(n==None):
            print("Path Unavailable!")
            return None  
        if n==goal:
            path=[]
            while(parents[n]!=n):
                path.append(n)
                n=parents[n]
            path.append(start)
            path.reverse()
            return path
        else:
            print("Present Node: ",n)
            print("GoalTest: Goal not Reached!False")
            print("Successor of Present Node: ",successor_Node(n))
            for i,val in graph[n][0]:
                if(i not in OL and i not in CL):
                    OL.add(i)
                    parents[i]=n
                    g[i]=g[n]+val   
                else:
                    if(g[i]>g[n]+val):
                        g[i]=g[n]+val
                        parents[i]=n
                        if i in CL:
                            CL.remove(i)
                            OL.add(i)
            OL.remove(n)
            CL.add(n)
            print()
    return []

def printstatement():
 try:
    start='X'
    goal='K' 
    heuristic="m"
    arr=[]
   
    print("Start: ",start)
    print("Goal: ",goal)
    if(heuristic=="m"):
         print("Heuristic: Manhattan Distance")
         print()
         arr=Astar_manhattenDist(graph,start,goal,[],[])
    elif(heuristic=="e"):
         print("Heuristic: eucledianDist Distance")
         print()
         arr=Astar_eucledianDist(graph,start,goal,[],[]) 

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
    