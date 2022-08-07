from cmath import inf
from bs4 import BeautifulSoup # scrap the date from a website
import requests # use to get request from the respective url
from csv import writer #use to append all the data extracted from website into a csv file 

website_url = "https://www.pararius.com/apartments/amsterdam?ac=1"

html_page = requests.get(website_url) # HTTP request from the above URl

soup = BeautifulSoup(html_page.content,'html.parser') # content of the page and parse the hhtml page

get_list = soup.find_all('section',class_= "listing-search-item") # class_ for css not py use to list all the required data


with open('house.csv','w',encoding='utf8',newline='') as file:
    the_writer = writer(file)
    attribute = ['Title','Location','Price','Area'] # attributes of the csv file
    the_writer.writerow(attribute)

    # followeing attributes for csv file
    for lists in get_list:
        House_title = lists.find('a', class_="listing-search-item__link--title").text.replace('\n','')
        
        House_location = lists.find('div', class_="listing-search-item__location").text.replace('\n','')
        
        House_price = lists.find('div', class_="listing-search-item__price").text.replace('\n','')
        
        House_square_area = lists.find('li', class_="illustrated-features__item--surface-area").text.replace('\n','')
        
        info = [House_title,House_location,House_price,House_square_area]
        
        the_writer.writerow(info)    # append all the information in row wise
