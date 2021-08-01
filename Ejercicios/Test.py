var = 1
while var < 10:
    print("#")
    var = var << 1

lst = [3,1,-2]
print(lst[lst[-1]])

lll = [i for i in range(-1,2)]
print(lll)

t = [[3-i for i in range(3)] for j in range(3)]
s = 0
print(t)
for i in range(3):
    s += t[i][i]
print(s)
    
lss = [[0,1,2,3] for i in range(2)]
print(lss)
print(lss[2][0])
