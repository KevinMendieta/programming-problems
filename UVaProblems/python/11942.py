from sys import stdin

def isSorted(numbers):
    ascendent, descendent = True,True
    i = 0
    while(i<len(numbers)-1 and (ascendent or descendent)):
        if(numbers[i] > numbers[i+1]):
            ascendent = False
        if(numbers[i] < numbers[i+1]):
            descendent = False
        i += 1
    return (ascendent, descendent)

def main():
    cases = int(stdin.readline())
    print("Lumberjacks:")
    while (cases > 0):
        numbers = [int(x) for x in stdin.readline().split()]
        sort = isSorted(numbers)
        if(sort[0] or sort[1]):
            print("Ordered")
        else:
            print("Unordered")
        cases -= 1
main()
