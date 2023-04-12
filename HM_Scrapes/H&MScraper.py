import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import uuid
import time


# Here the cookies get clicked away
url = 'https://www2.hm.com/nl_nl/heren/shop-op-item/truien-en-hoodies.html?sort=stock&productTypes=Sweater&image-size=big&image=stillLife&offset=0&page-size=36'
driver = webdriver.Edge()
driver.get(url)
time.sleep(1)
cookies = driver.find_element(By.ID, "onetrust-accept-btn-handler")
cookies.click()


with open('Images_Data/H&M_images.csv', 'w', newline='', encoding='utf-8') as image_file, \
     open('Reviews_Data/H&M_reviews.csv', 'w', newline='', encoding='utf-8') as review_file:
     
    # create the csv writers
    image_fieldnames = ['H&M_IMG']
    image_writer = csv.DictWriter(image_file, fieldnames=image_fieldnames)

    review_fieldnames = ['H&M_Review']
    review_writer = csv.DictWriter(review_file, fieldnames=review_fieldnames)

    # Load meer 10 keer doen
    Loadmorebutton = driver.find_element(By.CSS_SELECTOR, 'button.button.js-load-more')
    teller = 0
    for teller in range(12):
        time.sleep(1)
        Loadmorebutton.click()
        # teller = teller + 1

    Truien = driver.find_elements(By.CSS_SELECTOR, 'a.item-link.remove-loading-spinner')
    print(len(Truien))
    links = []                                        
    for i in Truien:
        links.append(i.get_attribute('href'))

    print(len(links))
    image_writer.writeheader()
    review_writer.writeheader()
    for link in links:
        driver.get(link)
        # i get the image here
        Div = driver.find_elements(By.CSS_SELECTOR, "div.product-detail-main-image-container")
        Img = Div[0].find_element(By.XPATH, "img")
        src = Img.get_attribute('src')
        # image_id = str(uuid.uuid4())  # generate a unique identifier

        # write the image source and its ID to the image csv file
        
        try:  
            # time.sleep(1)
            ReviewButtonSection = driver.find_element(By.ID, 'reviews-trigger')
            ReviewButton = ReviewButtonSection.find_element(By.CSS_SELECTOR, 'button.CTA-module--action__AdoYs.CTA-module--medium__kRlC3.CTA-module--reset__ln67B')

            ReviewButton.click()
            image_writer.writerow({'H&M_IMG': src})

            time.sleep(1)
            reviews = [] 
            
            MeerLezen = driver.find_elements(By.CSS_SELECTOR, 'button.CTA-module--action__AdoYs.CTA-module--medium__kRlC3.CTA-module--reset__ln67B.CTA-module--inline__ykOgZ')

            for button in MeerLezen:
                button.click()
                    
            Reviews = driver.find_elements(By.CSS_SELECTOR, 'p.BodyText-module--general__KTCW3.Review-module--reviewContent__TnZII')
            # print(f"Number of reviews found for image ID '{image_id}': {len(reviews)}")


            for review in Reviews:
                #write each review and its corresponding image ID to the review csv file
                # print(f"image ID '{image_id}'")
                review_writer.writerow({'H&M_Review': review.text})
                # review_writer.writerow({'Image_ID': image_id, 'Review': '; '.join(reviews)})
                review_file.flush()


            
        except:
            continue

        
        
        















        # ReviewElement = driver.find_element(By.CSS_SELECTOR, 'div.as-m-popover.as-m-popover--drawer-large.as-m-popover--no-arrow.as-m-popover--drawer.as-m-popover--animated.as-m-popover--always-render.cotopaxi-popover-modal')
        #Reviews = ReviewElement.find_elements(By.CSS_SELECTOR, 'span.as_lt')
            # write the image source and the reviews in the CSV file
       # review_writer.writerow({'Image_ID': image_id, 'Review': '; '.join(reviews)})