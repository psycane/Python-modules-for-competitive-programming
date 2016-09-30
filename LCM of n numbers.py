def gcd(x, y):
   while(y):
       x, y = y, x % y
   return x

def lcm(x, y):
   lcm = (x*y)//gcd(x,y)
   return lcm

def lcm_of_n(li):
    return reduce(lcm,li)

li=[1,2,3,4,5,6,7,8,9,10]
print lcm_of_n(li)
