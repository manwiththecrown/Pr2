year = int(input("Введите год: "))
result = 0
tens = 0
units = 0

monthsWith31Days = 7
monthsWith30Days = 4
monthWith28Days = 1

days31 = 1
days30 = 1
days28 = 1

while days31 <= 31:
    tens = days31 // 10
    units = days31 % 10
    result += monthsWith31Days * (tens + units)
    days31 += 1

while days30 <= 30:
    tens = days30 // 10
    units = days30 % 10
    result += monthsWith30Days * (tens + units)
    days30 += 1 

if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
    
    while days28 <= 28:
        tens = days28 // 10
        units = days28 % 10
        result += monthWith28Days * (tens + units)
        days28 += 1
else:
    while days28 <= 29:
        tens = days28 // 10
        units = days28 % 10
        result += monthWith28Days * (tens + units)
        days28 += 1

print(f"Сумма дней в {year} году = {result}")

