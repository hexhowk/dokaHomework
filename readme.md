#Tasks from Doka for Homework

##Задача №1.
Написать метод domain_name, который вернет домен из url адреса:

```url = "http://github.com/carbonfive/raygun" -> domain name = "github"
url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
url = "https://www.cnet.com"                -> domain name = "cnet"
```


##Задача №2.
Написать метод int32_to_ip, который принимает на вход 32-битное целое число (integer) и возвращает строковое представление его в виде IPv4-адреса:

```2149583361 -> "128.32.10.1"
32         -> "0.0.0.32"
0          -> "0.0.0.0"
```


##Задача №3.
Написать метод zeros, который принимает на вход целое число (integer) и возвращает количество конечных нулей в факториале (N! = 1 * 2 * 3 * ... * N) заданного числа:

```zeros(6) = 1
# 6! = 1 * 2 * 3 * 4 * 5 * 6 = 720 --> 1 trailing zero

zeros(12) = 2
# 12! = 479001600 --> 2 trailing zeros
```


##Задача №4.
Написать метод bananas, который принимает на вход строку и возвращает количество слов «banana» в строке.

``` Input: bbananana
Outnput: b-anana--  b-anan--a   b-ana--na   b-an--ana
         b-a--nana  b---anana   -banana--   -banan--a
         -bana--na  -ban--ana   -ba--nana   -b--anana
```


##Задача №5.
Написать метод count_find_num, который принимает на вход список простых множителей (primesL) и целое число, предел (limit), после чего попробуйте сгенерировать по порядку все числа. Меньшие значения предела, которые имеют все и только простые множители простых чисел primesL.

``` primesL = [2, 5, 7]
limit = 500
List of Numbers Under 500          Prime Factorization
___________________________________________________________
           70                         [2, 5, 7]
          140                         [2, 2, 5, 7]
          280                         [2, 2, 2, 5, 7]
          350                         [2, 5, 5, 7]
          490                         [2, 5, 7, 7]
```

``` primesL = [2, 5, 7]
limit = 500
count_find_num(primesL, val) == [5, 490]
```