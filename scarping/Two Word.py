
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

    # #List Convert into onw word
    # add=' '.join(li)
    # # print(add)

    if len(li) == 2:
        two.append(" ".join(li))

    elif len(li)==3:
        three.append(" ".join(li))
    elif len(li)==4:
        four.append(" ".join(li))
    else:
        pass

print(two, "------------2")
print(three,"-------------3")
print(four,"----------------4")
