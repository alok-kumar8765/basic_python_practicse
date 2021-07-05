#****************** Step 1 *******************
# pip install bs4
# pip install resquests
# pip install lxml
import requests
# Step 1: Use the requests library to grab the page
# Note, this may fail if you have a firewall blocking Python/Jupyter 
# Note sometimes you need to run this twice if it fails the first time
res = requests.get("http://www.example.com")
type(res)   #Its is object typee response which hold information from website
#print(res.text)

import bs4
soup=bs4.BeautifulSoup(res.text,'lxml')
#print(soup)

#let grab the title of this web page
#print(soup.select('title'))
#print(soup.select('p'))
#result = soup.select('p')[1].getText()
#print(result)


#let grab all element of class for this we take wikipedia page of grace hoper for example
res=requests.get('https://en.wikipedia.org/wiki/Grace_Hopper')
soup=bs4.BeautifulSoup(res.text,'lxml')
#print(soup)
#items=soup.select('.toctext')[0]
#for item in soup.select('.toctext'):
    #print(item.text)

#lets grab images
res=requests.get('https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)')
soup=bs4.BeautifulSoup(res.text,'lxml')
computer=soup.select('.thumbimage')[0]
print(computer['src'])
#<img src="//upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Kasparov_Magath_1985_Hamburg-2.png/220px-Kasparov_Magath_1985_Hamburg-2.png">
img_link=requests.get('https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Kasparov_Magath_1985_Hamburg-2.png/220px-Kasparov_Magath_1985_Hamburg-2.png')
#print(img_link.content)

#to see img locally
f = open('my_computer_image.png','wb')
f.write(img_link.content)
f.close()

