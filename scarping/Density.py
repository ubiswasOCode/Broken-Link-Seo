import requests
from bs4 import BeautifulSoup
import metadata_parser


def Get_Density_Check(find, word_count):
    msg = []
    if find in word_count:
        density = word_count.count(find)
        words_in_keyword = find.split()
        total_length = len(word_count)
        word_length= len(words_in_keyword)
        try:
            length = round(total_length//word_length,4)
            density_rou = round(density / length,4)
            total_rou = round(density_rou,4)
            exist_keys = total_rou * 100
            msg.append('\n' + str(round(exist_keys,3)) + '%' + ' keyword density')
            msg.append('\nThe keyword appears ' + str(density) + ' times in the page.')
        except ZeroDivisionError:
            msg.append(f'{find} Not Userd')
    else:
        msg.append('\n' + str(find) + 'Not Userd')

    return msg

url = input("enter Url")
req = requests.get(url)
soup = BeautifulSoup(req.content, 'html.parser')
print(soup.prettify())
for para in soup.find_all(""):
    text=para.get_text()

    # print(text)
page = metadata_parser.MetadataParser(url)



##For all Keywords
print(page.get_metadata("keywords"))
word=page.get_metadata("keywords")
word_count =word.split()


find = input('\nWhat keyword are you looking for?: ')
messages = Get_Density_Check(find, word_count)
for message in messages:
    print(message)







