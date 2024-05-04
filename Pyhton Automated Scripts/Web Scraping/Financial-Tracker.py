from bs4 import BeautifulSoup
import requests
import csv
from datetime import datetime

# The link to get transaction amount alongside the data
url = 'https://global.americanexpress.com/activity/recent'

def get_amount_by_price(url):
    # Send a GET request to the website
    page = requests.get(url)
    # Parse the HTML content of the webpage with BeautifulSoup
    soup = BeautifulSoup(page.text, "html.parser")
    # Find the table containing the information we want using its class name
    amount_results = soup.find("div",{"class":"dls-gray-06 flex-item-grow body-2 hidden-sm-down"}).find_all("id",{"class":"flex flex-wrap flex-column-md flex-align-center border-b pad-1-tb-sm-down"})

    total = []

    for result in amount_results:
        total_amount = result.find("p",{"class":"col-md-12 pad-0 margin-0"}).text
        price = float(total_amount[1:].replace(",",""))
        total.append(price)
    return total


get_amount_by_price(url)
# Next grab all strong class as Transaction Amount is stored within