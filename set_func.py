import math
import time
# küme oluşturme
# set() function
# set() veya {}

# birleşim
# union()
un = set(input(" : "))
un1 = set(input(" : "))

def funcSet(x, y):
    return x.union(y)

print(funcSet(un, un1))


# kesişim
# intersection

def fonk(a, b):
    ab = un.intersection(un1)
    return ab
print(fonk(un, un1))

# difference function



def fonk1(x, y):
    b = x.difference(y)
    return b
print(fonk1(un, un1))


# symmetric_difference function

def symm(x, y):
    ax = x.symmetric_difference(y)
    return ax
print(symm(un, un1))

# alt kümesi mi? issubset function



def subset(x, y):
    abx = x.issubset(y)
    return abx
print(subset(un1, un))

# classic math functions

# a) kare alma

v = pow(10,2) # veya 10 ** 2
print(v) # 10 ** 2 = 100

# b) üs alma

def us(x, y):
    g = pow(x,y) # veya x ** y
    return g
hc = int(input("Taban sayısı giriniz..: "))
hz = int(input("Üs sayısı giriniz..: "))
print(us(hc,hz))

# karekök alma

def karekok(x):
    f = math.sqrt(x)
    return f
h = int(input("Karekökü alınacak sayı..: "))
print(karekok(h))

# mutlak değer alma
def mutlak(x):
    d = math.fabs(x)
    return d
hx = int(input("Mutlak değeri alınacak sayı..: "))
print(mutlak(hx))


# Python | Fonksiyon nasıl yazılır?
# Örnek:
def function(x,y):
  if(x > y):
    y = x + 1
    return y
print(function(15,9))
# Çıktı: 15, 9'dan büyük olduğu için;
# y = 9 iken x(15) + 1 olmuştur,
# Yeni değer 16 olur ve 16 yazdırılır.

# GITHUB.COM/FSWAIR
