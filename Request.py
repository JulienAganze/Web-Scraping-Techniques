#%%
import requests
for i in  range(1,11):
    print("Page: ",i)
    url = f'https://quotes.toscrape.com/page/{i}/'
    r = requests.get(url) 
    html = r.text
    with open('Quotes.txt', 'a', encoding='utf-8') as f:
        for line in html.split('\n'):
            if '<span class="text" itemprop="text">' in line:
                line = line.replace('<span class="text" itemprop="text">“', '').replace('”</span>','')
                line = line.strip()
                f.write(line)
                f.write('\n')
# %%
import requests
r = requests.get('https://quotes.toscrape.com/') 
html = r.text
with open('Authors.txt', 'w') as f:
    for line in html.split('\n'):
        if '<span>by <small class="author" itemprop="author">' in line:
            line = line.replace('<span>by <small class="author" itemprop="author">','').replace('</small>','')
            line = line.strip()
            f.write(line)
            f.write('\n')


# %%
import requests
for i in range(1,11): 
    print("Page: ",i)
    url = f'https://quotes.toscrape.com/page/{i}/'
    r = requests.get(url)
    htiml = r.text
    with open("quotes.txt",'a', encoding='utf-8') as f:
        for line in html.split('\n'):
            if '<span class="text" itemprop="text">' in line:
                line = line.replace('<span class="text" itemprop="text">“', '').replace('”</span>','')
                line= line.strip() # removing blank sppaces from both sides
                f.write(line)
                f.write('\n')

# %%
import requests
for i in range(1,11): 
    url = f'https://quotes.toscrape.com/page/{i}/'
    r = requests.get(url)
    htiml = r.text
    with open("Authors.txt",'a') as f:
        for line in html.split('\n'):
            if '<span>by <small class="author" itemprop="author">' in line:
                line = line.replace('<span>by <small class="author" itemprop="author">','').replace('</small>','')
                line = line.strip()
                f.write(line)
                f.write('\n')



# %%

import requests
for i in range(1,11): 
    print("Page: ",i)
    url = f'https://quotes.toscrape.com/page/{i}/'
    r = requests.get(url)
    htiml = r.text
    with open("AuthorsWithquotes.txt",'a', encoding='utf-8') as f:
        for line in html.split('\n'):
            if '<span>by <small class="author" itemprop="author">' in line:
                line = line.replace('<span>by <small class="author" itemprop="author">','').replace('</small>','')
                line = line.strip()
            author = line
            new_line = line + '\n'  

            if '<span class="text" itemprop="text">' in new_line:
                new_line = new_line.replace('<span class="text" itemprop="text">“', '').replace('”</span>','')
                new_line= new_line.strip() # removing blank sppaces from both sides
                quote = new_line
                authorandquotes = author+quote
            f.write(authorandquotes)
            f.write('\n')


#%%
for pat in html.split('\n'):
    print(pat)
#%%
print(type(html1))
print(html1[1])
html1[1]
type(html1[1])
html1.index(line)
# %%
import csv
import requests
for i in range(1,11): 
    print("Page: ",i)
    url = f'https://quotes.toscrape.com/page/{i}/'
    r = requests.get(url)
    html = r.text
    html1 = html.split('\n')
    with open("Athorandquotes.csv",'a', encoding='utf-8') as f:
        writer = csv.writer(f)
        header = ['Page'+str(i)+' Author', 'Quote']
         # write the header
        writer.writerow(header)
        for line in html1:
            if '<span class="text" itemprop="text">' in line:
                #line = line.replace('<span class="text" itemprop="text">“', '').replace('”</span>','')
                #line= line.strip() # removing blank sppaces from both sides
                quoteline = line
                quoteline = quoteline.replace('<span class="text" itemprop="text">“', '').replace('”</span>','').strip()
                authorline = html1[html1.index(line)+1]
                authorline = authorline.replace('<span>by <small class="author" itemprop="author">','').replace('</small>','').strip()
                #print(authorline )
                #print(quoteline+ '\n')
                
                data = [authorline,quoteline]
                writer.writerow(data)
                #authorwithquotes= f'{authorline}, {quoteline}'
                #print(authorwithquotes+'\n')
                #newline = html1
                #f.write(authorwithquotes)
                #f.write('\n')

# %%
type(html1)
type(line)
#html1.index(line)
# %%
print(len(html1))

# %%
import csv
import requests
with open("awqsecond.csv",'a', encoding='utf-8') as f:
        writer = csv.writer(f)
        header = ['Author', 'Quote']
         # write the header
        writer.writerow(header)
        for i in range(1,11): 
            print("Page: ",i)
            url = f'https://quotes.toscrape.com/page/{i}/'
            r = requests.get(url)
            html = r.text
            html1 = html.split('\n')
            
            for line in html1:
                if '<span class="text" itemprop="text">' in line:
                    #line = line.replace('<span class="text" itemprop="text">“', '').replace('”</span>','')
                    #line= line.strip() # removing blank sppaces from both sides
                    quoteline = line
                    quoteline = quoteline.replace('<span class="text" itemprop="text">“', '').replace('”</span>','').strip()
                    authorline = html1[html1.index(line)+1]
                    authorline = authorline.replace('<span>by <small class="author" itemprop="author">','').replace('</small>','').strip()
                    #print(authorline )
                    #print(quoteline+ '\n')
                    
                    data = [authorline,quoteline]
                    writer.writerow(data)
                    #authorwithquotes= f'{authorline}, {quoteline}'
                    #print(authorwithquotes+'\n')
                    #newline = html1
                    #f.write(authorwithquotes)
                    #f.write('\n')


#%%
import requests
r = requests.get('https://quotes.toscrape.com/') 
html = r.text
with open('awqthird.csv','w') as f:
    for line in html.split('\n'):
        if '<span class="text" itemprop="text">' in line:
            line = line.replace('<span class="text" itemprop="text">“', '').replace('”</span>','')
            line= line.strip() # removing blank sppaces from both sides
            quote = line
            

        if '<span>by <small class="author" itemprop="author">' in line:
            line = line.replace('<span>by <small class="author" itemprop="author">','').replace('</small>','')
            line = line.strip()
            author = line
            f.write(author+','+quote)
            f.write('\n')

   
            