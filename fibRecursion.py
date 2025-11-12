print(0)
print(1)
count = 2

def fibbi(prev1, prev2):
  global count
  if count <= 20:
    newFibbi = prev1 + prev2
    print(newFibbi)
    prev2 = prev1
    prev1 = newFibbi
    count += 1
    fibbi(prev1, prev2)
  else:
    return
  
fibbi(1, 0)