import requests
from bs4 import BeautifulSoup
import metadata_parser

url = "https://www.javatpoint.com/"
req = requests.get(url)
soup = BeautifulSoup(req.content, 'html.parser')
print(soup.prettify())
for para in soup.find_all(""):
    text=para.get_text()

    print(text)
page = metadata_parser.MetadataParser(url)
print(page.get_metadata("keywords"))
word=page.get_metadata("keywords")


word_count =word.split()

find = input('\nWhat keyword are you looking for?: ')

if find in word_count:
    density = word_count.count(find)
    words_in_keyword = find.split()
    a = len(word_count)
    b = len(words_in_keyword)
    while True:
        try:
            c = round(a//b,4)
            d = round(density / c,4)
            e = round(d,4)
            f = e * 100
            print('\n' + str(round(f,3)) + '%' + ' keyword density')
            print('\nThe keyword appears ' + str(density) + ' times in the page.')
            break
        except ZeroDivisionError:
            print('\nDivision by Zero Error, Please input a valid keyword')
            break
else:
    print('\n' + str(find) + ' does not appear in the URL, try again.')
