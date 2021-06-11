from math import ceil
import numpy as np

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
########################### trials one
# n= 3
# A= [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# B=[
#     [9,8,7],
#     [6,5,4],
#     [3,2,1]
# ]
# ########################### trials 2
# n= 2
# A= [
#     [1,2],
#     [7,8]
# ]
# B=[
#     [9,8],
#     [3,2]
# ]
########################

#### checking if the matrix needs padding by checking if its degree is a power of 2 by using bit manipulation
if (n & (n-1) != 0) and n != 0: ### 2^n
    A_pad_arr= np.pad(A, 1, mode='constant', constant_values=0)[:-1, :-1] ### pad awel row w awel column
    A_pad= A_pad_arr.tolist()
    B_pad_arr= np.pad(B, 1, mode='constant', constant_values=0)[:-1, :-1]
    B_pad= B_pad_arr.tolist()
else:
    A_pad= A
    B_pad= B

def strassen_fn(A_pad, B_pad):
    n= len(A_pad)
    if n == 1:
        return [[A_pad[0][0] *B_pad[0][0]]]
    else:
        ################ partitioning matrix A
        top_left_A =  [A_pad[i][:ceil(n / 2)] for i in range(ceil(n / 2))]
        top_right_A = [A_pad[i][ceil(n / 2):] for i in range(ceil(n / 2))]
        bot_left_A =  [A_pad[i][:ceil(n / 2)] for i in range(ceil(n / 2), n)]
        bot_right_A = [A_pad[i][ceil(n / 2):] for i in range(ceil(n / 2), n)]
        ########### partitioning matrix B
        top_left_B =  [B_pad[i][:ceil(n / 2)] for i in range(ceil(n / 2))]
        top_right_B = [B_pad[i][ceil(n / 2):] for i in range(ceil(n / 2))]
        bot_left_B =  [B_pad[i][:ceil(n / 2)] for i in range(ceil(n / 2), n)]
        bot_right_B = [B_pad[i][ceil(n / 2):] for i in range(ceil(n / 2), n)]
        ########################
        ## creation 10 matrices consisting of the adding or subtraction of the partitioned input matrices
        S_1= np.subtract(top_right_B, bot_right_B)
        S_2= np.add(top_left_A, top_right_A)
        S_3= np.add(bot_left_A, bot_right_A)
        S_4= np.subtract(bot_left_B, top_left_B)
        S_5= np.add(top_left_A, bot_right_A)
        S_6= np.add(top_left_B, bot_right_B)
        S_7= np.subtract(top_right_A, bot_right_A)
        S_8= np.add(bot_left_B, bot_right_B)
        S_9= np.subtract(top_left_A, bot_left_A)
        S_10= np.add(top_left_B, top_right_B)
        ## 
        P_1= strassen_fn(top_left_A, S_1)
        P_2= strassen_fn(S_2, bot_right_B)
        P_3= strassen_fn(S_3, top_left_B)
        P_4= strassen_fn(bot_right_A, S_4)
        P_5= strassen_fn(S_5, S_6)
        P_6= strassen_fn(S_7, S_8)
        P_7= strassen_fn(S_9, S_10)

        top_left_new= np.add(np.subtract(np.add(P_5, P_4), P_2), P_6).tolist()
        
        top_right_new = np.add(P_1, P_2).tolist()
        
        bot_left_new = np.add(P_3, P_4).tolist()
       

        bot_right_new = np.subtract(np.subtract(np.add(P_5, P_1),P_3), P_7).tolist()

    return combination_fn(top_left_new, top_right_new, bot_left_new, bot_right_new)

def empty_mat_creation(size):
    return [[None] * size for i in range(size)]

def combination_fn(top_left_new, top_right_new, bot_left_new, bot_right_new):
    size = len(top_left_new)
    c = empty_mat_creation(len(top_left_new) * 2)
    for i in range(size):
        for j in range(size):
            c[i][j] = top_left_new[i][j]
            c[i][j + size] = top_right_new[i][j]
            c[i + size][j] = bot_left_new[i][j]
            c[i + size][j + size] = bot_right_new[i][j]

    return c



output= strassen_fn(A_pad, B_pad)
if (n & (n-1) != 0) and n != 0: ### 2^n
    output_no_pad= np.delete(output, 0, 0)
    output_no_pad= np.delete(output_no_pad, 0, 1).tolist()
    print("Result of the divide and conquer alg", output )
    print("Result of the divide and conquer alg of the matrix without padding", output_no_pad )
else:
    print("Result of the divide and conquer alg", output )

