# %%
from bs4 import BeautifulSoup
html = '<b id="szy" class="abc">Hello World</b><span></span><span></span>'
soup = BeautifulSoup(html,'html.parser')
tag = soup.b
print(tag.string)
print(tag['class'])
print(tag.attrs) #provide all the attributes associated with the particular elements
print(tag)
tag['id'] = 'HELLO'
tag['class'] = 'World'
print(tag)
# %%
from bs4 import BeautifulSoup
html = '<b id="szy" class="abc 123">Hello World</b><span></span><span></span>'
soup = BeautifulSoup(html,'html.parser',multi_valued_attributes=None)
tag = soup.b
print(tag['class'])