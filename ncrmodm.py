def modinv(a,m):
    return pow(a,m-2,m)
def nCrmodm(n,k,m):
    num=1
    for i in range(k):
        num=(num*(n-i))%m
    den=1
    for i in range(1,k+1):
        den=(den*i)%m
    return (num*modinv(den,m))%m
print nCrmodm(5,2,pow(10,9)+7)
