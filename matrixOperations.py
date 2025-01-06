row,column = map(int,input().split())
matrix1 = []
for i in range(row):
    line = list(map(int,input().split()))
    matrix1.append(line)

matrix2 = []
for i in range(row):
    line = list(map(int,input().split()))
    matrix2.append(line)


def matrixAddition(matrix1,matrix2):
    finalMatrix = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        finalMatrix.append(row)
    
    for row in finalMatrix:
        print(' '.join(map(str,row)))



def matrixSubstraction(matrix1,matrix2):
    finalMatrix = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] - matrix2[i][j])
        finalMatrix.append(row)
    
    for row in finalMatrix:
        print(' '.join(map(str,row)))









print("Matrix Addition")
matrixAddition(matrix1,matrix2)

print("Matrix Substraction")
matrixSubstraction(matrix1,matrix2)

# print("Matrix Multiply")
# print(matrixMultiply(matrix1,matrix2))

# print("Matrix Transpose")
# print(matrixtranspose(matrix1))

# print("Matrix DiagonalSum")
# print(matrixDiagonalSum(matrix1))