import numpy as np

x1_input = [1, 2, 7, 0, np.nan]

x1_output1 = np.nanmax(x1_input)
print(x1_output1)
# 7.0
x2_input = [[np.nan, 17, 12, 33, 44],
            [15, 6, 27, 8, 19]]

x2_output1 = np.nanmax(x2_input,axis=0)
# [15. 17. 27. 33. 44.]

x2_output2 = np.nanmax(x2_input,axis=1)
# [44. 27.]

print(x2_output1)
print(x2_output2)

x3 = np.arange(5)
np.nanmax(x2_input,axis=0,out=x3)
print(x3)


