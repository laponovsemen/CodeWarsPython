"""
Your task, is to create a NxN spiral with a given size.

For example, spiral with size 5 should look like this:

00000
....0
000.0
0...0
00000
and with the size 10:

0000000000
.........0
00000000.0
0......0.0
0.0000.0.0
0.0..0.0.0
0.0....0.0
0.000000.0
0........0
0000000000
Return value should contain array of arrays, of 0 and 1, with the first row being composed of 1s. For example for given size 5 result should be:

[[1,1,1,1,1],[0,0,0,0,1],[1,1,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Because of the edge-cases for tiny spirals, the size will be at least 5.

General rule-of-a-thumb is, that the snake made with '1' cannot touch to itself.
"""

----------------------------------------------------------------------------------------------------------------------------------------------------


def spiralize(size):
    snail = [[0 for x in range(size)] for y in range(size)]
    top_border = 0
    right_border = 0
    bottom_border = 0
    left_border = 0
    i = 0
    while i < size:
        for j in range(left_border - 2, size - right_border):
            snail[top_border][j] = 1
        top_border += 2 
        i += 1
        if i > size - 1:
            break
        
        for j in range(top_border - 2, size - bottom_border):
            snail[j][size - right_border - 1] = 1
        right_border += 2  
        i += 1
        if i > size - 1:
            break
        
        for j in range(size - 1 - right_border + 2, left_border -1, -1):
            snail[size - 1 - bottom_border][j] = 1
        bottom_border += 2
        i += 1
        if i > size - 1:
            break
            
        for j in range(size - 1 -  bottom_border + 2, top_border - 1, -1):
            snail[j][left_border] = 1
        left_border += 2
        i += 1
        if i > size - 1:
            break
        
    # Make a snake
    return snail

print(spiralize(6))

[[1, 1, 1, 1, 1, 1],
 [0, 0, 0, 0, 0, 1],
 [1, 1, 1, 1, 0, 1],
 [1, 0, 1, 1, 0, 1],
 [1, 0, 0, 0, 0, 1],
 [1, 1, 1, 1, 1, 1]]
