import numpy as np
import scipy.stats as stats

data = [11, 12, 10, 7, 8, 11, 13, 12, 11, 10, 7, 10, 10, 10, 10, 10, 11, 4, 9, 13, 12, 7, 9, 10, 9, 8, 13, 10, 11, 12,
        6, 11, 12, 8, 8, 10, 9, 8, 10, 8, 9, 10, 12, 10, 13, 8, 9, 9, 8, 8, 11, 11, 11, 9, 10, 11, 7, 12, 10, 10, 8, 7,
        9, 12, 9, 8, 10, 14, 11, 11, 10, 11, 10, 13, 9, 8, 8, 12, 10, 10, 9, 11, 11, 11, 8, 9, 13, 8, 7, 9, 13, 12, 13,
        9, 8, 9, 13, 10, 10, 13, 9, 8, 10, 9, 9, 10, 11, 11, 10, 13, 10, 11, 6, 10, 9, 9, 11, 13, 13, 10, 9, 12, 11, 8,
        8, 10, 13, 9, 9, 10, 7, 11, 10, 11, 10, 10, 9, 9, 10, 12, 11, 13, 10]

# функція пошуку двосторонього довірчого інтервалу на математичне сподівання
def interval_mean(data):
    n = len(data)
    confidence_level = 0.95
    mean = sum(data) / n
    standard_deviation = 1.7

    # Розраховуємо критичне значення (Z) для заданого рівня довіри
    z_value = stats.t.ppf((1 + confidence_level) / 2, n - 1)

    # Обчислюємо межу похибки
    margin_error = z_value * standard_deviation / np.sqrt(n)

    # Обчислюємо довірчий інтервал
    confidence_interval = (mean - margin_error, mean + margin_error)
    return confidence_interval


# функція пошуку двосторонього довірчого інтервалу на середньо квадратичне відхилення
def interval_standard_deviation(data):
    n = len(data)
    confidence_level = 0.95
    standard_deviation = 1.7

    # Розраховуємо критичні значення (нижнє та верхнє) для заданого рівня довіри та ступенів свободи
    chi2_lower = stats.chi2.ppf((1 - confidence_level) / 2, n - 1)
    chi2_upper = stats.chi2.ppf((1 + confidence_level) / 2, n - 1)

    # Обчислюємо межі довірчого інтервалу
    confidence_interval = (np.sqrt((n - 1) * standard_deviation ** 2 / chi2_upper),
                           np.sqrt((n - 1) * standard_deviation ** 2 / chi2_lower))
    return confidence_interval




print(f'Довірчий інтервал на математичне сподівання: {interval_mean(data)}')
print(f'Довірчий інтервал на середньоквадратичне відхилення: {interval_standard_deviation(data)}')





datas_size = [50, 100, 200]
confidence_level = [0.95, 0.99]
standard_deviation = 1.7
mean = 10

for size in datas_size:
    for level in confidence_level:
        data = np.random.normal(loc=mean, scale=standard_deviation, size=size)
        confidence_interval_mean = stats.t.interval(level, size - 1, loc=np.mean(data), scale=stats.sem(data))
        confidence_interval_std = stats.chi2.interval(level, size - 1, scale=np.std(data))
        print(f"Довірчий інтервал для обсягу вибірки {size}, рівня довіри {level}:")
        print(f"Довірчий інтервал для математичного сподівання: {confidence_interval_mean}")
        print(f"Довірчий інтервал для середньоквадратичного відхилення: {confidence_interval_std}")
        print("---------------------")