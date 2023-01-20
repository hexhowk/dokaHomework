# Написать метод domain_name, который вернет домен из url адреса:

def domain_name(url):
    start_index = url.find("www.") + 4 if "www." in url else url.find("://") + 3
    start = url[start_index:]
    ending = start.find(".")
    domain = start[:ending]
    return domain


assert domain_name("http://google.com") == "google"
assert domain_name("http://google.co.jp") == "google"
assert domain_name("www.xakep.ru") == "xakep"
assert domain_name("https://youtube.com") == "youtube"



# Написать метод int32_to_ip, который принимает на вход 32-битное целое число (integer)
# и возвращает строковое представление его в виде IPv4-адреса:

def int32_to_ip(int32):
    return '.'.join([str(int32 >> (i << 3) & 0xFF)
        for i in range(4)[::-1]])


assert int32_to_ip(2154959208) == "128.114.17.104"
assert int32_to_ip(0) == "0.0.0.0"
assert int32_to_ip(2149583361) == "128.32.10.1"



# Написать метод zeros, который принимает на вход целое число (integer)
# и возвращает количество конечных нулей в факториале (N! = 1 * 2 * 3 * ... * N) заданного числа:

def zeros(n):
    res = 0 
    while n > 0:
        n = n // 5
        res += n
    return res


assert zeros(0) == 0
assert zeros(6) == 1
assert zeros(30) == 7



# Написать метод bananas, который принимает на вход строку
# и возвращает количество слов «banana» в строке.

from functools import lru_cache

@lru_cache(None)
def items(word, schema):
    res = []
    if schema == "":
        res.append("".rjust(len(word), '-'))
        return res
    for i in range(len(word)):
        if schema[0] == word[i]:
            left_s = "".rjust(i, '-') + word[i]
            if word[i + 1 :] == "" and schema[1:] == "":
                res.append(left_s)
            else:
                right_s_list = items(word[i + 1 :], schema[1:])
                for j in right_s_list:
                    res.append(left_s + j)
    return res

def bananas(word) -> set:
    return set(items(word, "banana"))


assert bananas("banann") == set()
assert bananas("banana") == {"banana"}
assert bananas("bbananana") == {"b-an--ana", "-banana--", "-b--anana", "b-a--nana", "-banan--a",
                     "b-ana--na", "b---anana", "-bana--na", "-ba--nana", "b-anan--a",
                     "-ban--ana", "b-anana--"}
assert bananas("bananaaa") == {"banan-a-", "banana--", "banan--a"}
assert bananas("bananana") == {"ban--ana", "ba--nana", "bana--na", "b--anana", "banana--", "banan--a"}