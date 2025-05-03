import urllib.request
import bs4
import pandas as pd 
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
r = urllib.request.urlopen("https://hiking.biji.co/index.php?q=news&act=info&id=1458")
print(r.status)
print(r)
#url = "https://hiking.biji.co/index.php?q=news&act=info&id=1458/"


data = r.read().decode("utf-8")

root = bs4.BeautifulSoup(data,"html.parser")

#print(root.prettify())

animals_topic = []
animals_detail = []

animals_top = root.find_all("p")
for i in range(2,11):
    for animal in animals_top[i].contents:
        #print(animal)
        animals_topic.append(animal.string)

#print("hello",animals_topic[0])
#print("lens = ", len(animals_topic))

animals_topic[7] += animals_topic[8]
del animals_topic[8]

for i in range(0,9):
    del animals_topic[i]

for i in range(len(animals_topic)):
    print(animals_topic[i])

animals_del = root.find("div",class_ = "fr-view")
#print(animals_del.find_all('li'))
for i in animals_del.find_all('li'):
    animals_detail.append(i.string) 
    #print(i.string)

# for i in range(len(animals_detail)):
#     print("When i = ",i,animals_detail[i])

for i in range(1,14,6):
    # print(i)
    # print(animals_detail[i])
    del animals_detail[i]

for i in range(18,50,6):
    # print(i)
    # print(animals_detail[i])
    del animals_detail[i]

while(len(animals_detail)  >53):
    del animals_detail[53]

# for i in range(len(animals_detail)):
#     print("When i = ",i,animals_detail[i])

animals = []

for i in range(0,17,6):
    a = ""
    for j in range(i,i+6):
        a = a + str(animals_detail[j])
    a = a.strip()
    print(a)
    animals.append(a)

str123 = ""

for i in range(18,23):
    str123 = str123 + str(animals_detail[i])

str123 = str123.strip()
print(str123)
animals.append(str123)

for i in range(23,52,6):
    a = ""
    for j in range(i,i+6):
        a = a + str(animals_detail[j])
    a = a.strip()
    print(a)
    animals.append(a)

print(len(animals))

