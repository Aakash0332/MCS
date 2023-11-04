import math
print("case1 : Large values of cluster size N = 7")
N = 7
n = 3
Q = math.sqrt((3*N))
print("Co-channel reuse ratio: ",Q)
# Equidistant
s1 = (Q**n)/6
print("Normal value of s1 is ", s1) 
S1 = 10*(math.log(s1,10))
print("S1 in db is ",S1 )
# Non-Equidistant
s2 = 1/(2*(Q+1)**(-n)) + (2*(Q)**(-n)) + (2*(Q-1)**(-n))
print("Normal value of s2 is ", s2)
S2 = 10*(math.log(s2,10))
print("S2 in db is ",S2 )
print("\ncase2 : Small values of cluster size N = 3")
N = 3
n = 3
Q = math.sqrt((3*N))
print("Co-channel reuse ratio: ",Q)
# Equidistant
s3 = (Q**n)/6
print("Normal value of s3 is ", s3)
S3 = 10*(math.log(s3,10))
print("S3 in db is ",S3 )
# Non-Equidistant
s4 = 1/(2*(Q+1)**(-n)) + (2*(Q)**(-n)) + (2*(Q-1)**(-n))
print("Normal value of s4 is ", s4)
S4 = 10*(math.log(s4,10))
print("S4 in db is ",S4)
if (S1>S3):
    print("S/I increases with increase in cluster size")
else:
    print("S/I decreases with decrease in cluster size")
if (S2>S4):
    print("S/I increases with increase in cluster size")
else:
    print("S/I decreases with decrease in cluster size")
