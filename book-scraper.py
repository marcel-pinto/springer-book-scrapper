import csv
import scrapy
import wget

file_name = "SpringerOpenBooksSearchResults.csv"


def extract_links(file_name):
    links = set()
    with open(file_name) as csvfile:
        raw_file = csv.DictReader(csvfile)
        for row in raw_file:
            links.add(row["URL"])
    return links


class BookSpider(scrapy.Spider):
    name = "book_spider"
    urls = extract_links(file_name)
    prefix = "https://link.springer.com"

    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url=url, callback=self.get_download_link)

    def get_download_link(self, response):
        url = response.css(".test-bookpdf-link").attrib["href"]
        book_name = response.css(".page-title h1::text").get()
        author = response.css(".authors__name::text").get()
        download_url = f"{self.prefix}{url}"
        wget.download(download_url, f"./book/{book_name} - {author}.pdf")
