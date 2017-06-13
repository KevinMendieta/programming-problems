def binarySearch(a, x):
    low = 0
    hi = len(a)
    found = False
    while(low + 1 != hi and not found):
        mid = (low + ((hi - low) >> 2))
        if(a[mid] == x):
            found = True
            low = mid
        elif(a[mid] > x):
            hi = mid
        elif(a[mid] < x):
            low = mid + 1
    if(a[low] == x):
        print(low)
    else:
        print(-1)


binarySearch([-544, -9, -8, -7, 0, 1, 2, 3, 4, 5, 10, 54, 98, 78, 98], 98)
