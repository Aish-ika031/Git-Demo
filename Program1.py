# Write a python program to take 5 elements of array as input in a sperate line sort them in descending order and print them each on a separate line.

#arr=[1,2,3,4,5]
arr=[]
n=int(input())
for i in range(0, n):
     element = int(input())
     arr.append(element)
arr.sort(reverse=True)
print("Sorted Array:")
for i in range(0,n):
     print(arr[i])


#   space separated array
# arr=list(map(int,input().split()))
# print(arr)

