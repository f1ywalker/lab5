import random
spisok = []
for i in range(5):
    spisok.append(random.randrange(1,20))
n = int(input("Введите число: "))
if n in spisok:
    print(spisok, n, "\nПоздавляю, вы угадали!")
else:
    print(spisok,n, "\nТакого числа нет в списке")

from collections import Counter
import random
spisok = []
for i in range(10):
    spisok.append(random.randrange(1,20))
counter = Counter(spisok)
print(counter)

