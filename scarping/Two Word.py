
import requests
from bs4 import BeautifulSoup
import metadata_parser

url = input("enter Url")
req = requests.get(url)
soup = BeautifulSoup(req.content, 'html.parser')
# print(soup.prettify())

two = []
three = []
four = []

for para in soup.find_all("p"):
    text=para.get_text()
    # print(text)
    "Reinforcement Learning"
    #convert into List
    li=list(text.split())
    print(li)

    if len(li) == 2:
        two.append(" ".join(li))

    elif len(li)==3:
        three.append(" ".join(li))
    elif len(li)==4:
        four.append(" ".join(li))
    else:
        pass


#
for Head1 in soup.find_all("h1"):
    text1=Head1.get_text()
    li2=list(text1.split())
    if len(li2)==2:
        two.append(" ".join(li2))
    elif len(li2)==3:
        three.append(" ".join(li2))
    elif len(li2)==4:
        four.append(" ".join(li2))
    else:
        pass

for Head2 in soup.find_all("h2"):
    text2=Head2.get_text()
    print(text2)
    li3 = list(text2.split())
    if len(li3) == 2:
        two.append(" ".join(li3))
    elif len(li3) == 3:
        three.append(" ".join(li3))
    elif len(li3) == 4:
        four.append(" ".join(li3))
    else:
        pass
#
for Head3 in soup.find_all("h3"):
    text3=Head3.get_text()
    li4 = list(text3.split())
    if len(li4) == 2:
        two.append(" ".join(li4))
    elif len(li4) == 3:
        three.append(" ".join(li4))
    elif len(li4) == 4:
        four.append(" ".join(li4))
    else:
        pass

for Head4 in soup.find_all("h4"):
    text4=Head4.get_text()
    print(text4)
    li5=list(text4.split())
    if len(li5)==2:
        two.append(" ".join(li5))
    elif len(li5)==3:
        three.append(" ".join(li5))
    elif len(li5)==4:
        four.append(" ".join(li5))
    else:
        pass


print(two, "------------2")
print(three,"-------------3")
print(four,"----------------4")