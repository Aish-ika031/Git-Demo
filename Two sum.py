nums=list(map(int,input().split()))
target=int(input())
d1={}
for i in range(len(nums)):
    rem=target-nums[i]
    if rem in d1:
        print(i,d1[rem])
        break
    d1[nums[i]]=i 
    print(d1)


# nums=[3,5,1,4]
# targrt=7

# d1={}
# i=0, nums[i]=3, rem=4
# d1[nums[i]]=i -> d1={3:0}

# i=1, nums[i]=5 , rem=2
# d1[nums[i]]=i -> d1={3:0, 5:1}

# i=2, nums[i]=1, rem=6
# d1[nums[i]]=i -> d1={3:0, 5:1, 1:2}

# i=3, nums[i]=4, rem=3
# print(i,d1[rem]) => 3,0