#Find the majority element in the array. A majority element in an array A[] of size n is an element that appears more than or equal to n/2 times (and hence there is at most one such element).

from collections import Counter
n=int(input())
arr=list(map(int, input().split()))
mp={}
#mp=Counter(arr)
for i in arr:
    if i not in mp:
        mp[i]=1
    else:
        mp[i]+=1
    print(mp)
#print(mp)
#n=n/2
a=(n//2)
for i in mp:
    if mp[i]>=a:
        print("Majority Element:",i) #i:key or element ,mp[i]:value
        break
    
# Complexity:o(n)


