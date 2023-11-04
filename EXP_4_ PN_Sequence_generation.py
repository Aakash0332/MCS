import numpy as np
print("The Polynomial is (example 1011):")
a = np.zeros((15, 4), dtype=int)

for j in range(4):
 a[0, j] = int(input())
for i in range(1, 15):
 for j in range(4):
  if j == 0:
   a[i, j] = a[i - 1, 2] ^ a[i - 1, 3]
  else:
   a[i, j] = a[i - 1, j - 1]
print("\nThe State Table is: ",a)

y = a[:, 3]
print("PN Sequence is:",y)

b = np.count_nonzero(y)
print("\nThe Number of Ones: ",b)

c = len(y) - b
print("\nThe Number of Zeroes: ",c)