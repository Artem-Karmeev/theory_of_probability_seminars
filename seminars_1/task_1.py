# Из колоды в 52 карты извлекаются случайным образом 4 карты. 
# a) Найти вероятность того, что все карты – крести. 
# б) Найти вероятность, что среди 4-х карт окажется хотя бы один туз.
import numpy as np

my_count_k = 4 # кол-во изымаемых карт
count_cards_n = 52 # всего карт

# Задание 1.а:
count_cross_n = 13 # кол-во карт одной масти 

# Находим все возможные комбинации из 4 крестовых карт используя формулу Сочетания
cross = np.math.factorial(count_cross_n) / (np.math.factorial(my_count_k) * np.math.factorial(count_cross_n - my_count_k))

# Находим все возможные комбинации из 4 карт из всей колоды используя формулу Сочетания
combination = np.math.factorial(count_cards_n) / (np.math.factorial(my_count_k) * np.math.factorial(count_cards_n - my_count_k))

# находим вероятность вытащить 4 крестовые крестовые карты используя формулу определения вероятности
p = cross / combination
print(f'Вероятность вытащить 4 крестовые карты из колоды составляет: {p} или {round(p, 4) * 100} % ;')



# Задание 1.b :
count_not_aces = 48 # кол-во не тузов в колоде

# Находим все возможные комбинации из 4 карт из всей колоды используя формулу Сочетания
combination = np.math.factorial(count_cards_n) / (np.math.factorial(my_count_k) * np.math.factorial(count_cards_n - my_count_k))

# Находим все возможные сочетания из 4 карт в колоде без тузов используя формулу Сочетания
combination_not_aces = np.math.factorial(count_not_aces) / (np.math.factorial(my_count_k) * np.math.factorial(count_not_aces - my_count_k))

# Находим комбинации в которых есть хотя бы один туз
combination_with_aces = combination - combination_not_aces

# находим вероятность получить комбинацию из 4 карт в которой есть хотя бы один туз
p = combination_with_aces / combination

print(f'вероятность того, что среди 4х карт окажется хотя бы один туз составляет: {p} или {round(p, 4) * 100} % ;')



