def gcd(x, y):
   while(y):
       x, y = y, x % y
   return x

def lcm(x, y):
   lcm = (x*y)//gcd(x,y)
   return lcm

def lcm_of_n(li):
    return reduce(lcm,li)


print lcm_of_n(range(1,10000))
