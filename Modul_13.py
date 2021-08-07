Num_of_tickets = int(input("Введите количество билетов \n"))

Age_list = [int(input(f"Укажте возраст {i+1}го зрителя \n")) for i in range(Num_of_tickets)]

S = 0 # Сумма к оплате
Count = 0 # счетчик платных билетов
for age in Age_list:
    if 18 <= age < 25:
        S += 990
        Count = Count + 1
    if 25 <= age:
        S += 1390
        Count = Count + 1
    else:
        S = S
if 3 < Count:
    S = int(S * 0.9)

print(f"Сумма к оплате {S} рублей")
print(f"Количество платных билетов {Count} шт")
