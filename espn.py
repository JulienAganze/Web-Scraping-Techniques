# %%
import requests
import json
url = 'https://hs-consumer-api.espncricinfo.com/v1/edition/feed?edition=ww&lang=en&page=1&records=1'
res = requests.get(url)
data = json.loads(res.text)
#print(data.keys())
print(data['results'])
for a in data['results'][0]:
    print(data['results'][0])
    print('----------------------')
    print(a[0])

# for a in data.keys():
#     print(data[a])
#     for b in a:
#         for c in b:
#             print(c)
#             print('------------')

# %%
import requests
import json
url = 'https://hs-consumer-api.espncricinfo.com/v1/edition/feed?edition=ww&lang=en&page=1&records=1'
res = requests.get(url)
data = json.loads(res.text)
#print(data.keys())
print(data['results'])
for a,b in data['results'][0].items():
    print(a,b)
    print(a)
    print(b)

    print('----------------------')
    
# %%
import requests
import json
url = 'https://hs-consumer-api.espncricinfo.com/v1/edition/feed?edition=ww&lang=en&page=1&records=1'
res = requests.get(url)
data = json.loads(res.text)
#print(data.keys())
print(data['results'])
for a,b in data['results'][0].items():
    print(a,data['results'][0][a])
    

    print('----------------------')

    # %%
import requests
import json
with open('Matches.txt','w') as f:
        for i in range(1,30):
                url = f'https://hs-consumer-api.espncricinfo.com/v1/edition/feed?edition=ww&lang=en&page={i}&records=1'
                res = requests.get(url)
                data = json.loads(res.text)
                #print(data.keys())
                #print(data['results'])
                #for a,b in data['results'][0].items():
                list1= ['id','title']
                #for element in list1:
                f.write(data['results'][0][list1[0]]+' | '+data['results'][0][list1[1]])
                        #f.write(element+'  |  '+data['results'][0][element])
                f.write('\n')
                        #print(element)
                        #print(data['results'][0][element])
                        #print('----------------------')