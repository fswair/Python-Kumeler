import math
import time
# küme oluşturme
# set() function
# set() veya {}

# birleşim
# union()
un = set(input(" : "))

def funcSet(u):
    print(u.union(u))

funcSet(un)


# kesişim
# intersection

un1 = set(input(" : "))

a = un.intersection(un1)

def fonk(ab):
    print(ab)
fonk(a)

# difference function

b = un.difference(un1)

def fonk1(ba):
    print(ba)
fonk1(b)


# symmetric_difference function
ax = un.symmetric_difference(un1)
def symm(axc):
    print(axc)
symm(ax)
time.sleep(56)

# alt kümesi mi? issubset function

abx = un1.issubset(un)

def subset(abc):
    print(abc)
subset(abx)

# classic math functions

# a) kare alma
x = 10
v = pow(x,2)

print(v)

# b) üs alma


def üs(x, y):
    g = pow(x,y)
    print(g,"\n")
hc = int(input("Taban sayısı giriniz..: "))
hz = int(input("Üs sayısı giriniz..: "))
üs(hc,hz)

# karekök alma

def karekok(x):
    f = math.sqrt(x)
    print(f)
h = int(input("Karekökü alınacak sayı..: "))
karekok(h)
# mutlak değer alma
def mutlak(x):
    d = math.fabs(x)
    print(d)
hx = int(input("Mutlak değeri alınacak sayı..: "))
mutlak(hx)


# Python | Fonksiyon nasıl yazılır?
# Örnek:
def function(x,y):
  if(x > y):
    y = x + 1
    print(y)
function(15,9)
# Çıktı: 15, 9'dan büyük olduğu için;
# y = 9 iken x(15) + 1 olmuştur,
# Yeni değer 16 olur ve 16 yazdırılır.



# @FLUSWAIR | GITHUB.COM/FSWAIR
