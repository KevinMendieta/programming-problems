from sys import stdin
MAX = 100000
cont = 0
def merge(A, low, mid, hi):
  global T,cont
  for i in range(low, hi): T[i] = A[i]
  l, r = low,mid
  for i in range(low, hi):
    if l<mid and r<hi:
      if T[l]<=T[r]:
        cont+=1
        A[i],l = T[l],l+1
      else:
        cont+=1
        A[i],r = T[r],r+1
    elif l==mid:
      A[i],r = T[r],r+1
    else:
      A[i],l = T[l],l+1

def merge_sort(A, low, hi):
  global T,cont
  T = [ None for i in range(MAX) ]
  cont = 0
  if low+1<hi:
    mid = low+((hi-low)//2)
    merge_sort(A, low, mid)
    merge_sort(A, mid, hi)
    merge(A, low, mid, hi)
  return(cont)
                
def main():
    numbers = [int(x) for x in stdin.readline().split()]
    while numbers[0] > 0:
        merge_sort(numbers,0,len(numbers))
        if cont%2 == 0:
            print("Carlos")
        else:
            print("Marcelo")
        numbers = [int(x) for x in stdin.readline().split()]
main()
