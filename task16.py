# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
n = int(input("Введите кол-во элементов: "))
A = []
for i in range(n):
    z = int(input("Введите число: "))
    A.append(z)
x = int(input("Какое число ищем? "))
print(*A)
count = 0
for j in range(len(A)):
    if A[j] == x:
        count += 1
print(count)
