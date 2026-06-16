import math

pt_A = [-3, 4, -5]
pt_B = [2, 0, -4]

AB = math.sqrt(abs((pt_B[0]-pt_A[0]) + (pt_B[1]-pt_A[1]) + (pt_B[2]-pt_A[2])))
print(float(AB))