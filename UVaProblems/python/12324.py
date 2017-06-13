from sys import stdin
from heapq import *

def solve(info):
    heap = []
    total = 0
    total += info[0][0]
    heappush(heap,info[-1][0]*-1)
    for i in range(len(info)-2,-1,-1):
        if i==0:
            powers = info[0][1]
            while(len(heap)!=0 and powers>0):
                total -= heappop(heap)>>1
                powers -= 1
        else:
            powers = info[i][1]
            if powers>0:                
                while(len(heap)!=0 and powers>0):
                    total -= heappop(heap)>>1
                    powers-=1
            heappush(heap,info[i][0]*-1)
    while(len(heap)!=0):
        total -= heappop(heap)
    return (total)
    
def main():
    cases = int(stdin.readline())
    while cases != 0:
        info = []
        for i in range(cases):
            info.append([int(x) for x in stdin.readline().split()])
        if(len(info)>1):
            print(solve(info))
        else:
            print(info[0][0])
        cases = int(stdin.readline())
main()
