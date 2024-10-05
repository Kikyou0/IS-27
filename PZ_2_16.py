#Дано трехзначное число. Найти сумму и произведение его цифр.
n = int(input("Введите трехзначное число: "))

suma = 0
mult = 1

while n > 0:
    number = n % 10
    suma = suma + number
    mult = mult * number
    n = n // 10

print("Сумма:", suma)
print("Произведение:", mult)
