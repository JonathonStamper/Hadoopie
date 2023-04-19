import PIL
from PIL import Image
import requests
from io import BytesIO
import webcolors
import pandas as pd
import csv
 
def closest_colour(requested_colour):
   min_colours = {}
   for key, name in webcolors.CSS3_HEX_TO_NAMES.items():
        # skip whitesmoke and ghostwhite
        if name in ['whitesmoke', 'ghostwhite']:
            continue
        
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_colour[0]) ** 2
        gd = (g_c - requested_colour[1]) ** 2
        bd = (b_c - requested_colour[2]) ** 2
        min_colours[(rd + gd + bd)] = name
   return min_colours[min(min_colours.keys())]

def get_image_color(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img = img.convert('RGB')
     
    # resize the image to 300 x 300
    img = img.resize((10,10))
    
    detected_colors = []
    for x in range(img.width):
        for y in range(img.height):
            color = closest_colour(img.getpixel((x, y)))
            if (color != 'whitesmoke'):
                detected_colors.append(color)
    Series_Colors = pd.Series(detected_colors)
    output = Series_Colors.value_counts()
    return output.head(1).index[0]

# Read the CSV file containing the image URLs
with open('Images_Data\H&M_images.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader)
    image_urls = [row[0] for row in reader]

# Open the output CSV file and write the headers
with open('image_colors.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['image_url', 'color'])

    # Loop through the image URLs and write the detected color(s) to the output CSV file
    for url in image_urls:
        try:
            color = get_image_color(url)
            writer.writerow([url, color])
        except:
            print(f"Error processing image at {url}")



























# import csv
# import requests
# from PIL import Image
# import webcolors
# from io import BytesIO



# # Define the function to get the dominant color
# def get_dominant_color(image_url):
#     response = requests.get(image_url)
#     img = Image.open(BytesIO(response.content))
#     colors = img.getcolors(img.size[0]*img.size[1])
#     max_occurence, dominant_color = max(colors)
#     try:
#         dominant_color_name = webcolors.rgb_to_name(dominant_color, spec='css3')
#     except ValueError:
#         # If the RGB value doesn't match a named color in the CSS3 database,
#         # find the closest named color using a custom function
#         hex_color = webcolors.rgb_to_hex(dominant_color)
#         closest_name = get_closest_color_name(hex_color)
#         dominant_color_name = webcolors.CSS3_NAMES_TO_HEX[closest_name]
#     return dominant_color_name

# # Define the function to find the closest named color
# def get_closest_color_name(hex_color):
#     color_diffs = []
#     for color_name, color_hex in webcolors.CSS3_HEX_TO_NAMES.items():
#         color_diff = sum(abs(int(hex_color[i:i+2], 16) - int(color_hex[i:i+2], 16)) for i in (0, 2, 4))
#         color_diffs.append((color_diff, color_name))
#     if not color_diffs:
#         return 'unknown'
#     return min(color_diffs)[1]

# # Read in the CSV file and store the image URLs in a list
# image_links = []
# with open('Images_Data/H&M_images.csv') as csvfile:
#     reader = csv.reader(csvfile)
#     next(reader)
#     for row in reader:
#         image_links.append(row[0])

# # Loop through the image links and get the dominant color for each image
# results = []
# for link in image_links:
#     color = get_dominant_color(link)
#     results.append([link, color])

# # Write the results to a new CSV file
# with open('dominant_colors.csv', 'w', newline='') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(['Image URL', 'Dominant Color'])
#     for row in results:
#         writer.writerow(row)



# import pandas as pd
# from PIL import Image
# from colorthief import ColorThief
# import requests
# from io import BytesIO


# df = pd.read_csv('Images_Data/H&M_images.csv')

# for index, row in df.iterrows():
#     image_url = row['H&M_IMG']
#     try:
#         response = requests.get(image_url)
#         image = Image.open(BytesIO(response.content))
#         color_thief = ColorThief(image)
#         dominant_color = color_thief.get_color(quality=1)
#         df.at[index, 'dominant_color'] = dominant_color
#     except Exception as e:
#         print(f"Error downloading image {image_url}: {e}")




# df.to_csv('Image_colors.csv', index=False)# # read images from URL
# url = "https://lp2.hm.com/hmgoepprod?set=quality%5B79%5D%2Csource%5B%2F62%2F9b%2F629b4e8939d06f8f115bf13a308003cefeae900c.jpg%5D%2Corigin%5Bdam%5D%2Ccategory%5B%5D%2Ctype%5BLOOKBOOK%5D%2Cres%5Bm%5D%2Chmver%5B1%5D&call=url[file:/product/main]"
# response = requests.get(url)
# img = Image.open(BytesIO(response.content))
# img

  
  
# def closest_colour(requested_colour):
#     min_colours = {}
#     for key, name in webcolors.CSS3_HEX_TO_NAMES.items():
#         r_c, g_c, b_c = webcolors.hex_to_rgb(key)
#         rd = (r_c - requested_colour[0]) ** 2
#         gd = (g_c - requested_colour[1]) ** 2
#         bd = (b_c - requested_colour[2]) ** 2
#         min_colours[(rd + gd + bd)] = name
#     return min_colours[min(min_colours.keys())]

# def top_colos(image, n):
#     # convert the image to rgb
#     image = image.convert('RGB')
     
#     # resize the image to 300 x 300
#     image = image.resize((10,10))
     
#     detected_colors = []
#     for x in range(image.width):
#         for y in range(image.height):
#             color = closest_colour(image.getpixel((x, y)))
#             if color != 'whitesmoke':
#                 detected_colors.append(color)
    
#     # count the occurrences of each color
#     Series_Colors = pd.Series(detected_colors)
#     output = Series_Colors.value_counts()
#     print(output.head(n))
#     return output.head(n)

 
 
# top_colos(img,1)




# import PIL
# from PIL import Image
# import requests
# from io import BytesIO
# import pandas as pd
 
# # read image from URL
# url = "https://www.fantasy-milos.com/slider/69/slider_image.jpg"
# response = requests.get(url)
# img = Image.open(BytesIO(response.content))

# # dictionary of CSS3 color names and their RGB values
# css3_colors = {
#     'black': (0, 0, 0),
#     'silver': (192, 192, 192),
#     'gray': (128, 128, 128),
#     'white': (255, 255, 255),
#     'maroon': (128, 0, 0),
#     'red': (255, 0, 0),
#     'purple': (128, 0, 128),
#     'fuchsia': (255, 0, 255),
#     'green': (0, 128, 0),
#     'lime': (0, 255, 0),
#     'olive': (128, 128, 0),
#     'yellow': (255, 255, 0),
#     'navy': (0, 0, 128),
#     'blue': (0, 0, 255),
#     'teal': (0, 128, 128),
#     'aqua': (0, 255, 255)
# }

# def closest_color(requested_color):
#     min_distance = float('inf')
#     closest_color_name = None
#     for name, color in css3_colors.items():
#         r_c, g_c, b_c = color
#         rd = (r_c - requested_color[0]) ** 2
#         gd = (g_c - requested_color[1]) ** 2
#         bd = (b_c - requested_color[2]) ** 2
#         distance = rd + gd + bd
#         if distance < min_distance:
#             min_distance = distance
#             closest_color_name = name
#     return closest_color_name

# def top_colors(image, n):
#     # convert the image to rgb
#     image = image.convert('RGB')
     
#     # resize the image to 300 x 300
#     image = image.resize((300,300))
     
#     detected_colors =[]
#     for x in range(image.width):
#         for y in range(image.height):
#             detected_colors.append(closest_color(image.getpixel((x,y))))
#     series_colors = pd.Series(detected_colors)
#     output = series_colors.value_counts()
#     print(output.head(n))
#     return output.head(n)

# top_colors(img, 10)
