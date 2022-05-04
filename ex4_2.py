import time

n=int(input('Введите верхнюю границу ряда '))
start=time.time()
primary=[2,3,5,7,11]
for i in range(2,n):
    if(i%2!=0 and i%3!=0 and i%5!=0 and i%7!=0 and i%11!=0 ) :
        primary.append(i)
print(f'В этом ряду {len(primary)} простых чисел')
idx=2077925
print(primary[idx-1])
print(time.time()-start)
#алгоритм ищет число под номером 10k за 3 секунды, при 10 миллионах чисел, последнее число, так де за 3 секунды
# def eratosthenes_sieve(n):
#     count = 1
#     start = 3
#     end = 4 * n
#
#     sieve = [i for i in range(start, end) if i % 2 != 0]
#     prime = [2]
#
#     if n == 1:
#         return 2
#
#     while count < n:
#
#         for i in range(len(sieve)):
#
#             if sieve[i] != 0:
#                 count += 1
#
#                 if count == n:
#                     return sieve[i]
#
#                 j = i + sieve[i]
#
#                 while j < len(sieve):
#                     sieve[j] = 0
#                     j += sieve[i]
#
#         prime.extend([i for i in sieve if i != 0])
#
#         start, end = end, end + 2 * n
#         sieve = [i for i in range(start, end) if i % 2 != 0]
#
#         for i in range(len(sieve)):
#
#             for num in prime:
#
#                 if sieve[i] % num == 0:
#                     sieve[i] = 0
#                     break
#
# start=time.time()
# print(eratosthenes_sieve(idx))
# print(time.time()-start)
#алгоритм находит 10к число за 6 секудн, 20к число за 22 секунды, сложность О(n), этот алгоритм медленее, чем тот, что без решета
