# pylint: disable=missing-docstring
from random import randint

cache = {}

def get_data_from_server(url):
    return f"The content from {url} is: {randint(1,1000)}"

def get_page(url):
    if cache.get(url):
        return cache[url]
    data = get_data_from_server(url)
    cache[url] = data
    return data

print(get_page("www.example.com"))
print(get_page("www.example.com/about"))
print(get_page("www.example.com"))
