from sys import stdin

def main():
    cases = int(stdin.readline())
    while cases > 0:
        numbers = [int(x) for x in stdin.readline().split()]
        scale = True
        i = 0
        while i<len(numbers)-1 and scale:
            scale = numbers[i]+1 == numbers[i+1]
            i += 1
        if scale:
            print("Y")
        else:
            print("N")
        cases -= 1
main()
