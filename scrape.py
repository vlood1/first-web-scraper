import requests
from bs4 import BeautifulSoup
from requests.auth import HTTPBasicAuth # example 1/2 of Basic Authentication
from requests.auth import HTTPDigestAuth #example 1 of Digest Authentication
import re

# https://realpython.com/beautiful-soup-web-scraper-python/#reasons-for-automated-web-scraping
# https://pypi.org/project/requests/



# ---- BASIC AUTHENTICATION ---- #
'''this show how to bypass authentication (login protected pages so that they can still be scraped)'''
# example 1
#####      requests.get('https://httpbin.org/basic-auth/user/pass', auth=('user', 'pass')) #########
                          # website here    ^                             # ^^^ enter ^^^ user and password here

#example 2
##### basic = HTTPBasicAuth('user', 'pass')  ####
##### requests.get('https://httpbin.org/basic-auth/user/pass', auth=basic) ####


# ---- DIGEST AUTHENTICATION ---- #
''' another common authentication bypass form'''
#### url = 'https://httpbin.org/digest-auth/auth/user/pass'
#### requests.get(url, auth=HTTPDigestAuth('user', 'pass'))
                                        # ^^^ enter ^^^ user and password here


x = requests.get('https://realpython.com/beautiful-soup-web-scraper-python/#reasons-for-automated-web-scraping')

#print(x.text)

soup = BeautifulSoup(x.content, "html.parser")

# finding by id
# results = soup.find(id="dsq-count-scr")
# print(results.prettify())


# this website has div CLASS so we find by class
items = soup.find_all("div")
script = soup.find_all("script")

#print(items)




# FINDING THINGS E.G.: h1 tag, headers, subheaders , image links etc

print("All h1 tag items: headers")
for h1tag in items:
    h1 = h1tag.find("h1")
    if h1: # to remove the "None"s..
        #print(f"{h1} \n")
        print(h1.text + "\n")


print ("All subheaded tagged items (subheaders h2-h6)")

for subheader in items:
    h2 = subheader.find("h2")
    if h2: # to remove the "None"s..
        print(h2.text + "\n") # .text allows for readability

    h3 = subheader.find("h3")
    if h3: # to remove the "None"s..
        #print(f"{h3} \n")
        print(h3.text + "\n")

    h4 = subheader.find("h4")
    if h4: # to remove the "None"s..
        #print(f"{h4} \n")
        print(h4.text + "\n")

    h5 = subheader.find("h5")
    if h5: # to remove the "None"s..
        #print(f"{h5} \n")
        print(h5.text + "\n")

    h6 = subheader.find("h6")
    if h6: # to remove the "None"s..
        #print(f"{h6} \n")
        print(h6.text + "\n")


print("images!!")

images = soup.find_all()



print("links")

links = soup.find_all("a")
for link in links:
    link_url = link["href"]
    print(f"link: {link_url}\n")


images = soup.find_all('img', {'src': re.compile('.jpg')})

for image in images:
    print(image['src']) 


# find Elements by Class Name and Text Content

webscraper = soup.find_all("h2", string="web scraper") 
print(webscraper)







# import os
# import requests
# from bs4 import BeautifulSoup
# from urllib.parse import urljoin

# def download_images_from_webpage(url, folder="images"):
#     # Step 1: Send a GET request to fetch the HTML content of the webpage
#     response = requests.get(url)
#     response.raise_for_status()  # Raise an error for bad HTTP responses
    
#     # Step 2: Parse the HTML using BeautifulSoup
#     soup = BeautifulSoup(response.text, 'html.parser')
    
#     # Step 3: Find all <img> tags
#     img_tags = soup.find_all('img')
#     if not os.path.exists(folder):
#         os.makedirs(folder)  # Create a folder to store the images
    
#     # Step 4: Loop through <img> tags and download images
#     for i, img in enumerate(img_tags):
#         # Get the 'src' attribute (image URL)
#         img_url = img.get('src')
#         if not img_url:
#             continue  # Skip if no 'src' attribute
        
#         # Convert relative URLs to absolute URLs
#         img_url = urljoin(url, img_url)
        
#         try:
#             # Step 5: Send a GET request to fetch the image data
#             img_response = requests.get(img_url, stream=True)
#             img_response.raise_for_status()
            
#             # Step 6: Save the image locally
#             img_format = img_url.split('.')[-1]
#             img_filename = os.path.join(folder, f"image_{i}.{img_format}")
#             with open(img_filename, 'wb') as img_file:
#                 for chunk in img_response.iter_content(1024):
#                     img_file.write(chunk)
#             print(f"Downloaded: {img_filename}")
#         except requests.RequestException as e:
#             print(f"Failed to download {img_url}: {e}")

# # Example usage
# webpage_url = "https://example.com"  # Replace with your target URL
# download_images_from_webpage(webpage_url)
