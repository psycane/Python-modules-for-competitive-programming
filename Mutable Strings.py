import UserString
s1=raw_input()
s2=raw_input()
s1=UserString.MutableString(s1)
s2=UserString.MutableString(s2)

for i in range(len(s1)):
    s1[i]=s2[i]

print s1
print s2
