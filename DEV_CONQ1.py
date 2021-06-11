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

# top_left_A =  [A_pad[i][:ceil(n / 2)] for i in range(ceil(n / 2))]
# top_right_A = [A_pad[i][ceil(n / 2):] for i in range(ceil(n / 2))]
# bot_left_A =  [A_pad[i][:ceil(n / 2)] for i in range(ceil(n / 2), n)]
# bot_right_A = [A_pad[i][ceil(n / 2):] for i in range(ceil(n / 2), n)]


#print("matrix A", A_pad)
# print("top_left", top_left)
# print("top_right", top_right)
# print("bot_left", bot_left)
# print("bot_right", bot_right)


def Devide_Conquer_Matrix_mult(A_pad, B_pad):
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
        top_left_new= np.add(Devide_Conquer_Matrix_mult(top_left_A, top_left_B), Devide_Conquer_Matrix_mult(top_right_A, bot_left_B)).tolist()
        
        top_right_new = np.add(Devide_Conquer_Matrix_mult(top_left_A, top_right_B), Devide_Conquer_Matrix_mult(top_right_A, bot_right_B)).tolist()
        

        bot_left_new = np.add(Devide_Conquer_Matrix_mult(bot_left_A, top_left_B), Devide_Conquer_Matrix_mult(bot_right_A, bot_left_B)).tolist()
       

        bot_right_new = np.add(Devide_Conquer_Matrix_mult(bot_left_A, top_right_B), Devide_Conquer_Matrix_mult(bot_right_A, bot_right_B)).tolist()  

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



output= Devide_Conquer_Matrix_mult(A_pad, B_pad)
if (n & (n-1) != 0) and n != 0: ### 2^n
    output_no_pad= np.delete(output, 0, 0)
    output_no_pad= np.delete(output_no_pad, 0, 1).tolist()
    print("Result of the divide and conquer alg", output )
    print("Result of the divide and conquer alg of the matrix without padding", output_no_pad )
else:
    print("Result of the divide and conquer alg", output )
