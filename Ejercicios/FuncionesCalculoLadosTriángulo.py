def esUnTriangulo (a, b, c):
    return a + b > c and b + c > a and c + a > b

print(esUnTriangulo (1, 1, 1))
print(esUnTriangulo (1, 1, 3))