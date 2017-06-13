from sys import stdin

def main():
    numbers = [int(x) for x in stdin.readline().split()]
    while(numbers):
        jolly = True;i = 1
        while (i<numbers[0] and jolly):
            jolly = 0<abs(numbers[i]-numbers[i+1])<numbers[0] and numbers[i]<numbers[0] and numbers[i+1]<numbers[0]
            i+=1
        if(jolly):
            print("Jolly")
        else:
            print("Not jolly")
        numbers = [int(x) for x in stdin.readline().split()]
main()
