import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import csv

url = 'https://www.bever.nl/c/heren/truien.html'
driver = webdriver.Edge()
driver.get(url)

cookies = driver.find_element(By.ID, "accept-all-cookies")

cookies.click()

# #TruienLinks

# with open('bever_review.csv', 'w', newline='') as csvfile:
#     fieldnames = ['IMG']
#     writer = csv.DictWriter(csvfile, fieldnames = fieldnames)

#     Truien = driver.find_elements(By.CLASS_NAME, 'as-m-product-tile')
    
#     writer.writeheader()
#     for Trui in Truien:
#         # i get the image here
#         Img = driver.find_element(By.CLASS_NAME, "as-m-product-tile__image")
#         src = Img.get_attribute('src')
#         writer.writerow({'IMG': src})

#         TruiLink = driver.find_element(By.CLASS_NAME, 'as-m-product-tile__link')
#         TruiLink.click()

#         ReviewLink = driver.find_element(By.CSS_SELECTOR, 'button.as-a-btn.as-a-btn--link.as-a-btn--s')
#         ReviewLink.click()
#         driver.back()

        


with open('/BeverScrape/bever_review.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['IMG', 'Review']
    writer = csv.DictWriter(csvfile, fieldnames = fieldnames)

    Truien = driver.find_elements(By.CSS_SELECTOR, 'a.as-a-link.as-a-link--container.as-m-product-tile__link')
    links = []                                        
    for i in Truien:
        links.append(i.get_attribute('href'))


    writer.writeheader()
    for link in links:
        driver.get(link)
        # i get the image here
        Div = driver.find_elements(By.CSS_SELECTOR, "div.as-m-slide__magnify")
        Img = Div[0].find_element(By.CSS_SELECTOR, "img")
        src = Img.get_attribute('src')
        image_id = str(uuid.uuid4())  # generate a unique identifier

        # writer.writerow({'IMG': src})

        
        try:
            ReviewLink = driver.find_element(By.CSS_SELECTOR, 'button.as-a-btn.as-a-btn--link.as-a-btn--s')
            ReviewLink.click()
            
        except:
            continue

        reviews = []
        
        Reviews = driver.find_elements(By.CSS_SELECTOR, 'span.as_lt')
        Reviews = driver.find_elements(By.CSS_SELECTOR, 'span.as_lt')
        for review in Reviews:
            reviews.append(review.text)

       # write the image source and the reviews in the CSV file
        writer.writerow({'IMG': src, 'Review': '; '.join(reviews)})

            

            

        



        
        




