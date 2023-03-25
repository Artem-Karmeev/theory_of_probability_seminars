# В ящике имеется 15 деталей, из которых 9 окрашены. 
# Рабочий случайным образом извлекает 3 детали. 
# Какова вероятность того, что все извлеченные детали окрашены?
import numpy as np

my_count = 15 # Всего деталей
paint = 9 # Кол-во окрашенных деталей
step = 3 # Кол-во деталей которое возьмет рабочий

# находим все сочетания деталей по 3 используем формулу сочетания
count_combinations = np.math.factorial(my_count) / (np.math.factorial(step) * np.math.factorial(my_count - step))

# Находим все сочетания с позитивным исходом используем формулу сочетания
pos_count = np.math.factorial(paint) / (np.math.factorial(step) * np.math.factorial(paint - step))

# Применяем к имеющимся данным формулу определения вероятности Р(А) = m/n
result = pos_count / count_combinations
print(f'Вероятность того что рабочий извлечет 3 детали и они будут окрашены: {result} или {round(result, 3) * 100} % ;')