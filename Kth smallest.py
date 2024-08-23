# Given an array arr[] of N distinct elements and a K, Find the Kth smallest element in the given array (K < Length of array).
# Sample Input : [2, 3 , 7, 8] , K = 2
# Sample Output : 3

n=int(input())
arr=list(map(int, input().split()))
k=int(input())
arr.sort()
print("Kth smallest element:", arr[k-1])


