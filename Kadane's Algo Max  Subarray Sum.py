nums=list(map(int, input().split()))
maxx=-9999999
curr_sum=0
for i in range(len(nums)):
    curr_sum+=nums[i]
    maxx=max(maxx,curr_sum)
    if curr_sum<0:
        curr_sum=0
print(maxx)