import requests
from bs4 import BeautifulSoup


def extract(page):
    url = f'https://www.jobs.ie/Jobs.aspx?hd_searchbutton=true&Keywords=Full+Stack+developer&Regions=0&Categories=0&job-search=true'
    header = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"}
    result = requests.get(url, header)
    doc = BeautifulSoup(result.content, "html.parser")
    return doc


def filter_information(doc):
    titles = doc.find_all('div', class_='job-details-header')
    return len(titles)


info = extract(0)
print(filter_information(info))