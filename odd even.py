n=int(input())
arr=list(map(int, input().split()))
j=-1
for i in range(len(arr)):
    if arr[i]%2==0:
        j+=1
        arr[i],arr[j]=arr[j],arr[i]  #swapping
print(arr)

  
# res=[]
# for i in arr:
#     if i%2==0:
#         res.append(i)
# for i in arr:
#     if i%2!=0:
#         res.append(i)
# print(res)


# even=[]
# odd=[]
# for i in arr: #i denotes array elements
#     if i%2==0:
#         even.append(i)
#     else:
#         odd.append(i)
# print("Even numbers:",even, "Odd numbers:",odd)


# for i in range(0,len(arr)):
#     if arr[i]%2==0:
#         even.append(arr[i])
#     else:
#         odd.append(arr[i])
# print("Even numbers:",even, "Odd numbers:",odd)

