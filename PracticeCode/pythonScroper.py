import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import csv


url = "https://www.amazon.nl/s?k=hoodie&__mk_nl_NL=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=36YBN690F6F90&sprefix=hoodie%2Caps%2C117&ref=nb_sb_noss_1"

response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

product_tags = soup.find_all('div', {'class': 'as-m-product-tile as-m-product-tile--sizes'})



with open('Amazon_reviews.csv', 'w', newline='') as csvfile:
    fieldnames = ['img', 'Price']
    writer = csv.DictWriter(csvfile, fieldnames = fieldnames)

    writer.writeheader()
    for Tags in product_tags:
        img = Tags.find('span', {'class': 'a-size-base-plus a-color-base'}).text.strip()
        Price = Tags.find('span', {'class': 'a-price-whole'}).text.strip()
        writer.writerow({'img': img, 'Price': Price})

# driver = webdriver.Edge()

# driver.get(url)

# cookies = driver.find_element(By.ID, "sp-cc-accept")

# cookies.click()

# # driver.manage().timeouts().implicitlyWait(5, TimeUnit.SECONDS);

# link = driver.find_element(By.ID, "a-link-normal s-no-outline")


# link.click()

