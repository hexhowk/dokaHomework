# Написать метод domain_name, который вернет домен из url адреса:

def domain_name(url):
    start_index = url.find("www.") + 4 if "www." in url else url.find("://") + 3
    start = url[start_index:]
    ending = start.find(".")
    domain = start[:ending]
    print(domain)
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