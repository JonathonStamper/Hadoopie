import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import uuid
import time

url = 'https://nl.shein.com/style/Men-Sweater-sc-00131080.html?ici=nl_tab04navbar05menu10dir01&src_module=topcat&src_tab_page_id=page_home1681260160824&src_identifier=fc%3DMen%60sc%3DTops%60tc%3DGebreide%20Items%60oc%3DSweater%60ps%3Dtab04navbar05menu10dir01%60jc%3DitemPicking_00131080&srctype=category&userpath=category-Tops-Gebreide-Items-Sweater' 
driver = webdriver.Edge()
driver.get(url)
time.sleep(1)
cookies = driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')
cookies.click()
xbutton = driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div/div[1]/div/div[2]/div/i')
xbutton.click()

with open('SheinScrapes/Shein_images.csv', 'w', newline='', encoding='utf-8') as image_file, \
     open('SheinScrapes/Shein_reviews.csv', 'w', newline='', encoding='utf-8') as review_file:
     
    # create the csv writers
    image_fieldnames = ['Shein_IMG']
    image_writer = csv.DictWriter(image_file, fieldnames=image_fieldnames)

    review_fieldnames = ['Shein_Review']
    review_writer = csv.DictWriter(review_file, fieldnames=review_fieldnames)

    PaginaNummer = 1
    links = []
    for PaginaNummer in range(5): 
        url_up = 'https://nl.shein.com/style/Men-Sweater-sc-00131080.html?ici=nl_tab04navbar05menu10dir01&src_module=topcat&src_tab_page_id=page_home1681260160824&src_identifier=fc%3DMen%60sc%3DTops%60tc%3DGebreide%20Items%60oc%3DSweater%60ps%3Dtab04navbar05menu10dir01%60jc%3DitemPicking_00131080&srctype=category&userpath=category-Tops-Gebreide-Items-Sweater&page=' +str(PaginaNummer)
        driver.get(url_up)
        Truien = driver.find_elements(By.CSS_SELECTOR, 'a.S-product-item__img-container.j-expose__product-item-img')
        for i in Truien:
            links.append(i.get_attribute('href'))

    print(len(links))
    image_writer.writeheader()
    review_writer.writeheader()    
    for link in links:
        driver.get(link)
        
        try:  
            Img = driver.find_element(By.CSS_SELECTOR, 'img.j-verlok-lazy.loaded')
            src = Img.get_attribute('src')
            image_id = str(uuid.uuid4())  # generate a unique identifier
            

            time.sleep(1)
            
            ReviewButton = driver.find_element(By.CSS_SELECTOR, 'span.product-intro__head-reviews-text')
            ReviewButton.click()

            image_writer.writerow({'Shein_IMG': src})
            # image_writer.writerow({'Wehkamp_Image_ID': image_id, 'Wehkamp_IMG': src})

            # time.sleep(1)


            time.sleep(1)
            reviews = [] 

            # # MeerLezen = driver.find_elements(By.CSS_SELECTOR, 'button.CTA-module--action__AdoYs.CTA-module--medium__kRlC3.CTA-module--reset__ln67B.CTA-module--inline__ykOgZ')

            # # for button in MeerLezen:
            # #     button.click()
            Reviewsection = driver.find_element(By.CSS_SELECTOR, 'div.common-reviews__list-item she-clearfix j-expose__common-reviews__list-item-con')      
            Reviews = Reviewsection.find_elements(By.CSS_SELECTOR, 'div.rate-des')


            for review in Reviews:
                #Write the reviews into the csv file
                review_writer.writerow({'Shein_Review': review.text})
                #review_writer.writerow({'Image_ID': image_id, 'Review': '; '.join(reviews)})
                review_file.flush()

            
        except:
            continue

       

