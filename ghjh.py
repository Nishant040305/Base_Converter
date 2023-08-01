
from numpy import str0


def f(n,a):
    n = int(n)
    a = int(a)
    k= 0
    g = ''
    while a**k<n:
        k = k+1
    for m in range(k,-1,-1):
        b = str(int(n/(a**m)))
        n = n-int(b)*a**m
        x = b
        if int(x)>9:
            x = chr(65+int(x)-10)
        g = g+x
    if g[0]==a:
        g[0]='10'
    if g[0]== '0':
        k = int(len(g))
        s = ''
        for m in range(1,k):
            s = s+g[m]
        g = s
    return g
def g(b):
    try:
        b = int(b)
    except:
        b = ord(b)-65+10
    return b
def af(n,a):
    n = str(n)
    a = int(a)
    l = [x for x in n]
    l = list(map(g,l))
    k = len(l)-1
    z = 0
    for x in l:
        y = x*(a**k)
        k=k-1
        z=z+y
    return z


if __name__ == '__main__':
    n = str(input())
    a = int(input())
    print(af(n,a))
    k = int(input())