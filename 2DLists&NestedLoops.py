#lists inside list
# = matrix
#indexed from 0

numberGrid=[
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]
print(numberGrid[1][1])

for row in numberGrid:
    for col in row:
        print(col)