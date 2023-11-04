import math
n = 4
N = 7
Q = math.sqrt((3*N))
print("\nCase1: S/I for omnidirectional cell")
s1 = 1/(2*(Q+1)**(-n) + 2*Q**(-n) + 2*(Q-1)**(-n) )
print("S/I for omnidirectional cell",s1)
s1 = 10*math.log10(s1)
print("S/I for omnidirectional cell in db",s1)
print("\nCase2: S/I for 3-sector cell")
s2 = 1/((Q+0.7)**(-n) + Q**(-n))
print("S/I for 3-sector cell",s2)
s2 = 10*math.log10(s2)
print("S/I for 3-sector cell in db",s2)
print("\nCase3: S/I for 3-sector cell")
s3 = 1/((Q+0.7)**(-n) )
print("S/I for 6-sector cell",s3)
s3 = 10*math.log10(s3)
print("S/I for 6-sector cell in db",s3)
if(s3>s2>s1) :
    print("\n(S/I) ratio increase / improve with cell sectoring")