import math
from math import sqrt
#142103005 DIV2
#Pallavi Gaikwad

grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 1, 1, 1, 1, 0],
        [0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 1, 1, 1, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 1, 0, 1, 1, 1, 1, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


def Cost(x):
    return x[2]+x[3]


def Manhattan(Ax,Ay,Bx,By):
    return abs(Ax-Bx)+abs(Ay-By)

def Euclidian(Ax,Ay,Bx,By):
    return math.sqrt((Ax-Bx)**2 + (Ay-By)**2)


def BestFirstManhattan(Startx , Starty , Goalx , Goaly , grid) :
    OpenList = []
    ClosedList = []
    OpenList.append([Startx,Starty,0,Manhattan(Startx,Starty,Goalx,Goaly)])


    while(len(OpenList)!=0):

        OpenList.sort(key=Cost)
        print("OpenList : ",OpenList)

        element = OpenList.pop(0)
        x = element[0]
        y = element[1]
        c = element[2]
        
        if(grid[x][y]!=0):
            print("Marked")
            print("**************************************")
            continue

        grid[x][y] = 2 # mark as visited

        print("Node  = ",x,",",y)

        ClosedList.append([x,y])
        print("ClosedList : ",ClosedList)

        if(x==Goalx and y==Goaly):
            print("Goal Test is True")
            break
        else:
            print("Goal Test is False")


        print("The Successors are : ")

        if(x-1>=0 and grid[x-1][y]==0 and OpenList.count([x-1,y,c+1,Manhattan(x-1,y,Goalx,Goaly)])==0):
            OpenList.append([x-1,y,c+1,Manhattan(x-1,y,Goalx,Goaly)])
            print(x-1,y,c+1,Manhattan(x-1,y,Goalx,Goaly))

        if(y+1<=9 and grid[x][y+1]==0 and OpenList.count([x,y+1,c+1,Manhattan(x,y+1,Goalx,Goaly)])==0):
            OpenList.append([x,y+1,c+1,Manhattan(x,y+1,Goalx,Goaly)])
            print(x,y+1,c+1,Manhattan(x,y+1,Goalx,Goaly))
        
        if(x+1<=9 and grid[x+1][y]==0 and OpenList.count([x+1,y,c+1,Manhattan(x+1,y,Goalx,Goaly)])==0):
            OpenList.append([x+1,y,c+1,Manhattan(x+1,y,Goalx,Goaly)])
            print(x+1,y,c+1,Manhattan(x+1,y,Goalx,Goaly))
        
        if(y-1>=0 and grid[x][y-1]==0 and OpenList.count([x,y-1,c+1,Manhattan(x,y-1,Goalx,Goaly)])==0):
            OpenList.append([x,y-1,c+1,Manhattan(x,y-1,Goalx,Goaly)])
            print(x,y-1,c+1,Manhattan(x,y-1,Goalx,Goaly))        

        print("*********************************")



def BestFirstEuclidian(Startx , Starty , Goalx , Goaly , grid) :
    OpenList = []
    ClosedList = []
    OpenList.append([Startx,Starty,0,Euclidian(Startx,Starty,Goalx,Goaly)])


    while(len(OpenList)!=0):

        OpenList.sort(key=Cost)
        print("OpenList : ",OpenList)

        element = OpenList.pop(0)
        x = element[0]
        y = element[1]
        c = element[2]
        
        if(grid[x][y]!=0):
            print("Marked")
            print("************************************")
            continue

        grid[x][y] = 2 # mark as visited

        print("Node  = ",x,",",y)

        ClosedList.append([x,y])
        print("ClosedList : ",ClosedList)

        if(x==Goalx and y==Goaly):
            print("Goal Test is True")
            break
        else:
            print("Goal Test is False")


        print("The Successors are: ")

        if(x-1>=0 and grid[x-1][y]==0 and OpenList.count([x-1,y,c+1,Euclidian(x-1,y,Goalx,Goaly)])==0):
            OpenList.append([x-1,y,c+1,Euclidian(x-1,y,Goalx,Goaly)])
            print(x-1,y,c+1,Euclidian(x-1,y,Goalx,Goaly))

        if(y+1<=9 and grid[x][y+1]==0 and OpenList.count([x,y+1,c+1,Euclidian(x,y+1,Goalx,Goaly)])==0):
            OpenList.append([x,y+1,c+1,Euclidian(x,y+1,Goalx,Goaly)])
            print(x,y+1,c+1,Euclidian(x,y+1,Goalx,Goaly))
        
        if(x+1<=9 and grid[x+1][y]==0 and OpenList.count([x+1,y,c+1,Euclidian(x+1,y,Goalx,Goaly)])==0):
            OpenList.append([x+1,y,c+1,Euclidian(x+1,y,Goalx,Goaly)])
            print(x+1,y,c+1,Euclidian(x+1,y,Goalx,Goaly))
        
        if(y-1>=0 and grid[x][y-1]==0 and OpenList.count([x,y-1,c+1,Euclidian(x,y-1,Goalx,Goaly)])==0):
            OpenList.append([x,y-1,c+1,Euclidian(x,y-1,Goalx,Goaly)])
            print(x,y-1,c+1,Euclidian(x,y-1,Goalx,Goaly))
        
        

        print("******************************************")


# BestFirstManhattan(0,0,1,3,grid)

BestFirstEuclidian(0,0,1,3,grid)