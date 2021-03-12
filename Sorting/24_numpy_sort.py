# -numpy sort

import numpy as np

a = np.array([[1, 4], [98, 7]], float)
print(a)

b = np.array([0, 0, 1, 1, 0], int)
c = np.array([0, 1, 1, 0, 1], int)
print(a[b, c])

# ---random no generate

print(np.random.rand(6))
