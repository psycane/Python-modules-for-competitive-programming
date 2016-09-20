""" Works only if 'm' is prime """
def mod_inv(n,m):
    n=n%m
    return pow(n,m-2,m)

mod=10**9+7
print mod_inv(9,mod)
