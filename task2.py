a=int(input("Введите 3-значное число: "))
while a>999 or a<100:
    print("Введите 3-значное число!!!: ")
print(f"{(a%10)+((a//10)%10)+(a//100)} = {a//100} + {(a//10)%10} + {a%10}")