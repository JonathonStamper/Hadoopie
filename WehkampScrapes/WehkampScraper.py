import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import uuid
import time

url = 'https://www.wehkamp.nl/heren-kleding-truien/?soort-trui=gebreide-truien&pagina=1' 
driver = webdriver.Edge()
driver.get(url)
time.sleep(2)
cookies = driver.find_element(By.XPATH, '//*[@id="header"]/aside[2]/div/div[1]/div/p[1]/a[1]')
cookies.click()

with open('WehkampScrapes/Wehkamp_images.csv', 'w', newline='', encoding='utf-8') as image_file, \
     open('WehkampScrapes/Wehkamp_reviews.csv', 'w', newline='', encoding='utf-8') as review_file:
     
    # create the csv writers
    image_fieldnames = ['Wehkamp_Image_ID', 'Wehkamp_IMG']
    image_writer = csv.DictWriter(image_file, fieldnames=image_fieldnames)

    review_fieldnames = ['Wehkamp_Image_ID', 'Wehkamp_Review']
    review_writer = csv.DictWriter(review_file, fieldnames=review_fieldnames)

    PaginaNummer = 1
    links = []
    for PaginaNummer in range(6): 
        url_up = 'https://www.wehkamp.nl/heren-kleding-truien/?soort-trui=gebreide-truien&pagina=' +str(PaginaNummer)
        driver.get(url_up)
        Truien = driver.find_elements(By.CSS_SELECTOR, 'a.ct-text-primary.display-block')
        for i in Truien:
            links.append(i.get_attribute('href'))

    print(len(links))
    image_writer.writeheader()
    review_writer.writeheader()    
    for link in links:
        driver.get(link)
        
        try:  
            Img = driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[1]/div/div/div[1]/div/div[1]/div[1]/div/div/div[2]/button/figure/img')
            src = Img.get_attribute('src')
            image_id = str(uuid.uuid4())  # generate a unique identifier

            time.sleep(1)
            
            ReviewButton = driver.find_element(By.CSS_SELECTOR, 'button.ReviewSummary__ba-review-link___PH5fZ.type-link-inline.inline-block.rating-link.margin-left-small.color-black-opacity-88')
            ReviewButton.click()
            
            image_writer.writerow({'Wehkamp_Image_ID': image_id, 'Wehkamp_IMG': src})

            time.sleep(1)


            # time.sleep(1)
            reviews = [] 

            # MeerLezen = driver.find_elements(By.CSS_SELECTOR, 'button.CTA-module--action__AdoYs.CTA-module--medium__kRlC3.CTA-module--reset__ln67B.CTA-module--inline__ykOgZ')

            # for button in MeerLezen:
            #     button.click()
            Reviewsection = driver.find_element(By.CSS_SELECTOR, 'div.Reviews__list___KfPgV')      
            Reviews = Reviewsection.find_elements(By.CSS_SELECTOR, 'p.color-black-opacity-88')

            print(f"Number of reviews found for image ID '{image_id}': {len(Reviews)}")


            for review in Reviews:
                #write each review and its corresponding image ID to the review csv file
                #print(f"image ID '{image_id}'")
                review_writer.writerow({'Wehkamp_Image_ID': image_id, 'Wehkamp_Review': review.text})
                #review_writer.writerow({'Image_ID': image_id, 'Review': '; '.join(reviews)})
                review_file.flush()

            
        except:
            continue

       

