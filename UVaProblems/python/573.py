from sys import stdin

def main():
    info = [int(x) for x in stdin.readline().split()]
    while info[0] != 0:
        succes = False
        fail = False
        cont = 0
        total = 0
        factor = (info[3]/100)*info[1]
        while not(succes) and not(fail):
            if info[1] > 0:
                total += info[1]
            if total <= info[0]:
                total -= info[2]
            if total < 0:
                fail = True
            elif total > info[0]:
                succes = True                
            if info[1] > 0:
                info[1] -= factor
            cont += 1
        if succes:
            print("success on day",cont)
        else:
            print("failure on day",cont)
        info = [int(x) for x in stdin.readline().split()]
main()
