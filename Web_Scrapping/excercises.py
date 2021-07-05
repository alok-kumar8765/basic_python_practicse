# cmd line to import lib for scrape a website
import requests
import bs4

#write line of code to connect https://wuotes.toscrape.com and get html txt
res=requests.get('http://quotes.toscrape.com')
#print(res.text)

#get the name of auther from home page
soup=bs4.BeautifulSoup(res.text,'lxml')
soup.select('.author')
authors=set()
for name in soup.select('.author'):
    authors.add(name.text)
#print(authors)

#create list of all quotes on first page
quotes=[]
for quote in soup.select('.text'):
    quotes.append(quote.text)
#print(quotes)

#top 10 tag,
for item in soup.select('.tag-item'):
   #print(item.text)
   pass

#get author from 1 to last pages
url='http://quotes.toscrape.com/page/'
authors=set()
for page in range(1,10):
    page_url=url+str(page)
    res=requests.get(page_url)
    soup=bs4.BeautifulSoup(res.text,'lxml')
    for name in soup.select('.author'):
        authors.add(name.text)
print(authors)

# let find authors but this time page number loop break when web site say no quote found
page_still_valid=True
authors=set()
page=1

while page_still_valid:
    page_url=url+str(page)
    res=requests.get(page_url)
    if "No quotes found!" in res.text:
        break
    soup=bs4.BeautifulSoup(res.text,'lxml')
    for name in soup.select('.author'):
        authors.add(name.text)
    page=page+1
print(authors)