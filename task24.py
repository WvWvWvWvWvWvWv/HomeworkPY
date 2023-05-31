n = int(input("Введите кол-во кустов: "))
k = [int(i) for i in input("Введите кол-во ягод на кустах: ").split()]
maxk = 0
for i in range(n):
    if i == n - 1:
        sumk = k[i] + k[i - 1] + k[0]
    else:
        sumk = k[i] + k[i - 1] + k[i + 1]
    if sumk > maxk:
        maxk = sumk
print(maxk)
