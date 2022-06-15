from sys import stdin


def alt_subarray_recurrent(array, T, x):
  if x == T - 1:
    return 1
  if (array[x] < 0 and array[x + 1] > 0) or (array[x] > 0 and array[x + 1] < 0):
    return 1 + alt_subarray_recurrent(array, T, x + 1)
  else:
    return 1


def alt_subarray_iterative(T, array):
  memory = [0] * T
  for i in range(T - 1, -1, -1):
    if i + 1 < T:
      if (array[i] < 0 and array[i + 1] > 0) or (array[i] > 0 and array[i + 1] < 0):
        memory[i] = 1 + memory[i + 1]
      else:
        memory[i] = 1
    else:
      memory[i] = 1
  return memory


def solve(T, array):
  alt_subarray = alt_subarray_iterative(T, array)

  string = ''
  for i in range(T):
    if i + 1 < T:
      string += str(alt_subarray[i]) + ' '
    else:
      string += str(alt_subarray[i])
  return string


def main():
  cases = int(stdin.readline().strip())
  for _ in range(cases):
    T = int(stdin.readline().strip())
    array = [int(x) for x in stdin.readline().strip().split()]
    print(solve(T, array))


main()
