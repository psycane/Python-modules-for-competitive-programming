def check(n):
    if n&(n-1)==0:
        return True
    else:
        return False

print check(1024)
print check(500)
print check(100)
