from sys import stdin

def kaprekar(a):
    flag = False
    for i in range(len(str(a))*2):
        if (((a*a%(10**(i+1)))+(a*a//(10**(i+1))))==a)and(a*a%(10**(i+1)))>0 and (a*a//(10**(i+1)))>0:
            flag = True
    return flag

def main():
    cases = int(stdin.readline())
    prec = []
    for i in range(40001):
        prec.append(kaprekar(i))
    for i in range(cases):
        info = [int(x) for x in stdin.readline().split()]
        ans = []		
        for j in range(info[0],info[-1]+1):
            if (prec[j]):
                ans.append(j)
        print("case #"+str(i+1))
        if len(ans)>0:
            for j in ans:
                print(j)
        else:
            print("no kaprekar numbers")
        if(i<cases):
            print()
main()
