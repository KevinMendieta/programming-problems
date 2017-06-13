from sys import stdin

primes = [False for x in range(100)]

def sumDigits(n):
    cont = 0
    while (n//10!=0):
        cont += n%10
        n //= 10
    return cont+n

def isPrime(n):
    cont = 0
    for i in range(1,(n//2)+1):
        if(n%i==0):
            cont += 1
    return cont == 2

def preCalculate():
    global primes
    for i in range(len(primes)):
        if(isPrime(i) and isPrime(sumDigits(i))):
            primes[i] = True
def main():
    global primes
    preCalculate()
    print("hola")
    cases = int(stdin.readline())
    while (cases > 0):
        ranges = [int(x) for x in stdin.readline().split()]
        cont = 0
        for i in range(ranges[0],ranges[1]+1):
            if(primes[i]):
                cont += 1
        print(cont)
        cases -= 1
main()
