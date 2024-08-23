#Given an array of random numbers, Push all the zero’s of a given array to the end of the array. 
# For example, if the given arrays is {1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0}, it should be changed to {1, 9, 8, 4, 2, 7, 6, 0, 0, 0, 0}.

n= int(input())
arr=list(map(int, input().split()))
res=[]
j=-1
for i in range(len(arr)):
    if arr[i]!=0:
        j+=1
        arr[i],arr[j]=arr[j],arr[i] 
print(arr)
    

# res=[]
# for i in arr:
#     if i!=0:
#         res.append(i)
# diff=len(arr)-len(res)
# for i in range(diff):
#     res.append(0)
# print(res)


    
