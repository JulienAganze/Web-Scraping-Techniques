# %%
from bs4 import BeautifulSoup
import requests
r = requests.get('https://quotes.toscrape.com/') 
html = r.text
soup = BeautifulSoup(html,'html.parser')
with open('bs4quotes.txt','w') as f:
    for tag in soup.findAll('span' ,{'class':'text'}):
        f.write(tag.string)
        f.write('\n')


#print(type(soup.span))
#print(soup.title)
#print(soup.title.string)
#print(type(soup.title.string))
#print(soup.title.parent.name)
#print(soup.find_all('a'))

# %%
from bs4 import BeautifulSoup
import requests
r = requests.get('https://quotes.toscrape.com/') 
html = r.text
soup = BeautifulSoup(html,'html.parser')
with open('bs4authors.csv','w') as f:
    for tag in soup.findAll('small' ,{'class':'author'}):
        f.write(tag.string)
        f.write('\n')


# %%
