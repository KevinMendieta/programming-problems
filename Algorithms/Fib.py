NUMBERS = [None for x in range(1000)]
NUMBERS[0] = 0
NUMBERS[1] = 1
NUMBERS[2] = 1

def fib(n):
  global NUMBERS

  if (NUMBERS[n]):
    return NUMBERS[n]
  NUMBERS[n] = fib(n-1) + fib(n-2)
  return NUMBERS[n]

def fib_cycle(n):
  if (NUMBERS[n]):
    return NUMBERS[n]
  for i in range(3, n + 1):
    NUMBERS[i] = NUMBERS[i-1] + NUMBERS[i-2]

  return NUMBERS[n]
