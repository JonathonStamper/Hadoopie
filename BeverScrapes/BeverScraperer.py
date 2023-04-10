import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import uuid
import time


# Here the cookies get clicked away
url = 'https://www.bever.nl/c/heren/truien.html'
driver = webdriver.Edge()
driver.get(url)
cookies = driver.find_element(By.ID, "accept-all-cookies")
cookies.click()


with open('BeverScrapes/bever_images.csv', 'w', newline='', encoding='utf-8') as image_file, \
     open('BeverScrapes/bever_review.csv', 'w', newline='', encoding='utf-8') as review_file:
     
    # create the csv writers
    image_fieldnames = ['Image_ID', 'IMG']
    image_writer = csv.DictWriter(image_file, fieldnames=image_fieldnames)

    review_fieldnames = ['Image_ID', 'Review']
    review_writer = csv.DictWriter(review_file, fieldnames=review_fieldnames)

    Truien = driver.find_elements(By.CSS_SELECTOR, 'a.as-a-link.as-a-link--container.as-m-product-tile__link')
    links = []                                        
    for i in Truien:
        links.append(i.get_attribute('href'))


    image_writer.writeheader()
    review_writer.writeheader()
    for link in links:
        driver.get(link)
        # i get the image here
        Div = driver.find_elements(By.CSS_SELECTOR, "div.as-m-slide__magnify")
        Img = Div[0].find_element(By.CSS_SELECTOR, "img")
        src = Img.get_attribute('src')
        image_id = str(uuid.uuid4())  # generate a unique identifier

        # write the image source and its ID to the image csv file
        # image_writer.writerow({'Image_ID': image_id, 'IMG': src})
        
        try:  
            ReviewLink = driver.find_element(By.CSS_SELECTOR, 'button.as-a-btn.as-a-btn--link.as-a-btn--s')
            ReviewLink.click()

            print("button clicked")
            image_writer.writerow({'Image_ID': image_id, 'IMG': src})


            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)

           
            reviews = []
            
        
            Reviews = driver.find_elements(By.CSS_SELECTOR, 'span.as_lt')
            print(f"Number of reviews found for image ID '{image_id}': {len(reviews)}")

        
            for review in Reviews:
                reviews.append(review.text)

            # for review in reviews:
                # write each review and its corresponding image ID to the review csv file
            print(f"image ID '{image_id}'")
            review_writer.writerow({'Image_ID': image_id, 'Review': '; '.join(reviews)})
            review_file.flush()

            
        except:
            continue


            
        # ReviewElement = driver.find_element(By.CSS_SELECTOR, 'div.as-m-popover.as-m-popover--drawer-large.as-m-popover--no-arrow.as-m-popover--drawer.as-m-popover--animated.as-m-popover--always-render.cotopaxi-popover-modal')
        #Reviews = ReviewElement.find_elements(By.CSS_SELECTOR, 'span.as_lt')
            # write the image source and the reviews in the CSV file
       # review_writer.writerow({'Image_ID': image_id, 'Review': '; '.join(reviews)})