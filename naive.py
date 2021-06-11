n= int(input("Enter the degree of the matrix:  "))
while n <= 1:
    n= int(input("re-enter correct matrix size:  "))
A=[]
print("Enter the entries rowwise:")
  
# For user input
for i in range(n):          # A for loop for row entries
    a =[]
    for j in range(n):      # A for loop for column entries
        while(1):
            try:
                a.append(float(input("enter the values of the seccond matrix:  ")))
                break
            except:
                print("enter a correct value")
    A.append(a)

B=[]
print("Enter the entries rowwise:")    
for i in range(n):          # A for loop for row entries
    b =[]
    for j in range(n):      # A for loop for column entries
        while(1):
            try:
                b.append(float(input("enter the values of the seccond matrix:  ")))
                break
            except:
                print("enter a correct value")
    B.append(b)

O= [ [0] * (len(A)) for i in range(len(A))]

for i in range( len(A)):
    for j in range(len( B[0])): ## to be able to fill the correct entry in the new matrix O
        for k in range(len(B)):
            O[i][j] +=( A[i][k] * B[k][j]) ## swapped [k] and [j] to be able to access the columns in matrix B

print('output list using the naive multiplication (brute force)', O)
###############################################################################################################################################
############################ Since it is 3 loops the Big O is N^3 because of the 3 for loops###################################################
###############################################################################################################################################
