import requests # make a request to retrieve the page
from bs4 import BeautifulSoup # html parser
import pandas as pd

base_url = "https://hotels.ng/hotels-in-abia"
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36"}

response_page = requests.get(base_url,headers=header)

print("Connecting")
if response_page.status_code == 200:
    print("Connected Successfully")
else:
    print("Connection not Successful")

#To parse the html page...
parsed_page = BeautifulSoup(response_page.text, 'html.parser')

target = parsed_page.find('div', id='topPicks')
hotel_listing = target.find_all('div',class_="listing-hotels")
print(len(hotel_listing))

# Initialize an empty list to store all hotel dictionaries
all_hotels_listing = []

for listing in hotel_listing:
    hotel_name = listing.find('h2',class_="listing-hotels-name").text
    hotel_address = listing.find('p', class_='listing-hotels-address color-dark').text.strip().split()
    hotel_address = " ".join(hotel_address).split(' - ')
    address = hotel_address[1]
    city = hotel_address[0].split(',')[0]
    state = hotel_address[0].split(',')[1].strip()
    price = listing.find('p', class_='listing-hotels-prices-discount').text
    price = price.strip().split()[0].replace('₦', '').replace(',', '')
    rated = listing.findChild('p', class_='listing-hotels-rating')
    if rated is None:
        rating = "Not Available"
        index = "No Index"
    else:
        rating = rated.text.split(' - ')[0]
        index = rated.text.split(' - ')[1]
    facility = listing.find('div', class_='listing-hotels-facilities d-none d-md-flex')
    if facility is None:
        facilities = "No facilities recorded"
    else:
        all_facilities = facility.findChildren()
        all_facilities = [fac.find('p').text for fac in all_facilities if fac.find('p') is not None]
        all_facilities = ", ".join(all_facilities)
    likes = listing.find('div', class_='listing-hotels-likes').text
    likes = likes.strip().split()[0]

# Create a dictionary for the current hotel
    hotels_listing = {
        'hotel_name': hotel_name,
        'hotel_address': address,
        'city': city,
        'state': state,
        'price': price,
        'rating': rating,
        'rating_index': index,
        'facilities': all_facilities,
        'likes': likes
    }
    # Append the dictionary to the list
    all_hotels_listing.append(hotels_listing) 

# Print the list of all hotels   
print(all_hotels_listing)