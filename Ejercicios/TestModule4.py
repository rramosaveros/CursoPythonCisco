def f(x):
    if x == 0:
        return 0
    return x + f(x-1)

print(f(3))


def fun(s):
    s += 1
    return s

s = 2
s = fun(s+1)
print(s)

#def ff(a,b):
#    return a ** a

#print(ff(2))


def funco(a):
    return a**a
def funco2(a):
    return funco(a) * funco(a)
print(funco2(2))

def funcc(z):
    if z % 2 == 0:
        return 1
    else:
        return
#print(funcc(funcc(2)) + 1)

def nami(d):
    global y
    y = d * d
    return y
nami(2)
print(y)

def any():
    print(var + 1, end='')

var = 1
any()
print(var)

def funcco(x, y, z):
    return x + 2 * y + 3 *z
print(funcco(0, z=1, y=3))


def funy(inp=2, out=3):
    return inp * out
print(funy(out=2))


dct = {'one':'two', 'three':'one', 'two':'three'}
v = dct['one']
for k in range(len(dct)):
    v = dct[v]
print(v)

tup = (1,2,4,8)
tup = tup[1:-1]
tup = tup[0]
print(tup)

listt = [t * t for t in range(5)]

def funnny(lstt):
    del lstt[lstt[2]]
    return lstt
print(funnny(listt))

def funto(h):
    if h % 2 ==0:
        return 1
    else:
        return 2
print(funto(funto(2)))


list = ['Mary','had', 'a', 'little', 'lamb']
def list(lst):
    del lst[3]
    lst[3] = 'ram'
print(list(list))


