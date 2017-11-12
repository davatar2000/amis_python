#Дано действительное положительное число a и целоe число n.

#Вычислите a**n. Решение оформите в виде функции power(a, n).

#Стандартной функцией возведения в степень пользоваться нельзя.

a = float(input())
n = int(input())
def power(a, n):
      if n == 0:
          return 1
      elif n>0:
          return a * power(a, n-1)
      else:
          return 1/a * power(a, n+1)

print (power(a, n))
