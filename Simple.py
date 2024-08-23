# WAP to sort the array in descending order and print the new sorted array in reverse order.

n=int(input())
arr=list(map(int, input().split()))
arr.sort(reverse=True)
print("Reversed Array:",arr)
print(arr[::-1])