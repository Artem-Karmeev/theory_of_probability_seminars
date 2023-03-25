# На входной двери подъезда установлен кодовый замок, содержащий десять кнопок с цифрами от 0 до 9. 
# Код содержит три цифры, которые нужно нажать одновременно. 
# Какова вероятность того, что человек, не знающий код, откроет дверь с первой попытки?
import numpy as np

count_num = 10
combination = 3
win_combination = 1

# Находим все способы нажать на 3 кнопки кодового замка, на котором всего 10 кнопок. Используя формулу сочетания
count_combinations = np.math.factorial(count_num) / (np.math.factorial(combination) * np.math.factorial(count_num - combination))  

# Применяем к имеющимся данным формулу определения вероятности Р(А) = m/n
probability_open = win_combination / count_combinations

print(f'Вероятность открыть замок с первой попытки составляет: {probability_open} или {round(probability_open, 4) * 100} % ;')

