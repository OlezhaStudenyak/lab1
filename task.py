import matplotlib.pyplot as plt
import numpy as np
import math
from collections import Counter

data = [11, 12, 10, 7, 8, 11, 13, 12, 11, 10, 7, 10, 10, 10, 10, 10, 11, 4, 9, 13, 12, 7, 9, 10, 9, 8, 13, 10, 11, 12,
        6, 11, 12, 8, 8, 10, 9, 8, 10, 8, 9, 10, 12, 10, 13, 8, 9, 9, 8, 8, 11, 11, 11, 9, 10, 11, 7, 12, 10, 10, 8, 7,
        9, 12, 9, 8, 10, 14, 11, 11, 10, 11, 10, 13, 9, 8, 8, 12, 10, 10, 9, 11, 11, 11, 8, 9, 13, 8, 7, 9, 13, 12, 13,
        9, 8, 9, 13, 10, 10, 13, 9, 8, 10, 9, 9, 10, 11, 11, 10, 13, 10, 11, 6, 10, 9, 9, 11, 13, 13, 10, 9, 12, 11, 8,
        8, 10, 13, 9, 9, 10, 7, 11, 10, 11, 10, 10, 9, 9, 10, 12, 11, 13, 10]

# полігон частот
def plot_polygon(data):
    sorted_data = sorted(data)  # Сортуємо дані за зростанням
    y = np.arange(1, len(sorted_data) + 1) / len(sorted_data)  # Відносна частота
    plt.plot(sorted_data, y, marker='.', linestyle='none')  # Побудова полігону
    plt.xlabel('Значення')
    plt.ylabel('Відносна частота')
    plt.title('Полігон частот')
    plt.show()

# гістограма частот
def plot_histogram(data):
    plt.hist(data, bins='auto', edgecolor='black')  # Побудова гістограми
    plt.xlabel('Значення')
    plt.ylabel('Частота')
    plt.title('Гістограма частот')
    plt.show()

def data_mean(data):
    n = len(data)
    mean = sum(data) / n
    return mean

def median(data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    if n % 2 == 1:
        median = sorted_data[n // 2]
    else:
        median = (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
    return median


def mode(data):
    freq_counter = Counter(data)
    max_count = max(freq_counter.values())
    modes = [value for value, count in freq_counter.items() if count == max_count]
    return modes

def data_variance(data):
    n = len(data)
    mean = sum(data) / n
    variance = sum((x - mean) ** 2 for x in data) / (n - 1)
    return variance


def standard_deviation(data):
    variance = data_variance(data)
    standard_deviation = math.sqrt(variance)
    return standard_deviation



# діаграма розмаху
def plot_boxplot(data):
    plt.boxplot(data, vert=False)  # Побудова діаграми розмаху
    plt.xlabel('Значення')
    plt.title('Діаграма розмаху')
    plt.show()

# діаграма Парето
def plot_pareto(data):
    sorted_data = sorted(data)[::-1]  # Сортуємо дані у спадному порядку
    cumulative_percent = np.cumsum(sorted_data) / np.sum(sorted_data)  # Накопичена частка
    x = np.arange(len(sorted_data))
    fig, ax1 = plt.subplots()
    ax1.bar(x, sorted_data, color='tab:blue')  # Гістограма значень
    ax1.set_ylabel('Значення')
    ax2 = ax1.twinx()
    ax2.plot(x, cumulative_percent, color='tab:red', marker='o', linestyle='--')  # Накопичена частка
    ax2.set_ylabel('Накопичена частка')
    ax2.set_ylim([0, 1])
    ax1.set_xticks(x)
    ax1.set_xticklabels(x + 1)
    plt.xlabel('Номер')
    plt.title('Діаграма Парето')
    plt.show()

# кругова діаграма
def plot_pie_chart(data):
    unique_values, value_counts = np.unique(data, return_counts=True)
    plt.pie(value_counts, labels=unique_values, autopct='%1.1f%%')  # Кругова діаграма
    plt.title('Кругова діаграма')
    plt.show()


plot_polygon(data)
plot_histogram(data)
mean = data_mean(data)
median = median(data)
modes = mode(data)
variance = data_variance(data)
standard_deviation = standard_deviation(data)


print("вибіркове середнє:", mean)
print("медіана:", median)
print("мода:", modes)
print("вибіркова дисперсія:", variance)
print("середньоквадратичне відхилення:", standard_deviation)

plot_boxplot(data)
plot_pareto(data)
plot_pie_chart(data)

