import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import uuid
import time

PaginaNummer = 1
url = 'https://www.zalando.nl/herenkleding-truien-gebreidetruien/?p=' +str(PaginaNummer)
driver = webdriver.Edge()
driver.get(url)
time.sleep(2)
cookies = driver.find_element(By.CSS_SELECTOR, "button.uc-btn.uc-btn-primary")
cookies.click()

with open('ZalandoScrapes/Zalando_images.csv', 'w', newline='', encoding='utf-8') as image_file, \
     open('ZalandoScrapes/Zalando_reviews.csv', 'w', newline='', encoding='utf-8') as review_file:
     
    # create the csv writers
    image_fieldnames = ['Zalando_Image_ID', 'Zalando_IMG']
    image_writer = csv.DictWriter(image_file, fieldnames=image_fieldnames)

    review_fieldnames = ['Zalando_Image_ID', 'Zalando_Review']
    review_writer = csv.DictWriter(review_file, fieldnames=review_fieldnames)

    # Load meer 10 keer doen
    # Loadmorebutton = driver.find_element(By.CSS_SELECTOR, 'button.button.js-load-more')
    # teller = 0
    #     for teller in range(10):
    #         time.sleep(1)
    #         Loadmorebutton.click()
    #         # teller = teller + 1
    # for PaginaNummer in range(20):
    for PaginaNummer in range(20): 
        Truien = driver.find_elements(By.CSS_SELECTOR, 'a._LM.JT3_zV.CKDt_l.CKDt_l.LyRfpJ')
        links = []                                        
        for i in Truien:
            links.append(i.get_attribute('href'))


        image_writer.writeheader()
        review_writer.writeheader()

    
        for link in links:
            driver.get(link)
            # i get the image here
            Div = driver.find_elements(By.CSS_SELECTOR, "div.KVKCn3.u-C3dd.jDGwVr.mo6ZnF.KLaowZ")
            Img = driver.find_element(By.CSS_SELECTOR, "img._0Qm8W1.u-6V88.FxZV-M._2Pvyxl.JT3_zV.EKabf7.mo6ZnF._1RurXL.mo6ZnF._7ZONEy")
            src = Img.get_attribute('src')
            image_id = str(uuid.uuid4())  # generate a unique identifier
        
            # write the image source and its ID to the image csv file
        
            try:  
                time.sleep(1)

                ReviewButton = driver.find_element(By.XPATH, '//*[@id="z-pdp-all-reviews"]')
                ReviewButton.click()
            
                image_writer.writerow({'Zalando_Image_ID': image_id, 'Zalando_IMG': src})

                time.sleep(1)


            # time.sleep(1)
            # reviews = [] 

            # MeerLezen = driver.find_elements(By.CSS_SELECTOR, 'button.CTA-module--action__AdoYs.CTA-module--medium__kRlC3.CTA-module--reset__ln67B.CTA-module--inline__ykOgZ')

            # for button in MeerLezen:
            #     button.click()
                    
                Reviews = driver.find_elements(By.CSS_SELECTOR, 'p._0Qm8W1.u-6V88.FxZV-M.pVrzNP.f4ql6o')

                print(f"Number of reviews found for image ID '{image_id}': {len(Reviews)}")


                for review in Reviews:
                 #write each review and its corresponding image ID to the review csv file
                 #print(f"image ID '{image_id}'")
                 review_writer.writerow({'Zalando_Image_ID': image_id, 'Zalando_Review': review.text})
                 #review_writer.writerow({'Image_ID': image_id, 'Review': '; '.join(reviews)})
                 review_file.flush()

            
            except:
                continue