# Given an array arr[] of size N-1 with integers in the range of [1, N], the task is to find the missing number from the first N integers.
# Sample Input : [2, 3 ,4 ,5] 
# Sample Output : 1

n=int(input())
arr=list(map(int, input().split()))
arr_sum=sum(arr)
total_sum=(n*(n+1))//2
print("Missing Element is:", (total_sum-arr_sum))

