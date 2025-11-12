prev2 = 0
prev1 = 1

print(prev2)
print(prev1)
for fib in range(10):
  newFib = prev1 + prev2
  print(newFib)
  prev2 = prev1
  prev1 = newFib