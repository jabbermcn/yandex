# алгоритм будет выглядеть следующим образом:
#
# Инициализировать переменные: max_profit = 0, k = 0.
# Проходить по дням i от 0 до N-1.
# Если p[i] >= p[i+1], перейти к следующему дню.
# Иначе:
# Инициализировать переменную profit = 0.
# Проходить по дням j от i+1 до N-1.
# Если p[j] <= p[j-1], перейти к следующему дню.
# Иначе:
# Вычислить текущую прибыль cur_profit = p[j] - p[i].
# Если cur_profit > profit, обновить значение profit и сохранить дни i и j.
# Пройти по всем парам дней между i и j, и если прибыль больше текущей максимальной прибыли, обновить максимальную прибыль.
# Если прибыль больше 0, увеличить k на 1.
# Если k > 0, вывести k, иначе вывести 0.
# Если k > 0, вывести дни каждой пары «покупка — продажа».

n = int(input())
prices = list(map(int, input().split(' ')))

# Создаем два списка для отслеживания текущей максимальной выгоды при покупке и продаже
buy = [-1] * n
sell = [-1] * n

# Инициализируем переменные для отслеживания минимальной цены и максимальной выгоды при покупке
min_price = prices[0]
max_profit = 0

# Проходим по списку цен и заполняем список buy
for i in range(n):
    if prices[i] < min_price:
        min_price = prices[i]
    elif prices[i] - min_price > max_profit:
        max_profit = prices[i] - min_price
    buy[i] = min_price

max_price = prices[-1]
max_profit = 0

for i in range(n - 1, -1, -1):
    if prices[i] > max_price:
        max_price = prices[i]
    elif max_price - prices[i] > max_profit:
        max_profit = max_price - prices[i]
    sell[i] = max_price

max_profit = 0
buy_day = -1
sell_day = -1

for i in range(n):
    if sell[i] - buy[i] > max_profit:
        max_profit = sell[i] - buy[i]
        buy_day = buy.index(buy[i])
        sell_day = i

if max_profit == 0:
    print(0)
else:
    print(1)
    print(buy_day, sell_day)
