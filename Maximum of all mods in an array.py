li=[2,5,7,10,100]
li.sort(reverse=True)
for i in li:
    if i!=li[0]:
        print i
        break
else:
    print 0
