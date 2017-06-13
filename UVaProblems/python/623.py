from sys import stdin

factorials=[1,1]

def factorial(n):
    global factorials
    for i in range(len(factorials),n+1):
        factorials.append(factorials[i-1]*i)

def main():
    global factorials
    factorial(1000)
    number = stdin.readline().strip()
    while (len(number)!=0):
        number = int(number)
        print(str(number)+"!")
        if(number>len(factorials)):
            factorial(number)            
            print(factorials[number])
        else:
            print(factorials[number])
        number = stdin.readline().strip()
main()
    
