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