import requests
import bs4

base_url='https://books.toscrape.com/catalogue/category/books_1/page-{}.html'
#we are not fixing page number actually we use loop to go all pages from 1 to last
res=requests.get(base_url.format(1))
soup=bs4.BeautifulSoup(res.text,'lxml')
#print(len(soup.select('.product_pod')))
#above line is to check no of page in that site
products=soup.select('.product_pod')
example=products[0]
#print(example)
#print(example.select('a')[1]['title'])
example.select('a')[1]['title']
two_star_title=[]

for n in range(1,51):
    scrap_url=base_url.format(n)
    res=requests.get(scrap_url)
    
    soup=bs4.BeautifulSoup(res.text,'lxml')
    books=soup.select('.product_pod')
    
    for book in books:
        #if 'star-rating Two' in str(book)
        if len(book.select('.star-rating.Two')) !=0:
            book_title=book.select('a')[1]['title']
            two_star_title.append(book_title)
    print(two_star_title)