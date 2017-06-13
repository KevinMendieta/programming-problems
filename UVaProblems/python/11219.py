from sys import stdin

def main():
    cases = int(stdin.readline())
    stdin.readline()
    for i in range(cases):
        secondDate = [int(x) for x in stdin.readline().split("/")]#fecha actual
        firstDate = [int(x) for x in stdin.readline().split("/")]#fecha nacimiento
        stdin.readline()
        if(firstDate[1]>=secondDate[1] and firstDate[2]>secondDate[2]):
            print("Case #"+str(i+1)+": Invalid birth date")
        elif (secondDate[2]-firstDate[2]>130):
            print("Case #"+str(i+1)+": Check birth date")
        else:
            if(secondDate[1]<=firstDate[1]):
                if(secondDate[0]<firstDate[0]):
                     print("Case #"+str(i+1)+": "+str(secondDate[2]-firstDate[2]-1))
                else:
                    print("Case #"+str(i+1)+": "+str(secondDate[2]-firstDate[2]))
            else:
                print("Case #"+str(i+1)+": "+str(secondDate[2]-firstDate[2]))
main()
