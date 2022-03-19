l = []
ans = []

num = int(input("Введите количество чисел "))

for x in range(num):
    n = int(input("Введите число "))
    l.append(n)

for x in l:
    if x % 3== 0:
        ans.append(x)



print(f"Answer is {sum(ans)}")
