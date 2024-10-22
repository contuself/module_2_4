numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] #список
primes = [] #список с простыми числами
not_primes = [] #список с сотавными числами
for i in numbers: #перебор
    is_prime = True #отметил простоту числа
    if i <= 1: #если число меньше или ровно единице, то
        is_prime = False #оно не является простым числом
    else: #иначе
        for j in range(2, i): #выбранное число не делиться ни на что в диапазоне от 2 до этого числа(не включительно)
            if i % j == 0: #если число делится на другие числа, то
                is_prime = False #оно не является простым
    if is_prime: #если оно простое, то
        primes.append(i) #записываем число в список
    else: #иначе
        if i != 1: #едница не является составным числом
            not_primes.append(i) #записываем составное число в список
print(f'Простые числа: {primes}') #вывод простого числа
print(f'Не простые числа: {not_primes}') #вывод составного числа