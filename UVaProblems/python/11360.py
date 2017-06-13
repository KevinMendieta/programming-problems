from sys import stdin

def row(mat,a,b):
    rowA = mat[a-1]
    rowB = mat[b-1]
    newMat = []
    for i in range(len(mat)):
        if(i+1==a):
            newMat.append(rowB)
        elif(i+1==b):
            newMat.append(rowA)
        else:
            newMat.append(mat[i])
    return newMat    

def col(mat,a,b):
    colA = []
    colB = []
    for i in range(len(mat)):
        colA.append(mat[i][a-1])
        colB.append(mat[i][b-1])
    for i in range(len(mat)):
        for j in range(len(mat)):
            if (i+1==a):
                mat[j][i] = colB[j]
            elif(i+1==b):
                mat[j][i] = colA[j]
    return mat
 
def inc(mat):
    for i in range(len(mat)):
        for j in range(len(mat)):
            mat[i][j] = (int(mat[i][j])+1)%10
    return mat

def dec(mat):
    for i in range(len(mat)):
        for j in range(len(mat)):
            mat[i][j] = (int(mat[i][j])-1)%10
    return mat

def transpose(mat):
    newMat = []
    for i in range(len(mat)):
        tmp = []
        for j in range(len(mat)):
            tmp.append(mat[j][i])
        newMat.append(tmp)
    return newMat

def main():
    for cases in range(int(stdin.readline())):
        mat = []
        for i in range(int(stdin.readline())):
            mat.append(list(stdin.readline()))
        for i in range(int(stdin.readline())):
            instruction = stdin.readline().split()
            if (instruction[0]=="row"):
                mat = row(mat,int(instruction[1]),int(instruction[2]))
            elif(instruction[0]=="col"):
                mat = col(mat,int(instruction[1]),int(instruction[2]))
            elif(instruction[0]=="inc"):
                mat = inc(mat)
            elif(instruction[0]=="dec"):
                mat = dec(mat)
            elif(instruction[0]=="transpose"):
                mat = transpose(mat)
        print("Case #"+str(cases+1))
        for i in range(len(mat)):
            for j in range(len(mat)):
                print(mat[i][j],end="")
            print()
        print()
main()
