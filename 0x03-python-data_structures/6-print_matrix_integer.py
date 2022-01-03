#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    #for i in range(len(matrix)):
        #for j in range(len(matrix[i])):
            #print('{}'.format(matrix[i][j]), end="\n")
#a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
    #for row in matrix:
        #for elem in row:
            #print(elem, end=' ')
    #print()
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print('{}'.format(matrix[i][j]), end=" ")
    print()
