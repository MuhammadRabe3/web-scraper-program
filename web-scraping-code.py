# first i will enter the url link of the website
#i will make a request to catch the website data 
#i will use the response to get the website dom or the html model 
# i will try to understand the pattern of this model 
# i will make a loop tp print the data i need 

import requests
from bs4 import BeautifulSoup

url="http://books.toscrape.com/"

response=requests.get(url)

soup=BeautifulSoup(response.content,'html.parser')

books= soup.find_all("article")

for book in books:
    title = book.h3.a['title']
    rating = book.p['class'][1]
    #book . select * elements which have the class "price_color"
    #after selecting them ..it will return the valuses in a list starting from 0
    # i will select the [0] index inorder to start from the first elememnt in the list and then the seconf and 
    #so on till i finish the loop 
    #after selecting the value, i will gather it using get_text() method.
    price = book.select(".price_color")[0].get_text()[1:]
    print(f"The name of the book is: {title}, its rating is: {rating} star, and its price is: {price}  .")
   
    