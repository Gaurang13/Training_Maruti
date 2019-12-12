import urllib.request
import json
import csv

response=urllib.request.urlopen('https://api.github.com/search/repositories?q=is:public+language:python&forks:%3E=200')
data = response.read()
if data:
    data = json.loads(data)
    items=data["items"]
    print(len(items))
    
    headers=["name" , "description" , "html_url", "watchers_count", "stargazers_count", "forks_count","language","forks","stargazers_count"]
    require_data=[]
    for i in items:
      if i["stargazers_count"]>2000:
                dic_data={
                        headers[0]:i[headers[0]],
                        headers[1]:i[headers[1]],
                        headers[2]:i[headers[2]],
                        headers[3]:i[headers[3]],
                        headers[4]:i[headers[4]],
                        headers[5]:i[headers[5]],
                        headers[6]:i[headers[6]],
                        headers[7]:i[headers[7]],
                        headers[8]:i[headers[8]],
                        }
                require_data.append(dic_data)

    with open("clean_list.csv","w",newline='') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(require_data)
else:
    print("Not found")