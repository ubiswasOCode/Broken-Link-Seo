import requests
from bs4 import BeautifulSoup
import metadata_parser


url = input("enter Url")
req = requests.get(url)
soup = BeautifulSoup(req.content, 'html.parser')
print(soup.prettify())

one=[]
two = []
three = []
four = []

for para in soup.find_all("keywords"):
    text = para.get_text()
    # print(text)

    # convert into List
    li = list(text.split())
    print(li,"-------------keyword")
    if len(li) == 1:
        one.append(" ".join(li))
    elif len(li) == 2:
        two.append(" ".join(li))
    elif len(li) == 3:
        three.append(" ".join(li))
    elif len(li) == 4:
        four.append(" ".join(li))
    else:
        pass
