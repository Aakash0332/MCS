X = int(input("total no. of cells in cellular system X (enter 2100): "))

#case1
print("\ncase1: Large vlaue of N (N = 7 cells)")
N1 = int(input("total no. of cells in cellular system N1 (enter 7) : "))
S = int(input("cluster capacity S in channels (enter 2000): "))
M1 = X/N1
C1 = M1*S
K1 = C1/(M1*N1)
print("total no. of channels per cell K1 : ",K1,"channels")
print("No. of clusters M1 : ",M1)
print("capacity of cellular system C1 : ",C1,"channels")

#case2
print("\ncase2: Large vlaue of N (N = 3 cells)")
N2 = int(input("total no. of cells in cellular system N2 (enter 3) : "))
S = int(input("cluster capacity S in channels (enter 2000): "))
M2 = X/N2
C2 = M2*S
K2 = C2/(M2*N2)
print("total no. of channels per cell K2 : ",K2,"channels")
print("No. of clusters M2 : ",M2)
print("capacity of cellular system C2 : ",C2,"channels")
if(C2>C1) :
    print("\ncapacity increase with decrese in cluster size")
else :
    print("\ncapacity decrease with increase in cluster size")