#[1 , 2, 3 ,4 ,1, 3, 5]
#o/p: [1]
n=int(input())
arr=list(map(int, input().split()))
seen=[]
for i in arr:
    if i not in seen:
        seen.append(i)
    else:
        print(i)
        break 

# break terminates nearest enclosing loop....
# [1 2 3 4 5 1 2]

# i = 1
# seen =[1 ,]

# i = 2
# seen =[1 ,2]

# i =3 
# seen = [1 , 2, 3]

# i =4
# seen = [1 , 2 , 3 , 4]

# i = 5
# seen =[1 , 2 , 3 , 4 , 5]

# i = 1
# print(i) // 1