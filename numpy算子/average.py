import numpy as np

x4_input = [[1, 2, 3, 4], [5, 6, 7, 8]]

x4_output1 = np.average(x4_input, axis=1, returned=False)
# [2.5 6.5]
x4_output2 = np.average(x4_input, axis=1, returned=True)
# (array([2.5, 6.5]), array([4., 4.]))
print(x4_output1)
print(x4_output2)

