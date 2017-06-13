from sys import stdin

def solve (numbers,source):    
    if numbers[0] > source[0] and numbers[1] > source[1]:
        print("NE")
    elif numbers[0] < source[0] and numbers[1] < source[1]:
        print("SO")
    elif numbers[0] < source[0] and numbers[1] > source[1]:
        print("NO")
    elif numbers[0] > source[0] and numbers[1] < source[1]:
        print("SE")
    else:
        print("divisa")
def main():
    cases = int(stdin.readline())
    while cases > 0:
        source = [int(x) for x in stdin.readline().split()]
        while cases > 0:
            numbers = [int(x) for x in stdin.readline().split()]
            solve(numbers,source)
            cases -=1           
        cases = int(stdin.readline())                
main()
