from sys import stdin

def main():
    number = int(stdin.readline())
    while (number > 0):
        if(number < 101):
            print("f91("+str(number)+") = 91")
        else:
            print("f91("+str(number)+") = "+str(number-10))
        number = int(stdin.readline())
main()
