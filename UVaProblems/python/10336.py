from sys import stdin
def fillDown(world,source,char):
    stack = []
    stack.append(source)
    while stack:
        node = stack.pop()        
        if node[0]+1 < len(world) and world[node[0]+1][node[1]] == char:
            stack.append((node[0]+1,node[1]))            
        if node[0]-1 < len(world) and world[node[0]-1][node[1]] == char:
            stack.append((node[0]-1,node[1])) 
        if node[1]+1 < len(world[0]) and world[node[0]][node[1]+1] == char:
            stack.append((node[0],node[1]+1))
        if node[1]-1 > 0 and world[node[0]][node[1]-1] == char:
            stack.append((node[0],node[1]-1))
        world[node[0]][node[1]] = 1
    return (world)
def solve(world,case):
    order = []
    apparitions = {}
    for i in range(len(world)):
        for j in range(len(world[0])):
            if world[i][j] not in apparitions and world[i][j]!=1:
                apparitions[world[i][j]] = 1
                world=fillDown(world,(i,j),world[i][j])            
            elif world[i][j]!=1:
                apparitions[world[i][j]] += 1
                world=fillDown(world,(i,j),world[i][j])
    
    for k in apparitions:
        order.append((apparitions[k],k))
    order.sort()
    print("World #"+str(case))
    for i in order:
        print(i[1]+": "+str(i[0]))
def main():
    cases = int(stdin.readline())
    for i in range(cases):
        dimensions = [int(x) for x in stdin.readline().split()]
        world = []
        for j in range(dimensions[0]):
            world.append(list(stdin.readline().strip()))
        solve(world,i+1)
main()
