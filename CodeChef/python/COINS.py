from sys import stdin


MEMO = dict()
MEMO[0] = 0
MEMO[1] = 1


def exchange_recursive(coin_value):
  if coin_value == 0:
    return 0
  if coin_value == 1:
    return 1
  return  max(
    coin_value,
    exchange_recursive(coin_value // 2) + exchange_recursive(coin_value // 3) + exchange_recursive(coin_value // 4)
  )


# slower since the input could be 10^9, so in that case we'll compute 10^9 values
def exchange_iterative(coin_value):
  global MEMO
  if coin_value in MEMO:
    return MEMO[coin_value]
  for i in range(2, coin_value + 1):
    MEMO[i] = max(
      coin_value,
      MEMO[i // 2] + MEMO[i // 3] + MEMO[i // 4]
    )
  return MEMO[coin_value]


# faster since we don't compute all the 10^9 values
def exchange_memorized(coin_value):
  global MEMO
  if coin_value in MEMO:
    return MEMO[coin_value]
  MEMO[coin_value] = max(
    coin_value,
    exchange_memorized(coin_value // 2) + exchange_memorized(coin_value // 3) + exchange_memorized(coin_value // 4)
  )
  return MEMO[coin_value]


def main():
  line = stdin.readline().strip()
  while line != "":
    coin_value = int(line)
    print(exchange_memorized(coin_value))
    line = stdin.readline().strip()


main()
# exchange_iterative(1000000000)
# exchange_memorized(1000000)
