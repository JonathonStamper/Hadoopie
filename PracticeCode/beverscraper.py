import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import csv

PaginaNummer = 0
url = 'https://www.bever.nl/c/heren/truien.html?size=48&page=' + str(PaginaNummer)

response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

product_tags = soup.find_all('div', {'class': 'as-m-product-tile'})


with open('bever_review.csv', 'w', newline='') as csvfile:
    fieldnames = ['name', 'Price']
    writer = csv.DictWriter(csvfile, fieldnames = fieldnames)

    writer.writeheader()
    for PaginaNummer in range(10):
        for Tags in product_tags:
            name = Tags.find('div', {'class': 'as-m-product-tile__title-wrapper'}).text.strip()
            Price = Tags.find('div', {'class': 'as-a-price__value as-a-price__value--sell'}).text.strip()
            print(f"Name: {name}, Price: {Price}")
            writer.writerow({'name': name, 'Price': Price})

print("Data written to CSV file successfully.")


