from math import factorial as fact
maxx=10**5+10
def populateAndIncreaseCount(count,string):
    for i in string:
        count[int(i)]+=1
    for i in range(maxx):
        count[i]+=count[i-1]

def updatecount(count,ch):
    for i in range(int(ch),maxx):
        count[i]-=1

def findRank(string):
    length=len(string)
    mul=fact(length)
    rank=1
    count=[0]*maxx
    populateAndIncreaseCount(count,string)
    for i in range(length):
        mul/=length-i
        rank+=count[int(string[i])-1]*mul
        updatecount(count,string[i])
    return rank

s=['1','2','3','4','5','6','7','8','10','9']
print findRank(s)
    
