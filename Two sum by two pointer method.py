nums=list(map(int, input().split()))
target=int(input())
left=0
right=len(nums)-1
while left < right:
    current_sum= nums[left]+nums[right]
    if current_sum==target:
        print(left,right)
        break
    elif current_sum < target:
        left+=1
    else :
        right-=1



# Initial Setup: 
# arr = [ 1 ,2 3, 5, 7, 10, 11, 15]
#         left                  Right
# target = 15
# left , right = 0 , len(nums) - 1 = 8 - 1 = 7
# left , right = 0 , 7

# 1st Iteration:
# cur_sum = nums[left] + nums[right] = nums[0] + nums[7] = 1 + 15 = 16
# if cur_sum == target : 16 ==15 : False
# elif curr_sum < target: 16 < 15 : False
# else right -= 1 , right = 7 - 1 =6

# 2nd Iteration:
# arr = [ 1 ,2 3, 5, 7, 10, 11, 15]
#         left              Right
# left , right = 0 , 6
# cur_sum = nums[left] + nums[right] = nums[0] + nums[6] = 1 + 11 =12
# if curr _sum == target : 12 == 15 : False
# elif curr_sum < target: 12 < 15: True
# left += 1 , left = 0 + 1 = 1

# 3rd Iteration:
# arr = [ 1 ,2 3, 5, 7, 10, 11, 15]
#            left           Right
# left , right = 1 , 6
# curr_sum = nums[left] + nums[right] = 2+ 11 = 13
# if curr_sum == target: 13 ==15 : False
# elif curr_sum < target: 13 < 15: True
# left += 1 , left = 1+1 = 2


# 4th Iteration:
# arr = [ 1 ,2 3, 5, 7, 10, 11, 15]
#              left         Right
# left , right = 2 , 6
# cur_sum = nums[left] + nums[right] = 3 + 11 = 14
# if cur_sum ==target: 14 ==15 : False
# elif curr_sum < target: 14<15: True
# left += 1 , left = 2 + 1 = 3

# 5th Iteration:
# arr = [ 1 ,2 3, 5, 7, 10, 11, 15]
#                 left       Right
# left , right = 3 , 6
# cur_sum = nums[left] + nums[right] = 5 + 11 = 16
# if curr_sum ==target: 16 == 15 : False
# elif curr_sum < target: 16 < 15: False
# else: right -= 1 , right = 6 - 1= 5

# 6th Iteration:
# arr = [ 1 ,2 3, 5, 7, 10, 11, 15]
#                 left  Right

# left , right = 3 , 5
# curr_sum = nums[left] + nums[right] = 5 + 10 = 15
# if curr_sum == target:15 ==15 : True
# print(left , right) -> 3 5 
# break -> LOOP ENDS

# Execution ends as loop is terminated when the condition is met and break statement is there.