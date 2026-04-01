rows,cols = 3,3
matrix = [[i*j for j in range(cols)]for i in range(rows)]

print("matrix:")
for row in matrix:
    print(row)