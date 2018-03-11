#1. Sum the Numbers
numbers = [-9, -8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(sum(numbers))

#2. Largest Number
print(max(numbers))

#3. Smallest Number
print(min(numbers))

#4. Even Numbers
for x in numbers:
    if x % 2 == 0:
        print(x)
        
#5. Positive Numbers:
for y in numbers:
    if y > 0:
        print(y)

#6. Positive Numbers II:
positiveNumbers = []
for z in numbers:
    if z > 0:
        positiveNumbers.append(z)
print("positiveNumbers is:", positiveNumbers)

#7. Multiply a list:
doubleNumbers = [u * 2 for u in numbers]
print("doubleNumbers is:", doubleNumbers)

#7.b Another solution:
doubleNumbers2 = list(map(lambda x:x * 2, numbers))
print("doubleNumbers2 is:", doubleNumbers2)

#8. Multiply Vectors:
numbers2 = [1, 2, 3, 4, 5]
numbers3 = [-5, -4, -3, -2, -1]
numbers4 = [numbers2[i] * numbers3[i] for i in range(0, len(numbers2))]
print(numbers4)

#8b. Use numpy: 
#import numpy as np
#a = np.array([1,2,3,4])
#b = np.array([2,3,4,5])
#c = list(a * b)
#print(c)

#9. Matrix Addition:
X = [[1, 3, 1], 
     [2, 4, 2],  
     [0, 0, 0]]
Y = [[5, 2, 5], 
     [0, 1, 0], 
     [0, 0, 0]]
Z = [[0, 0, 0], 
     [0, 0, 0], 
     [0, 0, 0]]
for i in range(0, len(X)):
    for j in range(0, len(X[0])):
        Z[i][j] = X[i][j] + Y[i][j]
for z in Z:
    print(z)

#10. Matrix Addition II:
def main():
    m=int(input("enter rows: "));
    n=int(input("enter columns: "));
 
#in python initilization is needed before indexing.
    matrix1=[[0 for j in range(0,n)] for i in range(0,m)]   # matrix 1 initialization with 0s
    matrix2=[[0 for j in range(0,n)] for i in range(0,m)]    #matrix 2 intialization with 0s
    res_matrix=[[0 for j in range(0,n)] for i in range(0,m)] # matrix for storing result
    print("enter first matrix elements")
    for i in range(0,m):
        for j in range(0,n):
            matrix1[i][j]= int(input("enter an element of {} x {}: ".format(m, n)))
    print("enter second matrix elements ")    
    for i in range(0,m):
        for j in range(0,n):
            matrix2[i][j]=int(input("enter an element of {} x {}: ".format(m, n)))
        
    for i in range(0,m):
        for j in range(0,n):
            res_matrix[i][j]=matrix1[i][j]+matrix2[i][j]
 
#print input matrices
    print("matrix1 = ", matrix1)
    print("matrix2 = ", matrix2)
        
# printing resultant matrix
    print("resultant matrix after adding = ", res_matrix)

main()    

#11. De-dup:
list1 = [1, 2, 3, 4, 1, 3, 6, 8, 10, 12, 14, 16, 17, 18, 19, 20]
list2 = [1, 3, 17, 19]
list3 = list(set(list1) - set(list2))
print("De-dup for list1 itself: ", set(list1))
print("De-dup after list1 and list2: ", list3)

#Bonus: Matrix Multiplication:
X = [[34,1,77],
     [2,14,8],
     [3 ,17,11]]

Y = [[6,8,1],
     [9,27,5],
     [2,43,31]]

result = [[0,0,0],
          [0,0,0],
          [0,0,0]]

for i in range(len(X)):
    for j in range(len(Y[0])):
        for k in range(len(Y)):
            result[i][j] += X[i][k] * Y[k][j]

for r in result:
    print(r)

#Bonus: A General Case:
def matrixmult (A, B):
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])

    if cols_A != rows_B:
        print("Cannot multiply the two matrices. Incorrect dimensions.")
        return

    # Create the result matrix
    # Dimensions would be rows_A x cols_B
    C = [[0 for row in range(cols_B)] for col in range(rows_A)]
    print(C)

    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                C[i][j] += A[i][k] * B[k][j]
    return C
    
