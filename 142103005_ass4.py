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
    return x[2]
def UniformCostSearch(Startx , Starty , Goalx , Goaly , grid) :
    OpenList = []
    ClosedList = []
    OpenList.append([Startx,Starty,0])


    while(len(OpenList)!=0):

        OpenList.sort(key=Cost)
        print("OpenList : ",OpenList)
        element = OpenList.pop(0)
        x = element[0]
        y = element[1]
        c = element[2]

        if (grid[x][y] != 0):
            print("Marked")
            print("*************************************")
            continue

        grid[x][y] = 2

        print("Node  = ",x,",",y)

        ClosedList.append([x,y])
        print("ClosedList : ",ClosedList)

        if(x==Goalx and y==Goaly):
            print("The GoalTest is True")
            break
        else:
            print("The GoalTest is False")

            print("The Successors are: ")

        if(x-1>=0 and grid[x-1][y]==0 and OpenList.count([x-1,y,c+1])==0):
            OpenList.append([x-1,y,c+1])
            print(x-1,y,c+1)
        if(y+1<=9 and grid[x][y+1]==0 and OpenList.count([x,y+1,c+1])==0):
            OpenList.append([x,y+1,c+1])
            print(x,y+1,c+1)        
        if(x+1<=9 and grid[x+1][y]==0 and OpenList.count([x+1,y,c+1])==0):
            OpenList.append([x+1,y,c+1])
            print(x+1,y,c+1)      
        if(y-1>=0 and grid[x][y-1]==0 and OpenList.count([x,y-1,c+1])==0):
            OpenList.append([x,y-1,c+1])
            print(x,y-1,c+1)

        print("****************************************")

UniformCostSearch(0,0,1,3,grid)