from sys import stdin

def main():
    cases = int(stdin.readline())
    while cases != 0:
        numbers = [int(x) for x in stdin.readline().split()]
        if numbers[0] > numbers[1] :
            print('>')
        elif numbers[0] < numbers[1]:
            print('<')
        else:
            print('=')
        cases -= 1
main()
    
