per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
a = list(per_cent.values()) #вызывает список значений из библиотеки и создает из них список процентных ставок
b = input("Введите сумму") #запрашивает данные на ввод, а именно сумму денежных средств
c = float(b)/100 #присваивает данным, введенной суммы тип данных float (чтобы считать с копейками) и высчитывает 1%
#от введенной суммы
print('money =',b) #вызывает введенные раннее данные (а именно введенную сумму)

for i in range(len(a)): #определяет диапазон итерации внутри списка
    a[i] *= c #производит умножение каждого значения в списке процентных ставок на величину одного процента
#введенной суммы
print("deposit =",a) #вызывает список рассчитаных депозитов

print("Максимальная сумма, которую вы можете заработать =", max(a)) #определяет в списке депозитов макскимальное
#значение и вызывает его