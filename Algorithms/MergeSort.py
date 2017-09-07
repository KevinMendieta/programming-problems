from sys import stdin
"""Try of an implementation of Merge Sort sorting algorithm """


def main():
    n = int(stdin.readline())
    while n != 0:
        array = []
        for i in range(n):
            array.append(int(stdin.readline()))
        print(sort(array))
        n = int(stdin.readline())


def sort(array):
    if len(array) < 2:
        return array
    else:
        return merge(sort(array[:len(array) // 2]), sort(array[len(array) // 2:]))


def merge(first, second):
    i = 0
    j = 0
    new = []
    while i < len(first) and j < len(second):
        if first[i] < second[j]:
            new.append(first[i])
            i += 1
        elif first[i] > second[j]:
            new.append(second[j])
            j += 1
        else:
            new.append(first[i])
            new.append(second[j])
            i += 1
            j += 1
    if i == len(first):
        new.extend(second[j:])
    else:
        new.extend(first[i:])
    return new


main()
