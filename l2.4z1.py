def tm(m):
    rows = len(m)
    cols = len(m[0])
    
    tm = [[0 for _ in range(rows)] for _ in range(cols)]
    
    for i in range(rows):
        for j in range(cols):
            tm[j][i] = m[i][j]
    
    return tm
m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposed = tm(m)
print(transposed)