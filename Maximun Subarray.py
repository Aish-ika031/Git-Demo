nums=list(map(int, input().split()))
maxx=-999999
for i in range(len(nums)):
    curr_sum=0
    for j in range(i,len(nums)):
        curr_sum+=nums[j]
        maxx=max(maxx,curr_sum)
print("Maximum Subarray:", maxx)
