# WAP to print the count of number of 1 in the array.
n=int(input())
arr=list(map(int, input().split()))
count=0
for i in range(n):
    if arr[i]==1:
        count+=1
print("Number of 1's present in the array:",count)