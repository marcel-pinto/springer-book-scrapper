import requests
import urllib.parse

def get_links(file_name):
    with open(file_name, 'r') as file:
        urls = file.read().splitlines()
        return urls

def get_correct_url(url):
    res = requests.get(url)
    if res.status_code == 200:
        return urllib.parse.unquote(res.url)
    with open('linksWithProblems.txt', 'a') as file:
        file.write(f'{url}\n')

def write_correct_urls(urls):
    with open('parsedLinks.txt', 'w') as file:
        for url in urls:
            file.write(f'{get_correct_url(url)}\n')
    

urls = get_links('linksFromLucasPdf.txt')
write_correct_urls(urls)
