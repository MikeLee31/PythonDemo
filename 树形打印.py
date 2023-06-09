import numpy as np

# [0. 1. 2. 3. 4. 5. 6. 7. 8.]
x = np.arange(9.0)
# [array([0., 1.]), array([2., 3., 4.]), array([5., 6., 7., 8.])]
np.split(x, [2, 5])
# [array([0., 1., 2.]), array([3., 4., 5.]), array([6., 7., 8.])]
np.split(x, 3)

A = np.arange(36).reshape((2, 2, 9))
# [
#   [
#       [ 0  1  2  3  4  5  6  7  8]
#       [ 9 10 11 12 13 14 15 16 17]
#   ]
#   [
#       [18 19 20 21 22 23 24 25 26]
#       [27 28 29 30 31 32 33 34 35]
#   ]
# ]

# A1:[[[ 0  1  2]
#      [ 9 10 11]]
#     [[18 19 20]
#      [27 28 29]]]
# A2：[[[ 3  4  5]
#      [12 13 14]]
#     [[21 22 23]
#      [30 31 32]]]
# A3：[[[ 6  7  8]
#      [15 16 17]]
#     [[24 25 26]
#      [33 34 35]]]


B = np.arange(12).reshape(3, 4)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]
[B1, B2] = np.split(B, 2, axis=1)
# B1:[[0  1]
#    [4  5]
#    [8  9]]
# B2:[[2  3]
#    [6  7]
#    [10 11]]
[B3, B4, B5] = np.split(B, 3, axis=0)
# [[0 1 2 3]]
# [[4 5 6 7]]
# [[8 9 10 11]]
print(B3)
print(B4)
print(B5)
# np.split(A, 3, axis=0)
